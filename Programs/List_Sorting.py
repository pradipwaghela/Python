"""
Function                 Syntax                             Desciption
sort()                  list.sort()                 Use to sort list in alphabetical order
sort(reverse=True)      list.sort(reverse=True)     Use to sort list in reverse alphabetical order
sorted()                list.sorted()               Use to temporary sort list
len()                   len(list)                   Use to find lenght of list 
"""



cars=["Maruti Suzuki","Hyundai Motors","Tata Motors","Toyota","Kia Motors","Skoda","MG","Mercedes","Volkswagen","Honda","Renault","Mahindra","BMW","Jeep","Ford","Nissan","Audi","Datsun","Tesla"]

print("Total car brand in India",len(cars))

cars.sort()
print("Sorted A - Z:-",cars)


cars.sort(reverse=True)
print("Sorted Z-A:-",cars)

print("Temporary sorted:-",sorted(cars))

print(cars)