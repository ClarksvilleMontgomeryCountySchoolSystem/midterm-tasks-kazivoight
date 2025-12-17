slices= party_pizza_mini+large+medium
print(slices)

people= people+1
each_person_gets= slices//int(people)
leftover=slices%int(people)
print(each_person_gets)
print(leftover)

people= people+2 #Eric and Brandon are coming too.
each_person_gets= slices//int(people)
leftover= slices%int(people)
print(each_person_gets)
print(leftover)

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

slices=party_pizza_mini*2+large+medium
each_person_gets=slices//int(people)
leftover=slices%int(people)
print(each_person_gets)
print(leftover)
print("...for Mr. Hollow Leg")
