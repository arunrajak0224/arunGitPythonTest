# # ctrl + / to comment
# list set , tuples 
# experimental git code
# ------------------

# 1.list
# Lists are mutable, they are sort of like an array that grows
# lists are not homogeneous which means it allows differnt data types
# list syntax is in square brackets []
# eg
listOfCars = ["Bmw", "audi", "Mercedes",3, "Mercedes"]
print("List of Cars are: ",listOfCars)

# 2.Tuples 
# TUples are immutable , they are similar to list except they are immutable
# tuples also can store heterogeous values
# they are denoted with parantheses ()
tuplesOfLaptops=["hp","Dell","Mac",1]
print("Tuples of laptops are: ",tuplesOfLaptops)

# 3.set
# sets are unordered collection they are mutable , but here no duplicate values are allowed
# Sets are mutable, however, only immutable objects can be stored in it.
# eg 

setOfColonge={"Givenchy",1,"Cobra",2}
print(" sets of colonge: ",setOfColonge)

# sets can be used in sceneario where we want to delete duplicate elements eg
# eg A user trying to log in at multiple times 
listOfEmployee=[1,2,3,4,5,6,1];
setOfEmployee=set(listOfEmployee)
print("Set of employee",setOfEmployee)

