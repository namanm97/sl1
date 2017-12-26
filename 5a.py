#5A 
#Write a python program to read in a list of numbers.
# Use one-line comprehensions of create a new list of even numbers.
# Create another list reversing the elements.



ip_list=eval(raw_input("Enter the list comma seprated : "))
even_list=[x for x in ip_list if x%2 == 0.0 ]
print ("Even list : ",even_list)
print ("Even reversed list : ",even_list[::-1])
