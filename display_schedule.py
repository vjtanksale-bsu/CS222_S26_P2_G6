def display_schedule(schedule):
    if not schedule:
        return
    
    print("\n--- Final Course Schedule ---")
    for section in schedule:
        print(f"Course: {section['course']} | Section: {section['section']} | Days: {section['days']} | Start Time: {section['start']} | End Time: {section['end']}")
    print("-----------------------------\n")