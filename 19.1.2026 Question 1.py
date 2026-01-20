# start

height = float(input("הכנס גובה למשלוש"))
while height <= 0:
    height = float(input("גובה לא תקין אנא בחר גובה שוב"))
base = float(input("הכנס בסיס למשולש"))
while base <= 0:
    base = float(input("בסיס לא תקין אנא בחר בסיס שוב"))
print("השטח הוא:",height*base/2)

#stop