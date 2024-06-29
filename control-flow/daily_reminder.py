task = input("Enter your task: ")
priority = input("classify the priority of it (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

reminder = ""
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

if time == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder:", reminder)

