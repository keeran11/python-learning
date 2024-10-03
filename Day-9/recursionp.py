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

# count = 1

# def printer(name):
#     global count
#     if count <=10:
#         print(name)
#         count +=1
#         printer(name)
# printer("kiran")
    


#factorical using recursion
#base case
# recursion case

# n = int(input('Enter number'))

# def fact(n):

#     if n ==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# if n<0:
#     print('factorial of negatiove cannot be calculated')
# elif n==0:
#     print(f'factorial of 0 is 1')

# else:
#     result = fact(n)

# print(result)

'''
2 raised to 5:- 2*2*2*2*2
2*2(4)
2*2*2(3)
2*2*2*2(2)
2*2*2*2*2(1)

'''

# def power(n,p):
#     if p==0:
#         return 1
#     return n*power(n,p-1)

# print(power(2,5))


#checking  the prime number 


# def prime(n,i):
#     if i==1:
#         return 1
#     if n%i ==0:
#         return 0
#     return prime(n,i-1)

# n = int(input("Enter the number:"))
# ind = prime(n, n-1)

# if ind ==1:
#     print('prime number')

# if ind == 0:
#     print("Not a prime number")

#python program for counting number of digits in given number 

# def count_of(n):
#     if n<10:
#         return 1
#     return 1+count_of(n//10)

# n=int(input("Enter the number: "))
# print(count_of(n))




#python program for fibonacci series using Recurison


def fibo(n):
    if n ==1:
        return 0
    if n ==2:
        return 1
    return (fibo(n-2)+fibo(n-1))
    
    

n= int(input("Enter number of terms:"))
for i in range(1,n+1):
    print(fibo(i))

result = 0
for j in fibo(i):
    result +=j
    print(result)

