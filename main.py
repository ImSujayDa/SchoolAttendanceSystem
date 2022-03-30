import datetime

import mysql.connector


def login():
    print("To Login")
    teacher = input("\tPlease enter Your Teacher ID : ")
    password = input("\tPlease enter Your Password : ")
    cls = input("\tEnter class (from 1 to 12) : ")
    if int(cls) > 12:
        print("Wrong input")
        login()
    else:
        for row in myresult:
            tid = row[0]
            tname = row[1]
            tpass = row[2]
            if tid == teacher:
                if tpass == password:
                    print(f"Dear {tname}, Login Successful")
                    welcome(cls)
                    break
                else:
                    print("Wrong Password")
                    login()
                    break

    print("Invalid Credentials")
    login()


def logout(cls):
    print("Logging Out")
    login()


def attendance(cls):
    sid = input("Please enter student's Roll No.:\n")
    day = datetime.datetime.now().date()
    pk = str(day) + str(sid)
    mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
    mycursor = mydb.cursor()
    if cls == str("1"):
        sql1 = f"select * from stud_class1 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class1 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("2"):
        sql1 = f"select * from stud_class2 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class2 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("3"):
        sql1 = f"select * from stud_class3 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class3 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("4"):
        sql1 = f"select * from stud_class4 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class4 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("5"):
        sql1 = f"select * from stud_class5 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class5 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("6"):
        sql1 = f"select * from stud_class6 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class6 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

            print("Wrong input!")
            welcome(cls)

    elif cls == str("7"):
        sql1 = f"select * from stud_class7 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class7 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("8"):
        sql1 = f"select * from stud_class8 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class8 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("9"):
        sql1 = f"select * from stud_class9 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class9 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("10"):
        sql1 = f"select * from stud_class10 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class10 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("11"):
        sql1 = f"select * from stud_class11 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class11 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)

    elif cls == str("12"):
        sql1 = f"select * from stud_class12 where sid = {sid}"
        i = 0
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            i = row[0]
            name = row[1]
            if str(i) == str(sid):
                sql = "INSERT INTO att_class12 (pkey, date, sid, sname, ststus) VALUES (%s, %s, %s, %s, %s)"
                val = (pk, day, sid, name, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Attendance of {name} is stored")
                welcome(cls)

        print("Wrong input!")
        welcome(cls)


def today(cls):
    print(f"Today's attendance of class {cls} :\nDate\t\t\tRoll No.\t\tName")
    print("--------------------------------------------")
    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")
    mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
    mycursor = mydb.cursor()
    if cls == str("1"):
        sql1 = f"select * from att_class1 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("2"):
        sql1 = f"select date, sid, sname from att_class2 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("3"):
        sql1 = f"select date, sid, sname from att_class3 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("4"):
        sql1 = f"select date, sid, sname from att_class4 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("5"):
        sql1 = f"select date, sid, sname from att_class5 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("6"):
        sql1 = f"select date, sid, sname from att_class6 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("7"):
        sql1 = f"select date, sid, sname from att_class7 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("8"):
        sql1 = f"select date, sid, sname from att_class8 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("9"):
        sql1 = f"select date, sid, sname from att_class9 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("10"):
        sql1 = f"select date, sid, sname from att_class10 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("11"):
        sql1 = f"select date, sid, sname from att_class11 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("12"):
        sql1 = f"select date, sid, sname from att_class12 where date = '{d1}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[1]
            r2 = row[2]
            r3 = row[3]
            print(f"{r1}\t\t{r2}\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)


def tot(cls):
    sid = input("Enter Roll No. of student :")
    print(f"Total attendance of Roll No. {sid} of class {cls} :\nDate\t\t\tRoll No.\t\tName")
    print("--------------------------------------------")
    mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
    mycursor = mydb.cursor()
    if cls == str("1"):
        sql1 = f"select date, sid, sname from att_class1 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("2"):
        sql1 = f"select date, sid, sname from att_class2 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("3"):
        sql1 = f"select date, sid, sname from att_class3 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("4"):
        sql1 = f"select date, sid, sname from att_class4 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("5"):
        sql1 = f"select date, sid, sname from att_class5 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("6"):
        sql1 = f"select date, sid, sname from att_class6 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("7"):
        sql1 = f"select date, sid, sname from att_class7 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("8"):
        sql1 = f"select date, sid, sname from att_class8 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("9"):
        sql1 = f"select date, sid, sname from att_class9 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("10"):
        sql1 = f"select date, sid, sname from att_class10 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("11"):
        sql1 = f"select date, sid, sname from att_class11 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("12"):
        sql1 = f"select date, sid, sname from att_class12 where sid = {sid}"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            r3 = row[2]
            print(f"{r1}\t\t{r2}\t\t\t\t{r3}")

        print("\n\n")
        mydb.commit()
        welcome(cls)


def reg(cls):
    sid = input("Please enter student's Roll No.:\n")
    sname = input("Please enter student's name :\n")
    mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
    mycursor = mydb.cursor()
    if cls == str("1"):
        sql = "INSERT INTO stud_class1 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("2"):
        sql = "INSERT INTO stud_class2 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("3"):
        sql = "INSERT INTO stud_class3 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("4"):
        sql = "INSERT INTO stud_class4 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("5"):
        sql = "INSERT INTO stud_class5 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("6"):
        sql = "INSERT INTO stud_class6 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("7"):
        sql = "INSERT INTO stud_class7 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("8"):
        sql = "INSERT INTO stud_class8 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("9"):
        sql = "INSERT INTO stud_class9 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("10"):
        sql = "INSERT INTO stud_class10 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("11"):
        sql = "INSERT INTO stud_class11 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)

    elif cls == str("12"):
        sql = "INSERT INTO stud_class12 (sid, sname) VALUES (%s, %s)"
        val = (sid, sname)
        mycursor.execute(sql, val)
        mydb.commit()
        welcome(cls)


def show(cls):
    mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
    mycursor = mydb.cursor()
    if cls == str("1"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class1"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("2"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class2"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("3"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class3"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("4"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class4"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("5"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class5"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("6"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class6"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("7"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class7"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("8"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class8"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("9"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class9"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("10"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class10"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("11"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class11"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)

    elif cls == str("12"):
        print(f"Students of Class {cls} :\nRoll No.\t\t\tName")
        print("-----------------------------------------")
        sql1 = "select sid, sname from Stud_class12"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()
        for row in myresult1:
            r1 = row[0]
            r2 = row[1]
            print(f"{r1}\t\t\t{r2}")

        print("\n\n")
        mydb.commit()
        welcome(cls)


def welcome(cls):
    print("Please Choose any option\n\t1. Student Attendance\n\t2. Check Attendance of Today\n\t3. "
          "Check any student's total attendance\n\t4. Student Registration\n\t5. Show Student Details\n\t0. Exit\n")
    choice = input()
    if choice == str("0"):
        logout(cls)
    elif choice == str("1"):
        attendance(cls)
    elif choice == str("2"):
        today(cls)
    elif choice == str("3"):
        tot(cls)
    elif choice == str("4"):
        reg(cls)
    elif choice == str("5"):
        show(cls)

    else:
        print("Invalid Choice !\n***try again***")
        welcome(cls)


mydb = mysql.connector.connect(host='localhost', user='root', password='123456', database='school')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM teacher")
myresult = mycursor.fetchall()
mydb.commit()
login()
