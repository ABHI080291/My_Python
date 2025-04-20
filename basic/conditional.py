
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter the operation: (option + , - , * , / ) ")

if choice =="+":
    sum_of_num = num1 + num2
    print("addition : ",sum_of_num)

#else if in python = elif
elif choice =="-":
    sub_of_num = num1 - num2
    print("substraction :",sub_of_num)

elif choice =="*":
    mul_of_num = num1 * num2
    print("multiplication: ",mul_of_num)

elif choice =="/":
    div_of_num = num1 / num2
    print("division:", div_of_num)

else:
 print("invalid choice")
