def has_conflict(section1, section2):
    shared_days = set(section1["days"]) & set(section2["days"])
    if not shared_days:
        return False
    return section1["start"] < section2["end"] and section2["start"] < section1["end"]