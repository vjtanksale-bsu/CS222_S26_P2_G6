def collect_course_selections(available_courses, required_count):
    """Collect a list of unique, valid course selections.

    The function prompts until the required number of valid courses has been
    collected, ignoring invalid entries and duplicates.
    """
    selections = []

    while len(selections) < required_count:
        course = input("Enter a course code: ").strip().upper()

        if not course:
            print("Error: course code cannot be empty.")
            continue

        if course not in available_courses:
            print("Error: course is not available.")
            continue

        if course in selections:
            print("Error: course already selected.")
            continue

        selections.append(course)

    return selections
