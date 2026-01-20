#start
b = None
a: float = float(input("תקלוט מספר"))
while a != b:
    b = a
    a: float = float(input("הכנס מספר נוסף"))
else:
    print("נמצא שני מספרים זהים ברצף")