# 🚀 JobHuntOS

### Your AI-Powered Job Search & Application Operating System

> **Stop searching for jobs. Start operating your job search.**

JobHuntOS is an AI-powered job discovery and application assistant designed to automate the repetitive parts of a modern job search.

Instead of manually opening dozens of websites, repeating the same searches, comparing job descriptions, checking your resume against requirements, writing outreach messages, and maintaining spreadsheets, JobHuntOS brings the entire workflow into one intelligent system.

---

## 🧠 The Vision

Finding a job is not a single task.

It is a continuous pipeline:

```text
Discover → Filter → Understand → Match → Apply → Reach Out → Follow Up → Track
```

JobHuntOS is being built to automate this entire pipeline.

You provide:

```text
Your Resume
     +
Natural-Language Job Search Prompt
```

For example:

```text
Data Analyst remote India fresher
SQL Python Power BI
```

JobHuntOS works toward transforming that request into a prioritized list of relevant opportunities.

```text
                         ┌──────────────────────┐
                         │    USER PROMPT       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   JOB DISCOVERY      │
                         │                      │
                         │ APIs                 │
                         │ Job Boards           │
                         │ ATS Platforms        │
                         │ Career Pages         │
                         │ Web Sources          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  JOB NORMALIZATION   │
                         │                      │
                         │ Deduplication        │
                         │ Company extraction   │
                         │ Location             │
                         │ Experience           │
                         │ Freshness            │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
          ┌──────────────────────┐       ┌──────────────────────┐
          │ RESUME INTELLIGENCE  │       │   JOB INTELLIGENCE   │
          │                      │       │                      │
          │ Skills               │       │ Requirements         │
          │ Projects             │       │ Experience           │
          │ Technologies         │       │ Skills               │
          │ Experience           │       │ Location             │
          │ Education            │       │ Freshness            │
          └──────────┬───────────┘       └──────────┬───────────┘
                     │                              │
                     └──────────────┬───────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   MATCHING ENGINE    │
                         │                      │
                         │ Resume ↔ Job        │
                         │ Compatibility        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   PRIORITY ENGINE    │
                         │                      │
                         │ Match Score          │
                         │ Relevance            │
                         │ Freshness            │
                         │ Experience Fit       │
                         └──────────┬───────────┘
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                       ▼                         ▼
              ┌────────────────┐       ┌────────────────┐
              │ APPLICATION    │       │   OUTREACH     │
              │                │       │                │
              │ Direct Link    │       │ Cold Message   │
              │ Resume Select  │       │ Recruiter      │
              │ Apply Assist   │       │ Follow-up      │
              └────────┬───────┘       └────────┬───────┘
                       │                        │
                       └────────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ APPLICATION TRACKER  │
                         │                      │
                         │ Saved                │
                         │ Applied              │
                         │ Follow-up            │
                         │ Interview            │
                         │ Rejected             │
                         │ Offer                │
                         └──────────────────────┘
```

---

# 🎯 What Problem Does JobHuntOS Solve?

Traditional job searching looks like this:

```text
Open Job Website
       ↓
Search for Jobs
       ↓
Open Job
       ↓
Read Job Description
       ↓
Compare Resume
       ↓
Apply
       ↓
Find Recruiter
       ↓
Write Message
       ↓
Track Application
       ↓
Repeat
```

Doing this dozens of times every day creates enormous repetitive work.

JobHuntOS changes that workflow into:

```text
Tell the system what you want
          ↓
Discover opportunities
          ↓
Analyze the jobs
          ↓
Compare them with your resume
          ↓
Rank the best opportunities
          ↓
Apply or assist with applying
          ↓
Generate personalized outreach
          ↓
Track everything
          ↓
Follow up
```

The goal is simple:

> **Let the candidate spend more time making career decisions and less time performing repetitive job-search tasks.**

---

# ✨ Key Features

## 🔎 1. Natural-Language Job Search

Users can describe exactly what they want using a normal sentence.

Example:

```text
Data Analyst remote India fresher SQL Python
```

Another example:

```text
Python Developer
0-2 years experience
Remote
India
FastAPI
AWS
```

Instead of forcing users to configure dozens of filters, JobHuntOS is designed around natural-language intent.

---

# 🌐 2. Multi-Source Job Discovery

