# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation (kia karna cahhte hen 1,2,3 ya 4).")
print("1.Add (jama karna he)")
print("2.Subtract (tafreek karna he)")
print("3.Multiply (zarb karna he)")
print("4.Divide (taksem karna he)")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number (Matlab pehla hindsa darj karen): "))
            num2 = float(input("Enter second number (Matlab doosra hindsa darj karen): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "Barabar he", add(num1, num2),'ke')

        elif choice == '2':
            print(num1, "-", num2, "Barabar he", subtract(num1, num2),'ke')

        elif choice == '3':
            print(num1, "*", num2, "Barabar he", multiply(num1, num2),'ke')

        elif choice == '4':
            print(num1, "/", num2, "Barabar he", divide(num1, num2),'ke')
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("sir jii Invalid Input")
        quit()