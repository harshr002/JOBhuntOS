import streamlit as st
import pandas as pd
from pathlib import Path

from src.freshness_filter import get_freshness_priority
from src.matcher import calculate_match_score
from src.scraper import fetch_demo_jobs
from src.outreach import generate_cold_message
from src.cover_letter import generate_cover_letter
from src.auto_apply import auto_apply
from src.resume_selector import select_resume
from src.tracker import today_date, followup_date, generate_followup_message
from src.email_agent import create_gmail_compose_link
from src.recruiter_finder import generate_recruiter_emails
from src.priority import calculate_final_priority_score
from src.exporter import export_apply_queue
from src.direct_apply_finder import find_direct_apply_jobs
from src.resume_parser import parse_resume


st.set_page_config(
    page_title="JobHuntOS",
    layout="wide"
)

st.title("JobHuntOS")
st.subheader("AI Job Search + Resume Match + Direct Apply Agent")

DATA_PATH = Path("data/jobs.csv")
UPLOAD_DIR = Path("resumes")
UPLOAD_DIR.mkdir(exist_ok=True)

COLUMNS = [
    "source",
    "company",
    "role",
    "location",
    "posted_time",
    "job_link",
    "experience",
    "skills",
    "match_score",
    "freshness_priority",
    "final_score",
    "priority_label",
    "status",
    "applied_date",
    "followup_date",
    "notes",
    "recruiter_email"
]


def load_jobs():
    if DATA_PATH.exists() and DATA_PATH.stat().st_size > 0:
        df = pd.read_csv(DATA_PATH, dtype=str)

        for col in COLUMNS:
            if col not in df.columns:
                df[col] = ""

        return df[COLUMNS]

    return pd.DataFrame(columns=COLUMNS)


def save_jobs(df):
    df.to_csv(DATA_PATH, index=False)


def refresh_scores(df):
    if df.empty:
        return df

    df = df.copy()

    for idx, row in df.iterrows():
        match_score = pd.to_numeric(
            row.get("match_score", 0),
            errors="coerce"
        )

        if pd.isna(match_score):
            match_score = 0

        final_score, priority_label = calculate_final_priority_score(
            int(match_score),
            row.get("freshness_priority", ""),
            row.get("role", ""),
            row.get("skills", ""),
            row.get("source", ""),
            row.get("experience", "")
        )

        df.at[idx, "final_score"] = str(final_score)
        df.at[idx, "priority_label"] = str(priority_label)

    return df


jobs = load_jobs()
jobs = refresh_scores(jobs)
save_jobs(jobs)


# -------------------------------
# Resume Upload + Scan
# -------------------------------

st.divider()
st.subheader("Resume Intelligence")

uploaded_resume = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)

resume_skills = []

if uploaded_resume:
    resume_path = UPLOAD_DIR / uploaded_resume.name

    with open(resume_path, "wb") as file:
        file.write(uploaded_resume.getbuffer())

    parsed_resume = parse_resume(resume_path)
    resume_skills = parsed_resume["skills"]

    st.success("Resume uploaded and scanned successfully.")

    st.write("Detected Skills:")

    if resume_skills:
        st.write(", ".join(resume_skills))
    else:
        st.warning("No known skills detected. We may need to improve the parser.")


# -------------------------------
# Metrics
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", len(jobs))

col2.metric(
    "Apply First",
    len(jobs[jobs["priority_label"] == "Apply First"]) if not jobs.empty else 0
)

col3.metric(
    "Applied",
    len(jobs[jobs["status"] == "Applied"]) if not jobs.empty else 0
)

col4.metric(
    "Interviews",
    len(jobs[jobs["status"] == "Interview"]) if not jobs.empty else 0
)


# -------------------------------
# Clear Jobs
# -------------------------------

if st.button("Clear All Jobs"):
    jobs = pd.DataFrame(columns=COLUMNS)
    save_jobs(jobs)
    st.success("All jobs cleared.")
    st.rerun()


# -------------------------------
# Direct Apply Finder
# -------------------------------

st.divider()
st.subheader("Prompt-Based Direct Apply Finder")

user_prompt = st.text_area(
    "Tell AI what jobs you want",
    placeholder="Example: data analyst remote india fresher SQL Python",
    height=100
)

