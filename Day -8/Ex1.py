#find the length of the string
#method1

# string = "hello my name is kiran."
# print(len(string)) #using the len() function can be used to find the length of the string.


#method 2
# string = "hello my name is kiran." #string is the sequence type data type
# count =0
# for i in string:
#     # print(i)
#     count +=1
# print(count)


#method 3
# #using the while loop


# string = "kiran"
# count =0
# while count <len(string):
#     count +=1
# print(count)



#method 4
#using the function ()
#  sub_method 1

# def count_length(string):
#     count =0
#     for i in string:
#         count += 1
#     print(count)
    
# count_length("hello my name is kiran acharya")

# using function() sub_method 2

# def count_length(string):
#     count =0
#     for i in string[count:]:
#         count +=1
#         # print(count)
#         print(i)
#     print(count)
    
# count_length("hello")

#method 5
#using the join() and count()


# string ='kiran A'
# length ="".join(string).count('') -1
# print(length)

'''join() method is used to combine all character of the string in a new string using the separator provided before join()
here in kiran acharya there is empty string 
"" so, "".join(string) doesn't actually change the sting , it just combine the character without any separator, resulting 
kiran Acharya

.count(''):
the count() method count how many empty string occurance exist between characters
in the kiran Acharya sting there is alwasya an empty space between each character(and before the first characer and the after the last character)
|k|i|r|a|n| |A|c|h|a|r|y|a| = this will return 14
'''

#method 6
#Using the Recursion

# def string_length(s):
#     if s == "":
#         return 0
#     else:
#         return 1 + string_length(s[1:])
# string ="python"
# length =string_length(string)
# print(length)

#method 7
#using the enumerate()
'''(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')
The enumerate() function is used to iterate over the string. enumerate() 
provides both the index of each character and the character itself.'''


string = "python"
count = 0 
for index, char in enumerate(string):
    count = index +1
print(count)


#using thie list comprehension
'''[expression for item in iterable if condition]
Where:

expression: This is the value or operation that produces the elements of the new list.
item: This represents the element from the iterable (e.g., a list, string, or range).
iterable: The collection you are iterating over (e.g., list, string).
condition (optional): A filter that determines which elements to include.'''


string = "python"
length =len([char for char in string])
print(length)