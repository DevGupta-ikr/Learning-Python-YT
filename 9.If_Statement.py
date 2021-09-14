is_male = False
is_tall = True

if is_male or is_tall:  # and , or operators in python
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_male:
    print("You are tall but not male")
else:
    print("You are neither male not tall")


# If Statements and Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("Maximum is " + num1)
    elif num2 >= num1 and num2 >= num3:
        print("Maximum is " + num2)
    else:
        print("Maximum is " + num3)

max_num("1", "2", "3")