if st.button("Find Direct Apply Jobs"):
    direct_jobs = find_direct_apply_jobs(
        user_prompt,
        limit=30
    )

    if not direct_jobs:
        st.warning("No direct jobs found for this prompt.")
    else:
        for job in direct_jobs:
            priority = "Highest"

            combined_text = f"{job.get('skills', '')} {' '.join(resume_skills)}"

            match_score = calculate_match_score(combined_text)

            final_score, priority_label = calculate_final_priority_score(
                match_score,
                priority,
                job.get("role", ""),
                combined_text,
                job.get("source", ""),
                job.get("experience", "")
            )

            new_job = {
                "source": str(job.get("source", "")),
                "company": str(job.get("company", "")),
                "role": str(job.get("role", "")),
                "location": str(job.get("location", "")),
                "posted_time": str(job.get("posted_time", "")),
                "job_link": str(job.get("job_link", "")),
                "experience": str(job.get("experience", "")),
                "skills": str(combined_text),
                "match_score": str(match_score),
                "freshness_priority": priority,
                "final_score": str(final_score),
                "priority_label": str(priority_label),
                "status": "Pending",
                "applied_date": "",
                "followup_date": "",
                "notes": "",
                "recruiter_email": ""
            }

            jobs = pd.concat(
                [jobs, pd.DataFrame([new_job])],
                ignore_index=True
            )

        jobs = jobs.drop_duplicates(
            subset=["job_link"],
            keep="first"
        )

        jobs = refresh_scores(jobs)
        save_jobs(jobs)

        st.success(f"{len(direct_jobs)} direct jobs added.")
        st.rerun()


# -------------------------------
# Export
# -------------------------------

st.divider()

export_file = export_apply_queue(
    jobs,
    limit=50
)

if export_file:
    with open(export_file, "rb") as file:
        st.download_button(
            label="Download Top Apply Queue",
            data=file,
            file_name=Path(export_file).name,
            mime="text/csv"
        )


# -------------------------------
# Job Pipeline
# -------------------------------

st.divider()
st.subheader("Job Pipeline")

if jobs.empty:
    st.info("No jobs yet.")

else:
    jobs["final_score_num"] = pd.to_numeric(
        jobs["final_score"],
        errors="coerce"
    ).fillna(0)

    jobs = jobs.sort_values(
        by="final_score_num",
        ascending=False
    )

    for index, row in jobs.iterrows():
        selected_resume = select_resume(
            row["role"],
            row["skills"]
        )

        with st.expander(
            f"{row['priority_label']} | {row['company']} | {row['role']} | Score: {row['final_score']}"
        ):
            st.write(f"Source: {row['source']}")
            st.write(f"Location: {row['location']}")
            st.write(f"Posted: {row['posted_time']}")
            st.write(f"Status: {row['status']}")
            st.write(f"Match Score: {row['match_score']}%")
            st.write(f"Recommended Resume: {selected_resume}")
            st.write(f"Apply Link: {row['job_link']}")

            cold_msg = generate_cold_message(
                row["company"],
                row["role"]
            )

            st.text_area(
                "Cold Message",
                cold_msg,
                height=150,
                key=f"cold_{index}"
            )

            suggested_emails = generate_recruiter_emails(
                row["job_link"]
            )

            if suggested_emails:
                st.write("Suggested Recruiter Emails:")

                for email in suggested_emails:
                    st.code(email)

            recruiter_email = st.text_input(
                "Recruiter Email",
                value=str(row.get("recruiter_email", "")),
                key=f"email_{index}"
            )

            if st.button("Save Email", key=f"save_email_{index}"):
                jobs.loc[index, "recruiter_email"] = recruiter_email
                save_jobs(jobs)
                st.success("Saved.")
                st.rerun()

            if recruiter_email:
                gmail_link = create_gmail_compose_link(
                    recruiter_email,
                    f"Application for {row['role']}",
                    cold_msg
                )

                st.markdown(
                    f"[Open Gmail Draft]({gmail_link})",
                    unsafe_allow_html=True
                )

            cover_letter = generate_cover_letter(
                row["company"],
                row["role"],
                selected_resume
            )

            st.text_area(
                "Cover Letter",
                cover_letter,
                height=220,
                key=f"cover_{index}"
            )

            followup_msg = generate_followup_message(
                row["company"],
                row["role"]
            )

            st.text_area(
                "Follow-up Message",
                followup_msg,
                height=180,
                key=f"followup_{index}"
            )

            col_a, col_b, col_c = st.columns(3)

            with col_a:
                if st.button("Auto Apply", key=f"apply_{index}"):
                    result = auto_apply(
                        row["job_link"],
                        selected_resume
                    )
                    st.success(result)

            with col_b:
                if st.button("Mark Applied", key=f"mark_{index}"):
                    jobs.loc[index, "status"] = "Applied"
                    jobs.loc[index, "applied_date"] = today_date()
                    jobs.loc[index, "followup_date"] = followup_date(3)
                    save_jobs(jobs)
                    st.success("Applied.")
                    st.rerun()

            with col_c:
                if st.button("Mark Interview", key=f"interview_{index}"):
                    jobs.loc[index, "status"] = "Interview"
                    save_jobs(jobs)
                    st.success("Interview marked.")
                    st.rerun()