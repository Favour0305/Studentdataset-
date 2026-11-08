import random
import pandas as pd

# Set up fake data options
departments = ["Computer Science", "Business Admin", "Mass Communication", "Nursing", "Engineering", "Law"]
levels = ["100", "200", "300", "400"]
first_names = ["Favour", "Chiamaka", "Tunde", "Adaeze", "Ibrahim", "Blessing", "Emmanuel", "Zainab", "Chinedu", "Funke", "David", "Grace", "Olumide", "Ngozi", "Yusuf"]
last_names = ["Okafor", "Eze", "Bakare", "Nwosu", "Musa", "Adeyemi", "Obi", "Bello", "Okonkwo", "Alabi", "Johnson", "Mensah", "Adeleke", "Abdullahi"]

students = []

for i in range(1, 51):  # Change 51 to any number you want, e.g. 101 for 100 students
    dept = random.choice(departments)
    level = random.choice(levels)
    attendance = round(random.uniform(55, 100), 1)  # 55% to 100%
    exam = round(random.uniform(35, 98), 1)  # 35 to 98 marks
    
    students.append({
        "Student ID": f"STU-{1000 + i}",
        "First Name": random.choice(first_names),
        "Last Name": random.choice(last_names),
        "Department": dept,
        "Level": level,
        "Attendance Percentage": attendance,
        "Average Examination": exam
    })

# Create table
df = pd.DataFrame(students)

# Save as CSV
df.to_csv("student_dataset.csv", index=False)

# Show first 10 rows
print(df.head(10))
print("\nTotal students:", len(df))
print("Saved as student_dataset.csv")