The long-term goal is to search across a broad range of available job sources instead of depending on a single job website.

Potential sources include:

```text
Job APIs
Job Aggregators
ATS Platforms
Company Career Pages
Public Job Boards
Search Engines
Other Public Web Sources
```

The architecture is designed so additional sources can be added without rewriting the entire application.

```text
                 JOB SEARCH REQUEST
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Source A       Source B       Source C
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  NORMALIZATION
                         │
                         ▼
                    DEDUPLICATION
                         │
                         ▼
                    JOB DATABASE
```

---

# 📄 3. Resume Intelligence

Upload your resume and let JobHuntOS extract useful information.

The system is designed to identify:

- Skills
- Programming languages
- Frameworks
- Tools
- Technologies
- Projects
- Experience
- Education
- Domain keywords

Example:

```text
Resume PDF
    ↓
Text Extraction
    ↓
Information Extraction
    ↓
Candidate Profile
    ↓
Matching Engine
```

---

# 🧠 4. Resume ↔ Job Matching

A job is valuable only when it matches the candidate.

JobHuntOS evaluates the compatibility between the candidate profile and the job.

Example:

```text
MATCH ANALYSIS

Python                 ██████████  95%
SQL                    █████████  90%
Power BI               █████████  88%
FastAPI                ████████   82%
AWS                    ███████    72%

Overall Match: 89%
```

The goal is to help users answer:

> **"Should I spend my time applying to this job?"**

---

# ⚡ 5. Intelligent Job Ranking

Not every job deserves equal attention.

JobHuntOS can combine multiple factors to calculate a priority score.

```text
Resume Match
      +
Role Relevance
      +
Skill Compatibility
      +
Experience Compatibility
      +
Location Compatibility
      +
Job Freshness
      ↓
Final Priority Score
```

Example:

| Priority | Match | Freshness | Recommendation |
|---|---:|---|---|
| 🔥 Highest | 94% | < 1 hour | Apply immediately |
| 🔥 High | 89% | < 24 hours | Apply today |
| 🟡 Medium | 76% | 1–3 days | Review |
| ⚪ Low | 54% | Older | Optional |

---

# 🔗 6. Direct Application Links

JobHuntOS is designed to return the application destination whenever a usable direct link is available.

Each result can contain:

```text
Company
Role
Location
Source
Posted Time
Match Score
Priority
Application Link
```

Example:

```text
┌────────────────────────────────────────────┐
│ 🔥 HIGH PRIORITY                           │
│                                            │
│ Data Analyst                               │
│ Example Company                            │
│ Remote • India                             │
│                                            │
│ Resume Match: 91%                          │
│                                            │
│ [ OPEN APPLICATION ]                       │
└────────────────────────────────────────────┘
```

---

# 💬 7. AI Cold Outreach

Applying to a job is only one part of the process.

JobHuntOS can generate personalized outreach based on:

```text
Candidate Profile
       +
Company
       +
Role
       +
Relevant Skills
```

Example:

```text
Hi [Recruiter],

I came across the Data Analyst opportunity at
[Company]. My background in Python, SQL and data
analysis aligns closely with the requirements of
the role.

I would be grateful if you could consider my
profile for the opportunity.

Best,
[Candidate]
```

The objective is to combine:

```text
Applications
      +
Networking
      +
Recruiter Outreach
```

---

# ✉️ 8. Recruiter Outreach

JobHuntOS is designed to support recruiter communication workflows.

Potential capabilities include:

- Recruiter discovery
- Recruiter email collection where publicly available
- Personalized outreach
- Gmail draft generation
- Follow-up message generation
- Outreach tracking

---

# 📝 9. AI Cover Letters

Generate a role-specific cover letter using:

```text
Resume
   +
Job Description
   +
Company
   +
Role
```

Instead of using one generic cover letter for every application.

---

# 📅 10. Application Tracking

Applications can move through a structured pipeline:

```text
DISCOVERED
    ↓
SHORTLISTED
    ↓
APPLIED
    ↓
FOLLOW-UP
    ↓
INTERVIEW
    ↓
OFFER
```

Alternative path:

```text
DISCOVERED → REJECTED
```

This helps eliminate the classic:

> "Did I already apply to this company?"

problem.

---

# 📊 11. Application Queue

JobHuntOS can generate a prioritized application queue.

