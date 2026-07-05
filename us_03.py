def prompt_course_count(available_courses):
    """Prompt the student for a positive integer number of courses to select."""
    while True:
        try:
            count = int(input("Enter the number of courses you wish to register for: ").strip())
        except ValueError:
            print("Error: please enter a positive integer.")
            continue

        if count <= 0:
            print("Error: please enter a positive integer.")
            continue

        if count > len(available_courses):
            print("Error: you cannot request more courses than are available.")
            continue

        return count
