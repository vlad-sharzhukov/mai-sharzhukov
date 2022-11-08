#Exersice 1
print ("Exersice 1\n")

list =[]
for i in range (10):
    a = int(input("Write a number\n"))
    list.append(a)
    b = f"\nLast {10 - len(list)} numbers\n"
    print (b)
        
sum (list)
print (f"The sum of the entered numbers is equal to {sum (list)}\n")
    

#Exersice 2
print ("Exersice 2\n")

list =[]
for i in range (10):
    a = int(input("Write number\n"))    
    list.append(a)
    b = f"\nLast {10 - len(list)} numbers\n"
    print (b)
        
list.count(0)
print (f"Amount of zero is equal to {list.count(0)}\n")


#Exersice 3
print ("Exersice 3\n")

n = int(input("How many steps do u want to do?)\n"))

print ("Thats your stairs!\n")

for i in range(n):
    for a in range(1, i+2):
        print(a, end="")
    print()
print ("\n")


#Exersice 4
print ("Exersice 4\n")

n = int(input('How many steps do u want to do to reach th top of ur pyramid?\n'))
for i in range(1, n+1):
    for c in range(n-i):
        print(' ', end='')
    for a in range(1,i+1):
        print (a, end = '')
    for b in range(i-1, 0, -1):
        print(b, end='')
    print()
