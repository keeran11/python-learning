#Modules, Classes, and Objects
# mystuff = {'apple': 'I am apples!'}
# print(mystuff['apple'])



# mystuff['apple'] #get apple form dict
# mystuff.apple() #get apple form the module
# mystuff.tangerine #same thing, it's just a variable


#classes are like Modules


# class MyStuff(object):
#     def __init__(self):
#         self.tangering ="And now a thousands years between"

#     def apple(self):
#         print("i am Classy apples!")
# # Getting Things from Things
# # I now have three ways to get things from things:
# # dict style
# mystuff['apples']

# # module style
# mystuff.apples()
# print(mystuff.tangerine)

# # class style
# thing = MyStuff()
# thing.apples()
# print (thing.tangerine)


# class Song(object):
#     def __init__(self , lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# happy_bday = Song(["Happy birthday to you",
#                    "i don't want to get sued",
#                    "so I'll stop right there"])
# bulls_on_parade = Song(["They rally around the faimily",
#                         "with pockets full of shells"])

# national_song = Song([
#     "sayau thunga fulka hami",
#     "yeutai mala nepaali"
# ])

# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()
# national_song.sing_me_a_song()


# import random
# import requests
# import sys

# WORD_URL ="http://learncodethehardway.org/words.txt"
# WORDS = []

# PHRASES = {
# "class %%%(%%%):":
# "Make a class named %%% that is-a %%%.",
# "class %%%(object):\n\tdef __init__(self, ***)" :
# "class %%% has-a __init__ that takes self and *** parameters.",
# "class %%%(object):\n\tdef ***(self, @@@)":
# "class %%% has-a function named *** that takes self and @@@ parameters.",
# "*** = %%%()":
# "Set *** to an instance of class %%%.",
# "***.***(@@@)":
# "From *** get the *** function, and call it with parameters self, @@@.",
# "***.*** = '***'":
# "From *** get the *** attribute and set it to '***'."
# }

# #DO THEY Want to drill phrases first

# PHRASES_FIRST = False

# if len(sys.argv) == 2 and sys.argv[1] =="english":
#     PHRASES_FIRST = True


# #load up the wrods form the webistes
# response =requests.get(WORD_URL)
# for word in response.text.splitlines():
#     WORDS.append(word.strip())

# def convert(snippet, phrase):
#     # Generate class names and other names based on placeholders
#     class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
#     other_names = random.sample(WORDS, snippet.count("***"))

#     print(f"class name: {class_name}")  # Debugging
#     print(f"other names: {other_names}")  # Debugging

#     result_snippet = []
#     results_phrase = []
#     param_names = []

#     # Generate parameter names
#     for i in range(0, snippet.count("@@@")):
#         param_count = random.randint(1, 3)
#         param_names.append(', '.join(random.sample(WORDS, param_count)))

#     # Replace placeholders in both snippet and phrase
#     for sentence in (snippet, phrase):
#         result = sentence[:]

#         # Replace class names
#         for word in class_name:
#             result = result.replace("%%%", word, 1)

#         # Replace other names
#         for word in other_names:
#             result = result.replace("***", word, 1)

#         # Replace parameter names
#         for word in param_names:
#             result = result.replace("@@@", word, 1)

#         if sentence == snippet:
#             result_snippet.append(result)
#         else:
#             results_phrase.append(result)

#     # Ensure there are results to return
#     if not result_snippet:
#         result_snippet.append("no snippet generated")
#     if not results_phrase:
#         results_phrase.append("no phrase generated")

#     return result_snippet[0], results_phrase[0]

    

#     #keep going until they hit CTRl -D

# try:
#     while True:
#         snippets = list(PHRASES.keys())
#         random.shuffle(snippets)

#         for snippet in snippets:
#             phrase = PHRASES[snippet]
#             question, answer = convert(snippet, phrase)
#             if PHRASES_FIRST:
#                 question, answer = answer, question
#             print(question)

#             input(">")

#             print(f"Answer:{answer}\n")
# except EOFError:
#         print("\nBye")    



