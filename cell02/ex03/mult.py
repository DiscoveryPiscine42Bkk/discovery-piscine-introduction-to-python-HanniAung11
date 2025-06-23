n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print(n1 , " * ", n2 ," = ", n1*n2)

if(n1*n2==0):
    print("The result is negative and positive.")
elif(n1*n2<0):
    print("The result is negative")
else:
    print("The result is positive.")
        