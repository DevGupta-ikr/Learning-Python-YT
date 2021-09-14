
for letter in "Giraffe Academy":
    print(letter)    # each letter of "Giraffe Academy"

friend = ["Jim", "Karen", "Kelly"]
for name in friend:
    print(name)

for index in range(10):
    print(index)   # output has 0 - 9

for index2 in range(3, 10):
    print(index2)   # output has 3 - 9

len(friend)  # length of array
for index in range(len(friend)):
    print(friend[index])


for index3 in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")
