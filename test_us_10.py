import time

from schedule_generation import generate_schedule


def make_dataset(num_courses=10, sections_per_course=10):
    selected = [f"C{i}" for i in range(num_courses)]
    sections = []
    for i, c in enumerate(selected):
        # assign a unique time slot per course to ensure a valid schedule exists
        start = i * 1000
        end = start + 30
        for j in range(sections_per_course):
            sections.append({
                "course": c,
                "days": "M",
                "start": start,
                "end": end,
                "id": f"{c}-S{j}",
            })
    return selected, sections


def test_us_10_performance():
    selected, sections = make_dataset(10, 10)
    t0 = time.perf_counter()
    schedule = generate_schedule(selected, sections)
    elapsed = time.perf_counter() - t0
    print(f"US-10 baseline: generate_schedule for {len(selected)} courses x 10 sections = {elapsed:.6f} seconds")
    assert schedule is not None
    assert len(schedule) == len(selected)
