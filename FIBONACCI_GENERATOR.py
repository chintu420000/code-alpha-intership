def Fibonacci_Sequence(num):
    a=0
    b=1
    if user<0:
       print("invalid number")
    else:
        if num == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i  in range(3,num+1):
                c = a + b
                a = b
                b=c
                print(c)
print("plz enter postive number only")
user=int(input("enter you want to Fibonacci Sequence:"))
Fibonacci_Sequence(user)
