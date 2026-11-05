

name = input("Enter Student Name : ")
age = int(input("Enter Student age : ")) 
student_class = input("Enter Student class : ")

math = float(input("Enter Math marks : ")) 
english = float(input("Enter English marks : "))
science = float(input("Enter Science marks : "))

total = math + english + science 
average = total / 3 

print("\n===== Student Information =====")
print("Name : ",name )
print("Age : ",age)
print("Class : ",student_class)
print("Total Marks : ",total)
print("Average Marks : ",average)

print("\n===== Data Types =====")
print("Name type : ",type(name))
print("Age Type :",type(age))
print("Average type : ",type(average))