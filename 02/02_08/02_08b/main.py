my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))


student_grade = [("Ahmad", 85), ("Zahid", 82), ("Saad", 91), ("Hamza", 89)]

print(sorted(student_grade))
print(sorted(student_grade, key=lambda x: x[1], reverse=True))
print(sorted(student_grade, key=lambda x: x[1], reverse=False))
