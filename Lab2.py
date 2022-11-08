#Exersice 1. a=true b=false
    #false
    #false
    #true
    #false
    #false
    #4
    #0
    #1
    #2
    #False


a = True
b = False
 
print ("\nExersice 1")
for c in [
a and b, (a and b) or b, (a and b) or not (a and b), a and b or not (a or b) or b, b and b or not a and (a or b or a) or not (a or b), 1 << 2, 1 & 0 | 1 >> 1, 1 & 0 | 1 >> 0, 0b101 & 0b111 ^ 0b111 | 0b010, bool(0)
]:
    print (c)



#Exersice 2.

print ("\nExersice 2")
number1 = int(input("Enter nuber one\n"))
number2 = int(input("Enter nuber two\n"))

if number1 < number2:
    print (f"Number {number1} is smaller than {number2}")
elif number1 > number2:
    print (f"Number {number2} is smaller than {number1}")
elif number1 == number2:
    print (f"Number {number1} is equal {number2}")


#Exersice 3.

print ("\nExersice 3")
number1 = int(input("Enter nuber one\n"))
number2 = int(input("Enter nuber two\n"))
number3 = int(input("Enter nuber three\n"))

if number1 > number2 and number1 > number3:
    print (f"Number {number1} is the biggest number")
elif number2 > number1 and number2 > number3:
    print (f"Number {number2} is the biggest number")
elif number3 > number1 and number3 > number2:
    print (f"Number {number3} is the biggest number")
elif number1 == number2 and number2 == number3:
    print ("All numbers are equal")


#Exersice 4.
print ("\nExersice 4")

def show (storage):
    for el in storage:
        print (el)

def Ex4 (number1, number2, number3): 
    result = None
    list1=[number1, number2, number3]
    result = set(list1) 
    return result

storage = []
is_stop = 1 
while is_stop == 1:
    number1 = int(input("Enter nuber one\n"))
    number2 = int(input("Enter nuber two\n"))
    number3 = int(input("Enter nuber three\n"))

    result = Ex4 (number1, number2, number3)
    str_result = f"When number 1 = {number1}, number 2 = {number2}, number 3 = {number3} amout of unique numbers is {len(result)}\n"
    storage.append(str_result)

    show(str_result)

    is_stop = int(input("1-repeat exersice\n0-finish exersice\n"))

show(storage)
