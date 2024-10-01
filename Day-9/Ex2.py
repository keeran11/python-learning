'''there are 2 male and female  chicken in the begineerof the year ,
 female give always 2 children i.e male and female and the the child can become parent 
 and give birth to the child when it reach 1 year , no one is died during those 10 year, find the total number of chicken in the family.'''

def calculate_chicken_population(years):
    males = 1
    females = 1
    for year in range(1, years + 1):
        # Each female gives birth to 1 male and 1 female
        new_males = males
        new_females = females
        males += new_males
        females += new_females
    total_chickens = males + females
    return total_chickens


years = 10
total_chickens = calculate_chicken_population(years)
print(total_chickens)
