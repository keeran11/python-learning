#write a function to Reverse a string


#method 1

# def ReverseString(string):
#     print(string [::-1])

# ReverseString("python")

#Second Method

# def ReverseString(string):

#     st =''
#     for i in string:
#         # st = i +st
#         st = st +i
#         print(st)
#     print(st)

# ReverseString("python")
#output:
# p
# yp
# typ
# htyp
# ohtyp
# nohtyp
# nohtyp


#method 3:
#using  reversed() function

# def reverse_string_reverse(s):
#     print(''.join(reversed(s)))
# reverse_string_reverse("hello")

'''Here, the reversed() function returns an iterator, and ''.join() is used to
 convert it back to a string.
'''

#method:4
#using the recursive function 
'''A recursive function is a function that calls itself in order to solve smaller instances of the same problem. It works by breaking the problem down into simpler subproblems until it reaches a base case, which is a condition that stops the recursion. After hitting the base case, the function starts returning values up the call stack, 
combining the results to produce the final output.'''

# def reverse_string_recursive(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string_recursive(s[1:]) + s[0]
    
# # Calling the function
# print(reverse_string_recursive("hello"))


#method:5
#using stac (list as Stack)
'''This method uses a stack (a list) to reverse the string by popping characters from the end.'''

# def reverse_string_stack(s):
#     stack = list(s)
#     print(stack)
#     reversed_str = ''
#     while stack:
#         reversed_str += stack.pop()
#     return reversed_str
# print(reverse_string_stack('hello'))


#using list comprehension

# def reverse_string_list_comprehension(s):
#      print(''.join([s[i] for i in range(len(s)-1, -1,-1)]))
    
# reverse_string_list_comprehension('kiran')
# This approach builds a list of characters by iterating over the string backwards and joins the list into a string.


# l1 = ['item1', 'item2', 'item3']
# join1 = ",".join(l1) #join le saab lai liyera string ma change  gardido raixa
# #join method chai string ma matra kaam haarna number ma chai kaam gaardaina

# print(join1)


def ReverseString(string):
    cis = "".join(reversed(string))
    print(cis)
ReverseString("python")


