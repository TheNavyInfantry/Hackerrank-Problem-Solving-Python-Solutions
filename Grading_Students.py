def gradingStudents(grades):
    for each in grades:
        if each >= 38:
            if each % 5 == 2:
                each += 3
            elif each % 5 == 3:
                each += 2
            elif each % 5 == 4:
                each += 1
        print(each)

gradingStudents([73,67,38,33])