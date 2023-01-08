variable1=input("PLease enter a number to sum : ")
variable2=input("PLease enter another number to sum : ")
# if we dont covert it to int it will assume its a string and our op would be 55 
# so we have to type cast it 
print("Sum of two input is without type casting: ",variable1+variable2) 
print("Sum of two input is: ",int(variable1)+int(variable2)) 


