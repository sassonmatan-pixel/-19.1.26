a: float = float(input("הכנס צלע 1"))
b: float = float(input("הכנס צלע 2"))
c: float = float(input("הכנס צלע 3"))
if a == b and a == c:
    print("זה משולש שווה צלעות")
else:
    if a == b or b == c or a == c:
        print("זה משולש שווה שוקיים")
    else:
        print("זה משולש שונה צלעות")