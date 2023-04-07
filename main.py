import random
items = []
#loops check
for i in range(-20,45,5):
    print(i, end = " ")

print()

for i in range(2):
    for j in range(5):
        print("*", end = "")
    print()
    
num = 50
while num >= 0:
    print(num, end = " ")
    num-=10

print()

choice = "Here's a cookie"
while choice != "no":
    print(choice)
    choice = input("Do you want another one?  yes or no")
    
print("ok see ya")

print()

#function check
def MonsterGenerator ():
    num = random.randrange(1, 100)
    if num < 20:
        items.append("skeleton")
        print("There's a skeleton!")
    elif num < 50:
        items.append("zombie")
        print("There's a zombie!")
    elif num < 60:
        items.append("witch")
        print("There's a witch!")
    else:
        print("no monsters appeared")
        
    print("Monsters appeared", items)
    
while(1):
    MonsterGenerator()
    input()
    

