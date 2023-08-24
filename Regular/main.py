import mysql.connector
import datetime


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="database@9440672439",
    database="library"
)

def search(reg):
    mycursor = mydb.cursor()
    sql="select * from student_info"
    val=(reg)
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    k=0
    print(type(myresult))
    for i in myresult:
        print(type(i))
        k=k+1
        #print(i)
        if i[1]==reg:
            password = input("Enter password : ")
            if i[1]==reg and password==i[3]:
                print("Reg_no :",i[1],"Name :",i[2])
                return 2
            elif i[1]==reg and password!=i[3]:
                print("Wrong password")
                return 1
        if k==len(myresult):
            print("No account found.Please create")
            return 0


def create(reg):
    mycursor = mydb.cursor()
    sql="insert into student_info(reg_no,name,password) values(%s,%s,%s)"
    name=input("Enter your name : ")
    password=input("Enter your password : ")
    values=(reg,name,password)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Created")
    return 0


def firstentry(reg):
    mycursor = mydb.cursor()
    sql = "insert into digital(Reg_no, intime, outtime) values(%s,%s,%s)"
    x = datetime.datetime.now()
    values = (reg, x, x)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Logged in")


def check(reg):
    mycursor = mydb.cursor()
    sql = "select * from digital"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    #print(myresult)
    if len(myresult)==0:
        return 0
    k=0
    for i in myresult:
        k=k+1
        #print(len(myresult),k,myresult[-1][1])
        if i[1] == reg and i[2] == i[3]:
            return 1
        elif k==len(myresult):
            return 0


def leave(reg):
    mycursor = mydb.cursor()
    t="select * from digital"
    mycursor.execute(t)
    myalldata=mycursor.fetchall()
    for j in myalldata:
        #print(j[2],j[3])
        if j[2] == j[3]:
            y = datetime.datetime.now()
            sql = "update digital set outtime=%s where reg_no=%s and intime=outtime"
            val = (y, reg)
            mycursor.execute(sql,val)
            mydb.commit()
            break
    sql = "select * from digital"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    myresult.sort(reverse=True)
    for i in myresult:
        if i[1]==reg:
            print("In time :",i[2], "Out time :",i[3])
            print("Logged out")
            break



for i in range(50):
    reg = input("Enter your Reg no : ")
    y=search(reg)
    if y==0:
        create(reg)
        y=2
    x=check(reg)
    if x==0 and y==2:
        firstentry(reg)
    elif x==1 and y==2:
        leave(reg)
    print("Thank you")
