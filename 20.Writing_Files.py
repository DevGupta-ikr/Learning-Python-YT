
employee_file = open("employees.txt", "w")  # r ead, w rite, a ppend
# In the above, is you write "a", it adds the new text to existing file
# else if you write "w", it removes everything and writes what you have written below
# if you change the file name in above to employees1, it makes a new file for you automatically


employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")
#print(employee_file.read())

employee_file = open("index.html", "w")
employee_file.write("<p> HTML Code </p>")

employee_file.close()

