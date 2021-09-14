# First Line
print("Hello World")
# First Pattern
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

# VARIABLES
character_name = "John"  # String
character_age1 = 35  # Number
character_age = 35.57647654  # Number
is_Male = True  # Boolean
is_Female = False

# Strings

Age = "50"
print("There was once a person named " + character_name + ",")
print("He was " + Age + " years old.")
character_name = "Mike"
print("When " + character_name + " was " + Age + " he was ok.")
print("Not ill so far")

# More on Strings

print("Giraffe\nAcademy")  # prints Giraffe and Academy on separate lines
print("Giraffe\"Academy")  # Output: Giraffe"Academy
print("Giraffe\Academy")  # Output: Giraffe\Academy

phrase = "DAG"
print(phrase)  # using variables
print(phrase + " is cool")  # concatenation


# Functions in Strings

phrase = "Hello ThErE"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.lower().islower())
print(phrase.upper().isupper())
print(len(phrase))

# phrase = "Hello ThErE"
print(phrase[0])  # Character index Starts with 0
print(phrase[3])
print(phrase[6])

print(phrase.index("l"))  # First occurrence of character

print(phrase.replace("Hello", "Hello!!->"))

