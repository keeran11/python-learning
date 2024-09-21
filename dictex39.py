#Dictionaries

#python calls them "dicts", other languages call them "hashes"

# things = [ 'a', 'b', 'c','d']
# print(things[1])


# things[1] = 'z'
# print(things[1])
# print(things)


# stuff = {'name': 'Zed', 'age':36,'height': 6*12+2}
# print(stuff['name'])
# print(stuff['height'])

# # create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}
print(states)
# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print(cities)


# #print out some cities
# print("-"*10)
# print("Ny States has:", cities['NY'])
# print("OR state has:",cities['OR'])

# #print some states
# print("-"*10)
# print("Michigan's abbreviation is:", states['Michigan'])
# print("Florida's abbreviation is:", states['Florida'])

#print every state abbreviation
# print("-"*10)
# for state, abbrev in states.items():
#     print(f"{state} is abbreviated {abbrev}")

# # print every city in state
# print("-"*10)
# for abbrev, city in cities.items():
#     print (f"{abbrev} has the city {city}")



# # now do both at the same time
# print("-"*10)
# for state, abbrev in states.items():
#     print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")
    
# print("-"*10)
# # safely get an abbreviation by state that might not be there
# state = states.get('Texas', None)
# if not state:
#     print("Sorry, no Texas.")


# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print(f"The city for the state 'TX' is: {city}")

