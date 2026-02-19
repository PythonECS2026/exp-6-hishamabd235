# AIM: WAP to find students appearing for entrance exams
# Coder: Hisham Shariq Abdullah
# Date: 19/02/26

print("--- Entrance Exam Students ---")

cet_students = {"Bob", "Frank", "Charlie", "Alice"}
jee_students = {"Bob", "Heidi", "Frank", "Eve"}
neet_students = {"Bob", "Charlie", "Karl", "Liam"}

print("List of Students:")
print("CET Students:", cet_students)
print("JEE Students:", jee_students)
print("NEET Students:", neet_students)

# All students (Union)
all_students = cet_students.union(jee_students, neet_students)
print("All Students:", all_students)

# Students in all exams (Intersection)
all_exams = cet_students.intersection(jee_students, neet_students)
print("All Exams:", all_exams)

# JEE but not NEET (Difference)
jee_not_neet = jee_students.difference(neet_students)
print("JEE but not for NEET:", jee_not_neet)

# CET and NEET but not JEE
cet_neet_not_jee = cet_students.intersection(neet_students).difference(jee_students)
print("CET and NEET but not for JEE:", cet_neet_not_jee)

