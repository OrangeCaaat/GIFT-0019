import random

file = open("name_list.txt","r")
name_list = []
for i in file:
    name_list.append(i)
print(random.choice(name_list))
file.close()
