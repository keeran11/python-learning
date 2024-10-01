'''when a funcitn calls itself, then that functin is called as recursive function and process
is called as recursion'''

# def demo():
#     print('hello')

# demo()

'''Basic Recurion:-
1.Direct Recurison: when a funciton call itself
2.indirect Recursion

'''
#direct recurison
#Write a python program for printing n to 1 sequence

# n = int(input("Enter the value of n:")) #10 9 8 7 6 5 4 3 2 1
# #recursion ko problem solve garda stoping position thaha huna paarxa if not then if will go the infinite

# def natural(n):
#     if n ==0:   #stoping condition
#         return 
#     print(n)
#     return(natural(n -1))
# natural(n)

#indirect Recursion:
'''a function calls another function which then calls the first function again'''

# def num(n):
#     if n<=0:
#         return None
#     print(n, end= " ")
#     num1(n-1)

# def num1(n):
#     print(n , end=" ")
#     num(n-1)
# num(10) #here condition check hunxa ani ball print hunxa output:10 9 8 7 6 5 4 3 2 1 
# num1(10)#here n1 ma 0 print hunxa kina vane yo ma condition check navai direct print hunxa output:10 9 8 7 6 5 4 3 2 1 0


#write a python program for factorial of a number using recurison
#95% recursion ma same condition follow garinxa

# def fact():
#     if condition:
#         return
#     return [recursive call]
# fact()

# def fact(n):
#     if n ==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))


#print your name 10 times without using loop and manually

