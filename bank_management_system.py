import sqlite3

conn = sqlite3.connect('Database/UserData.db')
cursor = conn.cursor()
q = '''CREATE TABLE IF NOT EXISTS User_Bank_Detail(
    Name TEXT (20) NOT NULL,
    Username TEXT (20) NOT NULL,
    Password TEXT (10) NOT NULL,
    Mobile number (10) NOT NULL,
    Adhar_no number (12) NOT NULL,
    Bank TEXT (20) NOT NULL,
    Account_no number (10) NOT NULL,
    Total_balance number (10) NOT NULL,
    Address TEXT (20) NOT NULL,
    Date_of_birth number (20) NOT NULL,
    Gender TEXT (10) NOT NULL


   )'''

cursor.execute(q)
print("table created")


def login():
    un = input("enter your username")
    pwd = input("enter your password")
    q = '''select * from User_Bank_Detail where Username=? and Password=?'''
    userdata = cursor.execute(q,(un,pwd)).fetchone()
    if userdata:
        print("welcome", userdata[0])
        print(
            "1. all detail 2.update profile 3.change password 4.deposit amount 5.withdraw amount 6.check current balance 7.delete account")
        n = int(input("enter the choice"))
        if (n == 1):
            print("your detail")
            print("your name", userdata[0])
            print("your username", userdata[1])
            print("your password", userdata[2])
            print("your mobile_no", userdata[3])
            print("your adhar_no", userdata[4])
            print("your bank name", userdata[5])
            print("your account_no", userdata[6])
            print("your total_balance", userdata[7])
            print("your address", userdata[8])
            print("your date_of_birth", userdata[9])
            print("your gender", userdata[10])
        elif (n == 2):
            print("1.name 2.mobile_no 3.adhar_no 4.bank_name 5.address 6.date_of_birth 7.gender")
            n = int(input("enter your choice"))
            if n == 1:
                newname = input('enter your newname')
                q = '''update User_Bank_Detail set Name=? where Name=?'''
                cursor.execute(q, (newname, userdata[0]))
                conn.commit()
                print("name update")
            elif n == 2:
                mob = input('enter your new mobile_no')
                q = '''update User_Bank_Detail set Mobile_no=? where Mobile_no=?'''
                cursor.execute(q, (mob, userdata[0]))
                conn.commit()
                print("mobile_no  updated")
            elif n == 3:
                adrn = int(input("enter your adhar no."))
                q = '''update User_Bank_Detail set adhar_no=? where adhar_no=?'''
                cursor.execute(q, (adrn, userdata[4]))
                conn.commit()
                print("adhar no updated")
            elif n == 4:
                bn = int(input("enter your bank name"))
                q = '''update User_Bank_Detail set Bank_name=? where Bank_name=?'''
                cursor.execute(q, (bn, userdata[5]))
                conn.commit()
                print("bank name updated")
            elif n == 5:
                add = int(input("enter your address"))
                q = '''update User_Bank_Detail set Address=? where Address=?'''
                cursor.execute(q, (add, userdata[8]))
                conn.commit()
                print("address updated")
            elif n == 6:
                dob = int(input("enter your date of birth"))
                q = '''update User_Bank_Detail set Date_of_birth=? where Date_of_birth=?'''
                cursor.execute(q, (dob, userdata[9]))
                conn.commit()
                print("date of birth updated")
            elif n == 7:
                g = int(input("enter your gender"))
                q = '''update User_Bank_Detail set Gender=? where Gender=?'''
                cursor.execute(q, (g, userdata[10]))
                conn.commit()
                print("gender updated")
            else:
                print("wrong choice")
        elif (n == 3):
            pwd = int(input("enter new password"))
            q = '''update User_Bank_Detail set Password=? where Password=?'''
            cursor.execute(q, (pwd, userdata[2]))
            conn.commit()
            print("password has changed")
        elif (n == 4):
            da = int(input("enter the amount you want to deposit :"))
            tb = da + userdata[7]
            q = '''update User_Bank_Detail set Bank_balance=? where Bank_balance=?'''
            cursor.execute(q, (tb, userdata[7]))
            conn.commit()
            print("your money is deposit and current balance is:", userdata[7])
        elif (n == 5):
            wa = int(input("enter the money you want to withdraw"))
            while (True):

                if (userdata[7] < wa):
                    print("you have inefficient amount try another amount ")
                    wa = int(input("enter the money you want to withdraw"))
                else:
                    tb = userdata[7] - wa
                    break;
            q = '''update User_Bank_Detail set Bank_balance=? where Bank_balance=?'''
            cursor.execute(q, (wa, userdata[7]))
            conn.commit()
            print("you have withdaw the money now your balce is:", userdata[7])
        elif (n == 6):
            print("your current balance is:", userdata[7])
        elif (n == 7):
            q = '''delete from  User_Bank_Detail where Username=? '''
            cursor.execute(q, (userdata[1]))
            conn.commit()
            print("user is deleted")
        else:
            print("plzz enter valid choice")


def alluser():
    q = ''' select username from User_bank_detail'''
    data = cursor.execute(q).fetchall()
    return data


def insert(name, username, password, mobile, adhar, bank, account, total, address, date, gender):
    insert_q = '''insert into User values(?,?,?,?,?,?,?,?,?,?,?)
    '''
    cursor.execute(insert_q, (name, username, password, mobile, adhar, bank, account, total, address, date, gender))
    conn.commit()
    print("your data is added for login enter username and password");
    login()


def signup():
    username = []
    n = input("enter your name")
    data = alluser()
    for i in data:
        username.append(i[0])
    while (True):
        un = input("enter your username")
        if un in username:
            print("this username is already exits try other")
        else:
            break
    p = (input("enter your password"))
    m = int(input("enter your mobile number"))
    an = int(input("enter your adhar number"))
    bn = input("enter your bank name")
    ban = int(input("enter your bank account no of 10 digit"))
    while True:
        tb = int(input("deposit min 500 for opening an account"))
        if (tb < 500):
            print("plzz deposit min 500rs for opening a new account")
        else:
            break

    a = input("enter your address")
    dob = int(input("enter your date of birth"))
    g = input("enter your gender")

    insert_q = ''' insert into User_bank_detail values(?,?,?,?,?,?,?,?,?,?,?)'''
    cursor.execute(insert_q, (n, un, p, m, an, bn, ban, tb, a, dob, g))
    conn.commit()
    print("your data is added ")
    login()


print(" 1. for login into account 2. for open a new bank account")
option = int(input("enter the choice"))
if option == 1:
    login()
elif option == 2:
    signup()
else:
    print("invalid choice")

