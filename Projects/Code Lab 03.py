def letter_grade(func_score):
    grade = ' '
    if func_score >= 90:
        grade = 'A'
    elif func_score >= 80:
        grade = 'B'
    elif func_score >= 70:
        grade = 'C'
    elif func_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def calc_avg_grade(func_grades):
    sum = 0
    x = 0
    while x < 5:
        sum += func_grades[x]
        x += 1
    avg = sum/5.00
    return avg


def main():
    grades = []
    name = input("Enter student name : ")
    for x in range(5):
        score = input("Enter points for the grade : ")
        grades.append(int(score))
        lgrade = letter_grade(int(score))
        print('Points : ' + score, 'Grade : ' + lgrade)
    avg_grade = calc_avg_grade(grades)
    print(name + ' : Average grade - ' + str(avg_grade))


if __name__ == "__main__":
    main()
