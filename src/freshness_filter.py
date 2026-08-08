def get_freshness_priority(posted_time):
    posted_time = str(posted_time).lower()

    if "0-1" in posted_time or "1 hour" in posted_time:
        return "Highest", 100

    elif "1-6" in posted_time or "6 hours" in posted_time:
        return "Very High", 80

    elif "6-24" in posted_time or "24" in posted_time or "today" in posted_time:
        return "High", 60

    elif "1-3" in posted_time or "3 days" in posted_time:
        return "Medium", 40

    else:
        return "Low", 20