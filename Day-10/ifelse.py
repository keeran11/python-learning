#write a program to find positive and negative number take input form user

# num = int(input("Please Enter the number:"))

# if num >0:
#     print("this is positive number")
# elif num==0:
#     print("this is neither positve nor negative")


# else: 
#     print("Negative number")


#multiple input using the list

# numbers = list(map(float, input("Enter the number separeted by space: ").split()))

# for num in numbers:
#     if num > 0:
#         print(f"{num} is positive ")

#     elif num ==0:
#         print(f"{num} this number is either negative nor positive")
#     else:
#         print(f"{num} this number is negative number")



#using list ocmprehension

# number = list(map(int,input("Enter the number seperated by comma(,)").split(',')))

# positive = [num for num in number if num > 0]
# zeros = [num for num in number if num ==0]
# negative = [num for num in number if num <0]

# print("positive numbers", positive)
# print("negative number", negative)
# print("this is zero", zeros)



#handling multiple input with while loop
# while True:
#     user_input = input("Enter the number(or type 'q' to stop):")

#     if user_input.lower()=='q':
#         print("terminal is closing, have a great programming")
#         break
#     user_input1 =int(user_input)
#     if user_input1 > 0:
#         print('the number is positive')
#     elif user_input1 <0:
#         print('number is negative')
#     else:
#         print('the number is zero')



#input validation (handling non-numeric input)

# while True:
#     user_input = input("Enter the nummber or if you want to quit then pelase press 'q' button")

#     if user_input.lower() =='q':
#         print("now terminal is closing, have a great day")
#         break

   
#     try:
#         num =int(user_input)

#         if num > 0:
#             print('the number is positve')

#         elif num < 0:
#             print("the number is negative")

#         else:
#             print('the number eaither positive nor negative')


#     except ValueError:
#         print("invalid input, Please enter a numeric vaue.")


#Recursive Approach

# def check_number():
#     user_input = input("Enter the number (or tye 'q' tp stop ):- ")

#     if user_input.lower()=="q":
#         print('terminal is closing, good day')

#     try:
#         num = int(user_input)

#         if num > 0:
#             print("the number is positive")
#         elif num <0:
#             print('the number is negative')
#         else:
#             print('the number is zero')


#     except ValueError:
#         print("Invalid input. Please enter the valid number")

#     check_number()

# check_number()

'''What's Happening in Each Call:
The first time you call check_number(), the program asks for input.
If the input is not 'exit', it prints whether the number is positive or negative and then calls check_number() again.
The process continues (recursive calls) until the user types 'exit', at which point the recursion stops.
This is a less common approach compared to using loops, 
but it can be useful for certain kinds of problems where recursion is naturally suited (like tree traversals, backtracking problems, etc.).
'''


