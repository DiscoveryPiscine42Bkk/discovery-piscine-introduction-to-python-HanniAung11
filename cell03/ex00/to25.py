n=25
num=int(input("Enter a number less than 25:"))
if(num<25):
    for i in range(num,n+1):
        print("Inside the loop,my variable is ",i)
else:print("Error")