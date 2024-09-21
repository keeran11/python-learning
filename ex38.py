
ten_thing = "Apples Oranges Crows Telephone Light sugar"

print("wait there's not 10 things in that list, let's fix that")

stuff = ten_thing.split(' ')
more_stuff =["day", "night","song", "fribee", "corn", "Banana", "girl", "boy"]

while len(stuff)!=10:
    next_one =  more_stuff.pop() 
    print("adding:", next_one)
    stuff.append(next_one)
    print(f"there's {len(stuff)} items now ")
print(f"there we go:{stuff}")

print("let's do some thing with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())#it will remove the last element
print(stuff)
print(' '.join(stuff))
print('#'.join(stuff[1:6]))
