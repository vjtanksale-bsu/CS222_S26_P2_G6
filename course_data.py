def read_course_data(filename):
    courses = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            courses.append({
                "course": parts[0],
                "section": parts[1],
                "days": parts[2],
                "start": int(parts[3]),
                "end": int(parts[4])
            })

    return courses


def get_course_numbers(courses):
    numbers = []

    for course in courses:
        if course["course"] not in numbers:
            numbers.append(course["course"])

    return numbers


def display_course_numbers(courses):
    print("Available Courses:")

    for course in get_course_numbers(courses):
        print(course)
