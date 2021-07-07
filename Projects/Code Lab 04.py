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
    func_sum = sum(func_grades)
    avg = func_sum/5.00
    return avg


def main():
    grades = []
    i = 0
    outfile = open('Lab4.txt', 'w')
    while i < 4:
        name = input("Enter student name : ")
        for x in range(5):
            score = input("Enter points for the grade : ")
            grades.append(int(score))
            lgrade = letter_grade(int(score))
            print('Points : ' + score, 'Grade : ' + lgrade)
        avg_grade = calc_avg_grade(grades)
        avg_letter = letter_grade(int(avg_grade))
        print(name + ' : Average grade - ' + str(avg_grade))
        outfile.write(name + ': Average grade: ' + str(avg_grade) + ' Average letter grade: ' + avg_letter + "\n")
        grades.clear()
        i += 1
    outfile.close()
if __name__ == "__main__":
    main()
