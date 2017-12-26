# 7A
# Write a python program to define a student class that includes name,
# usn and marks of 3 subjects. Write functions calculate() - to calculate the
# sum of the marks print() to print the student details.




class student:
	usn = " "
	name = " "
	marks1 = 0
	marks2 = 0
	marks3 = 0

	def __init__(self,usn,name,marks1,marks2,marks3): #Constructor
		self.usn = usn
		self.name = name
		self.marks1 = marks1
		self.marks2 = marks2
		self.marks3 = marks3



	def calculate(self): # Member Function
	    print ("usn : ", self.usn, "\nname: ", self.name,"\nTotal is ", (self.marks1 + self.marks2 + self.marks3)/3)


print ("Result of Named object of student calling calculate ")
s1 = student("1MSIS16048", "Parineethi Chopra", 78, 76,62)
s1.calculate()
