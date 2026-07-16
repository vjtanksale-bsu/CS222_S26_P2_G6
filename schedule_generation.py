from conflict_detection import has_conflict


def order_courses_by_section_count(selected_courses, all_sections):
    def section_count(course):
        return sum(1 for s in all_sections if s["course"] == course)
    return sorted(selected_courses, key=section_count)


def generate_schedule(selected_courses, all_sections):
    course_sections = {
        course: [s for s in all_sections if s["course"] == course]
        for course in selected_courses
    }

    ordered_courses = order_courses_by_section_count(selected_courses, all_sections)

    def backtrack(index, current_schedule):
        if index == len(ordered_courses):
            return current_schedule

        current_course = ordered_courses[index]
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