Example:

```text
TODAY'S APPLY QUEUE

01  🔥 AI Engineer          96%
02  🔥 Python Developer     93%
03  🔥 Data Analyst         91%
04  🔥 ML Engineer          89%
05  🟡 Backend Engineer     82%
06  🟡 Data Scientist       78%
```

Instead of applying randomly, candidates can focus on the highest-value opportunities first.

---

# 🤖 Agentic Automation

The long-term vision is to turn JobHuntOS into an agentic job-search system.

The candidate provides a goal:

```text
Find remote Data Analyst jobs in India
suitable for a fresher with SQL and Python.
```

The system can then orchestrate multiple specialized capabilities:

```text
                  USER GOAL
                      │
                      ▼
              ORCHESTRATOR AGENT
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Search Agent  Resume Agent  Matching Agent
        │             │             │
        ▼             ▼             ▼
     Sources      Candidate       Scores
                   Profile
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
              Priority Engine
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Application Agent        Outreach Agent
          │                       │
          ▼                       ▼
      Apply Flow             Recruiter Flow
          │                       │
          └───────────┬───────────┘
                      ▼
               Tracking Agent
                      │
                      ▼
                Application DB
```

---

# 🏗️ Architecture

Current project structure:

```text
JobHuntOS/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── src/
│   ├── direct_apply_finder.py
│   ├── resume_parser.py
│   ├── matcher.py
│   ├── priority.py
│   ├── auto_apply.py
│   ├── outreach.py
│   ├── cover_letter.py
│   ├── tracker.py
│   ├── recruiter_finder.py
│   ├── email_agent.py
│   ├── exporter.py
│   ├── resume_selector.py
│   └── ...
│
└── data/
```

---

# 🛠️ Technology Stack

## Frontend

- Streamlit

## Backend

- Python

## Data Processing

- Pandas

## Resume Processing

- PDF parsing
- Text extraction
- Skill extraction

## Job Discovery

- External Job APIs
- Job Aggregators
- ATS Platforms
- Public Career Pages
- Web Discovery

## AI Layer

Designed to support:

- Large Language Models
- Resume analysis
- Job understanding
- Semantic matching
- Personalized communication
- Agent orchestration

## Development

- Git
- GitHub
- Python Virtual Environments
- Environment Variables

---

# 📂 Project Structure

