# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"'{task}' is a {priority} priority task."

# Process the task based on priority
match priority:
    case "high":
        reminder += " It requires immediate attention today!"
    case "medium":
        reminder += " It should be completed soon."
    case "low":
        reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
elif time_bound == "no":
    reminder += " Note: It's not time-sensitive."

# Print the customized reminder
print(reminder)

