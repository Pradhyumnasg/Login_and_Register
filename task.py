import re
def register():
    db = open("data.txt", "r")
    username = input("create username:")
    mail=input("mailid:")
    password = input("create password:")
    password1 = input("confirm password:")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))

    if password != password1:
        print("password dont match,restart")
        register()
    else:
        if len(password)<=5:
            print("password is too weak")
            register()

        elif username in d:
             print("username exists")
             register()

        else:
            db = open("data.txt", "a")
            db.write(username + "," + password + "\n")
            print("success!")



def access():
    db=open("data.txt", "r")
    username = input("enter username:")
    password = input("enter password:")

    if not len(username or password)<=1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("login successful")
                        print("Hi,",username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorrecct password of username")
            else:
                print("username or password doesn't exist")
        except:
            print("username or password doesn't exist")
    else:
        print("please enter a value")
def home(option=None):
    option=input("login | signup:")
    if option=="login":
        access()
    elif option=="signup":
        register()
    else:
        print("please enter a option")
home()