from datetime import datetime, timedelta

print("===================================")
print("        LEARNOVA - AI STUDY PLANNER")
print("===================================\n")

subjects = []

# Take number of subjects
n = int(input("Enter number of subjects: "))

# Input subject details
for i in range(n):
    print(f"\nEnter details for Subject {i+1}")
    name = input("Subject Name: ")
    priority = int(input("Priority (1 = High, 2 = Medium, 3 = Low): "))
    duration = int(input("Study Duration (in minutes): "))

    subjects.append({
        "name": name,
        "priority": priority,
        "duration": duration
    })

# Sort subjects by priority (AI logic simulation)
subjects.sort(key=lambda x: x["priority"])

# Start time input
start_time_input = input("\nEnter start time (HH:MM format, 24-hour): ")
break_time = int(input("Enter break time between subjects (minutes): "))

# Convert start time
current_time = datetime.strptime(start_time_input, "%H:%M")

print("\n========== YOUR AI STUDY SCHEDULE ==========\n")

# Generate schedule
for subject in subjects:
    start = current_time
    end = start + timedelta(minutes=subject["duration"])

    print(f"Subject: {subject['name']}")
    print(f"Time: {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
    print("----------------------------------")

    # Add break time
    current_time = end + timedelta(minutes=break_time)

print("\nStudy Plan Generated Successfully by Learnova AI 🚀")