#Basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)


#Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year")


#Calculate using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")



# Step1 Welcome Message
# Step2 Request customer to place order
# Step3 Tells ustomer to confirm order the proceed

# Greetings
greeting = "Hello! Welcome to Opnex Eat and Smile"
print(greeting)

# Order
order = input("Please kindly place your order: ")
print("Your order:", order)


# Confirm
confirm = input("Please confirm your order with proceed: ")
print("Thanks for your patronage")



option = input("for recharge card, type 1:\n for data, type 2 ")
print("enter", option )

price = int(input("Enter amount\n #100\n #200\n #300\n #400\n #500\n #1000: "))
print(f"Are you sure you want to racharge a sum of {price} recharge card?")

Confirmation = input("Type yes to proceed: ")
print(f"You have successfuly a {price} racharge card")