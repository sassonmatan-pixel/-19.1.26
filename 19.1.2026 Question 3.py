pepole: int =int(input("כנס מספר אנשים"))
total_room = 0
if pepole % 4 != 0:
    total_room = (pepole//4)+1
    print ("יש חדר אחד עם {} אנשים".format(pepole % 4))
    print("מספר החדרים שיש", total_room)
else:
    print("כל החדרים מלאים ללא מקום")
    print("מספר החדרים שיש",pepole/4)