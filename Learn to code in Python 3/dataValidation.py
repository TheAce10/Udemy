data_valid= False

while data_valid == False:
    grade= input("Type the grade  of the test")
    try:
        grade= float(grade)
    except:
        print("invalid input. Only number are accepted. Decimals should ebe seperated with a dot")
        continue
    if grade <0 or  grade >10:
        print("Grade")
        continue
    else:
        data_valid= True

data_valid= False

while data_valid == False:
    grade1= float(input("Type the grade  of the test"))
    if grade1 <0 or  grade1 >10:
        print("Grade1")
        continue
    else:
        data_valid= True


while data_valid == False:
    totalclasses= int(input("Type the grade  of the test"))
    if totalclasses <=0:
        print("The number of classes cant be less than 0")
        continue
    else:
        data_valid= True

while data_valid == False:
    absences= float(input("Type the grade  of the test"))
    if absences <0 or  absences > totalclasses:
        print("Thenumber of absence cant be less than zero or number of classes")
        continue
    else:
        data_valid= True

        