def calculate_mean(grades):
    mean_grade = sum(final_grades)/len(final_grades)
    if mean_grade >= 90:
        return "A"
    elif mean_grade >= 80:
        return "B"
    elif mean_grade >= 70:
        return "C"
    elif mean_grade >= 60:
        return "D"
    elif mean_grade >= 50:
        return "E"
    else:
        return "F"



# Collecting final grades from users
final_grades =[]
for _ in range(3):
    grade = int(input("Enter final grade:"))
    final_grades.append(grade)

# Calculating mean grade
mean_grade = calculate_mean(final_grades)
# Printing the mean grade
print("Mean grade:", mean_grade)
print("Final Grades:", final_grades)
print("Mean Grade:", mean_grade)


