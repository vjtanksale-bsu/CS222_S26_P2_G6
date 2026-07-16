from collections import defaultdict
from conflict_detection import has_conflict


def generate_schedule(selected_courses, all_sections):
    course_sections = defaultdict(list)

    for section in all_sections:
        course_sections[section["course"]].append(section)

    def backtrack(index, current_schedule):
        if index == len(selected_courses):
            return current_schedule

        current_course = selected_courses[index]
        for section in course_sections.get(current_course, []):
            conflict_found = False
            for existing in current_schedule:
                if has_conflict(section, existing):
                    conflict_found = True
                    break

            if not conflict_found:
                result = backtrack(index + 1, current_schedule + [section])
                if result is not None:
                    return result
        return None

    return backtrack(0, [])
