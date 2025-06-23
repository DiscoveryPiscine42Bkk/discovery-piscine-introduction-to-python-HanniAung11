
user_input = input("Give me a number: ")

try:
    number = float(user_input)

    
    if number == int(number):
        print(int(number))
    else:
       
        print(int(number) + 1)

except ValueError:
    print("Invalid input! Please enter a valid number.")
