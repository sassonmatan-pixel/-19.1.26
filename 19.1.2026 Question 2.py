# start
Dannys_grade: float= float(input("הכנס את הציון של דני"))
while Dannys_grade < 0 or Dannys_grade > 100:
    Dannys_grade: float = float(input("הכנס ציון תקין"))
big_class_grade = None
class_grade: float =float(input("הכנס ציוני כיתה"))
while class_grade >= 0 and class_grade <= 100:
    if big_class_grade is None or big_class_grade < class_grade:
        big_class_grade = class_grade
        class_grade: float = float(input("הכנס ציוני כיתה"))
    else:
        class_grade: float = float(input("הכנס ציוני כיתה"))
else:
    if Dannys_grade > big_class_grade:
        print("ציון של דני הוא הציון הגבוהה ביותר")

    else:
        print("הציון של דני לא הכי גבוהה")