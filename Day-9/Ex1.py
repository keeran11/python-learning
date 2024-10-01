#python program to find the sum of Natural Numbaers
#take input form the user

#nautral : 1 2 3 4 5 6 7 8 9 to infinity

#method1:


# num = int(input("Enter the number upto where you want sum: "))

# sum =0
# for j in range(1,num+1):
#     # print(j)
#     sum +=j
# print(sum)


#method 2

# n = int(input("Enter the the number up which you want sum of the natural number: "))
# def sum_of_natural_number(n):
#     total =0
#     for i in range(1, n+1):
#         total += i
#     return total

# print(sum_of_natural_number(n))


#sum of the natural number is calculated using the formula :sum = n(n+1)/2

# def sum_of_natural_numbers_formula(n):
#     return n*(n+1)//2

# n =3
# print(f"Sum of first {n} natural numbers", sum_of_natural_numbers_formula(n))


#using REcursuion
# you can use a recursive approach where the function calls itself with n-1 until n is 0

def sum_of_natural_number_recursive(n):
    if n ==0:
        return 0
    else:
        return n + sum_of_natural_number_recursive(n -1)
n =3
print(f"Sum of first {n} natural numbers:", sum_of_natural_number_recursive(n))
