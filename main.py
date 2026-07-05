from course_data import read_course_data, get_course_numbers, display_course_numbers
from us_03 import prompt_course_count
from us_04 import collect_course_selections
from schedule_generation import generate_schedule
from display_schedule import display_schedule
from notify_no_schedule import notify_no_schedule


def run(filename):
    courses = read_course_data(filename)
    available_courses = get_course_numbers(courses)
    display_course_numbers(courses)

    count = prompt_course_count(available_courses)
    selected_courses = collect_course_selections(available_courses, count)

    schedule = generate_schedule(selected_courses, courses)

    if schedule is None:
        notify_no_schedule()
    else:
        display_schedule(schedule)


if __name__ == "__main__":
    run("courses.txt")