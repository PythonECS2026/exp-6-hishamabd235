# AIM: WAP to find students appearing for entrance exams
# Coder: Hisham Shariq Abdullah
# Date: 19/02/26

print("--- Entrance Exam Students ---")

cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Eve", "Frank", "Grace", "Heidi"}
neet_students = {"Ivan", "Judy", "Karl", "Liam"}

print("\nList of Students:")
print("CET Students:", cet_students)
print("JEE Students:", jee_students)
print("NEET Students:", neet_students)

# TODO: Find and Print All the Students appearing for any Entrance Exam
all_students = cet_students.union(jee_students, neet_students)
print("All Students:", all_students)

# TODO: Find and Print Students appearing for All Entrance Exams
all_exams = cet_students.intersection(jee_students, neet_students)
print("All Exams:", all_exams)

# TODO: Find and Print Students appearing for JEE but not for NEET
jee_not_neet = jee_students.difference(neet_students)
print("JEE but not for NEET:", jee_not_neet)

# TODO: Find and Print Students appearing for CET and NEET but not for JEE
cet_neet_not_jee = cet_students.intersection(neet_students).difference(jee_students)
print("CET and NEET but not for JEE:", cet_neet_not_jee)
