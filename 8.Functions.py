
# Function Declaration
def say_hi():
    print("Hello User")

print("Top")
say_hi()  # To execute the code
print("Bottom")

def say_name(name, age):
    print("Hello " + name + ", you are " + age)


say_name("Peter", "22")  # passing value into function


def cube(num):
    return num*num*num  # if return is not written, no output
    print("Code")  # Not printed


result = cube(3)
print(result)