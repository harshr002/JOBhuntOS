from urllib.parse import quote


JOB_SOURCES = {
    "Google": "https://www.google.com/search?q={query}",
    "LinkedIn": "https://www.linkedin.com/jobs/search/?keywords={query}",
    "Naukri": "https://www.naukri.com/{query}-jobs",
    "Instahyre": "https://www.instahyre.com/search-jobs/?company_size=0&skills={query}",
    "Cutshort": "https://cutshort.io/jobs/{query}-jobs",
    "Wellfound": "https://wellfound.com/jobs",
    "Greenhouse": "https://www.google.com/search?q=site:greenhouse.io/jobs {query}",
    "Lever": "https://www.google.com/search?q=site:lever.co {query}",
    "Ashby": "https://www.google.com/search?q=site:jobs.ashbyhq.com {query}",
    "Workable": "https://www.google.com/search?q=site:jobs.workable.com {query}",
}


def generate_search_links(user_prompt):
    query = str(user_prompt).strip()

    if not query:
        return []

    encoded_query = quote(query)

    links = []

    for source, url_template in JOB_SOURCES.items():
        links.append({
            "source": source,
            "search_query": query,
            "search_link": url_template.format(query=encoded_query)
        })

    return links