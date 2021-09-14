
employee_file = open("employee.txt", "r")  # r ead, w rite, a ppend

print(employee_file.readable())  # check readablility
#print(employee_file.read())  # reads all lins at once

print(employee_file.readline())  # reads one line at a time
print(employee_file.readline())

#print(employee_file.readlines())  # makes it an array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()