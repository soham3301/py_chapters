student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def grade_checker(score_dict):
    std_grades = {}
    grade = ""
    for key, value in score_dict.items():
        if value > 90:
            grade = "Outstanding"
            std_grades.update({key: grade})
        elif value > 80:
            grade = "Exceeds Expectations"
            std_grades.update({key: grade})
        elif value > 70:
            grade = "Acceptable"
            std_grades.update({key: grade})
        else:
            grade = "Fail"
            std_grades.update({key: grade})
    return std_grades

def main():
    student_grades = grade_checker(student_scores)
    print(student_grades)

main()