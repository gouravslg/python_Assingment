#If a five digit number is input through the keyboard, write a program to print a new numb er
#by adding one to each of its digits. For example if the number that is input is 12391 then the
#output should be displayed as 23402.

num = input("Enter a five-digit number: ")

new_number = "  "


for digit in num:
    new_digit = (int(digit) + 1) % 10 
    new_number += str(new_digit) 
print("The new number is :",new_number)