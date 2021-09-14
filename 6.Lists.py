
old_friends = ["Kevin", "karen", "Jim"]

print(old_friends)  # All list elements
print(old_friends[1])  # only indexed position element
print(old_friends[-2])  # from backwards
print(old_friends[1:3]) # from 1 to 3(dne so till 2 only )


# Function in Lists

lucky_numbers = [4, 8, 15, 16, 23, 42]
new_friends = ["Kevin", "karen", "Jim", "Oscar", "Tobey"]

new_friends.extend(lucky_numbers)  # Adds all elements of second to back of first
new_friends.append("Creedy")  # Same work

new_friends.insert(1, "Kelly")  # to add element in the middle
new_friends.remove("Jim")
new_friends.clear()  # Empties the entire list

new_friends = ["Kevin", "karen", "Jim", "Oscar", "Tobey"]
new_friends.pop(1)

print(new_friends)
print(new_friends.index("Jim"))
print(new_friends.count("Karen"))  # Popped out so 0
new_friends.sort()  # implemented like this
print(new_friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends = new_friends.copy()
print(friends)
