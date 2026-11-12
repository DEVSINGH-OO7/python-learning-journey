email=input("enter email:")
if "@" in email:
    password=input("enter pass;")
    if email=='devsingh@gmail.com' and password=='1234':
        print("welcome")
    elif email=='devsingh@gmail.com' and password !='1234':
        print("pass not correct")
        password=input("reenter pass:")
        if password=='1234':
            print("welcome")
        else:
            print("pass incorrect again")
    else:
        print("incorrect credentials")
else:
    print("inproper mail")