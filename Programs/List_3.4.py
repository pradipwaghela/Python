

from os import PRIO_USER


guest=["Pradip","Karan","hitesh","ritesh"]
print("hey,",guest[0])
print("This is to invite for Dinner party ")

print("hey,",guest[1])
print("This is to invite for Dinner party ")

print("hey,",guest[2])
print("This is to invite for Dinner party ")

print("hey,",guest[3])
print("This is to invite for Dinner party ")

print(guest)

pl=int(input("Who will not be able to come enter place "))
guest.pop(pl)

gName=input("Do you want to invite someone else  enter hes/her Name:-")
guest.insert(pl,gName)

gName=input("Do you want to invite someone else  enter hes/her Name:-")
guest.insert(0,gName)

print(guest)
print(guest.pop())
print(guest.pop())
print(guest.pop())
print("Final List")

print(guest)
print("Invitation Send to ",guest[0])
del guest[0]
print("Invitation Send to ",guest[0])
del guest[0]
print(guest)
print("Invitation Done!!")