```text
JobHuntOS/
│
├── app.py                         # Main Streamlit application
│
├── src/
│   ├── direct_apply_finder.py    # Job discovery
│   ├── resume_parser.py          # Resume processing
│   ├── matcher.py                # Job/resume matching
│   ├── priority.py               # Priority calculation
│   ├── auto_apply.py             # Application automation
│   ├── outreach.py               # Outreach generation
│   ├── cover_letter.py           # Cover letter generation
│   ├── tracker.py                # Application tracking
│   ├── recruiter_finder.py       # Recruiter discovery
│   ├── email_agent.py            # Email workflows
│   ├── exporter.py               # Export application queue
│   └── resume_selector.py        # Resume selection
│
├── data/
│   └── jobs.csv                  # Local application data
│
├── resumes/
│   └── ...                        # Local resumes
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/harshr002/JOBhuntOS
cd JobHuntOS
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

Never commit your `.env` file.

The repository provides:

```text
.env.example
```

as a safe configuration template.

---

# ▶️ Run JobHuntOS

Start the application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL displayed in your terminal.

---

# 💡 Example Workflow

## Step 1 — Upload Resume

```text
resume.pdf
```

JobHuntOS extracts your skills and candidate information.

---

## Step 2 — Enter a Job Search Prompt

```text
Data Analyst remote India fresher SQL Python Power BI
```

---

## Step 3 — Discover Jobs

The system searches available job sources and collects relevant opportunities.

---

## Step 4 — Analyze Jobs

Each opportunity can be evaluated against:

```text
Resume
+
Skills
+
Experience
+
Location
+
Role
+
Freshness
```

---

## Step 5 — Prioritize

The strongest opportunities are ranked first.

---

## Step 6 — Review the Application

The user can:

```text
Open Application
Add to Pipeline
Generate Cover Letter
Generate Recruiter Message
Auto Apply*
```

---

## Step 7 — Track

Move applications through:

```text
Saved
Applied
Follow-up
Interview
Offer
Rejected
```

---

# 📈 Roadmap

## ✅ Completed / In Progress

- [x] Streamlit dashboard
- [x] Prompt-based job search
- [x] External job API integration
- [x] Job result ingestion
- [x] Resume PDF upload
- [x] Resume text extraction
- [x] Basic skill extraction
- [x] Job matching
- [x] Job scoring
- [x] Priority ranking
- [x] Direct application links
- [x] Saved job pipeline
- [x] Application status tracking
- [x] Cold message generation
- [x] Cover letter generation
- [x] Recruiter outreach support
- [x] Follow-up generation
- [x] Apply queue export
- [x] GitHub project management

---

## 🔄 Next

- [ ] Multi-source job aggregation
- [ ] Advanced resume parsing
- [ ] Semantic resume ↔ JD matching
- [ ] Job deduplication
- [ ] Freshness detection
- [ ] Sub-24-hour job prioritization
- [ ] Company career-page discovery
- [ ] Better location understanding
- [ ] Experience-level detection
- [ ] Salary extraction
- [ ] Job quality scoring
- [ ] Persistent application database
- [ ] Advanced search filters

---

## 🚀 Future

- [ ] AI agent orchestration
- [ ] Browser-based application assistant
- [ ] Intelligent form filling
- [ ] Personalized resume selection
- [ ] Personalized cover letters
- [ ] Automated recruiter outreach
- [ ] Follow-up scheduling
- [ ] Interview tracking
- [ ] Application analytics
- [ ] Email integration
- [ ] Calendar integration
- [ ] Autonomous job-search mode

---

# 🔒 Privacy & Security

JobHuntOS may process career-related information such as:

- Resumes
- Skills
- Employment history
- Job preferences
- Application history

Sensitive credentials should always be stored using environment variables.

Never commit:

```text
.env
API Keys
Passwords
Resume Files
Private Application Data
```

The `.gitignore` file is configured to prevent common sensitive files from being committed.

---

# ⚠️ Responsible Automation

JobHuntOS is designed as a job-search and application assistant.

Automation should respect:

- Website Terms of Service
- Job-platform policies
- Anti-bot protections
- Authentication requirements
- API rate limits
- User consent
- Recruiter communication preferences

The system should not bypass security mechanisms, CAPTCHA systems, authentication controls, or other platform restrictions.

Where automated application functionality is used, it should operate only where permitted.

---

# 🎯 Design Philosophy

JobHuntOS follows one principle:

> **The candidate should spend their time making decisions, not performing repetitive searches.**

The system should handle the repetitive work:

```text
Searching
Filtering
Reading
Comparing
Ranking
Drafting
Tracking
```

while the candidate remains in control of:

```text
Career decisions
Application approval
Communication
Interviews
Negotiation
Career choices
```

---

# 🌟 Why JobHuntOS?

Most job-search tools focus on:

```text
"Find jobs."
```

JobHuntOS aims to solve the broader workflow:

```text
                 DISCOVER
                    ↓
                 ANALYZE
                    ↓
                  MATCH
                    ↓
                PRIORITIZE
                    ↓
                  APPLY
                    ↓
                OUTREACH
                    ↓
                FOLLOW-UP
                    ↓
                 TRACK
                    ↓
               INTERVIEW
                    ↓
                  OFFER
```

The long-term vision is not another job board.

It is:

# **A Personal AI Career Operator.**

---

# 👨‍💻 Author

## Harsh Roy

**B.Tech — Information Technology**

Focused on:

- Artificial Intelligence
- Agentic AI
- Data Science
- Data Engineering
- Software Engineering
- Intelligent Automation

---

# 🤝 Contributing

Contributions, suggestions, issues, and improvements are welcome.

If you have an idea that can make JobHuntOS better, feel free to open an issue or submit a pull request.

If you find the project useful, consider giving it a ⭐.

---

# ⭐ Support

If you find JobHuntOS interesting:

```text
⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest features
🤝 Contribute
```

---

# 📜 License

License information will be added as the project matures.

---

## 🚀 JobHuntOS

```text
Your Resume
     +
Your Goal
     ↓
JobHuntOS
     ↓
Discover → Match → Prioritize → Apply → Connect → Track
     ↓
Your Next Opportunity
```

> **Don't just apply to more jobs. Apply smarter.**
