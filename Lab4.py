#Exersice 1
print ("Exersice 1\n")

any_list = [1,2,3,3,3,4,5,6,7,7,8,8,9,10,22,33,4,5,6,7,8]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(any_list)

#Exersice 2
print ("Exersice 2\n")

any_list = [1,2,3,4,3,2,1,1,2,3,4,6,789,0,99999,7,75,4,3]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)

#Exersice 3
print ("Exersice 3\n")

any_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def replacement(list):
    i_of_max_el = list.index(max(list))
    i_of_min_el = list.index(min(list))
    list[i_of_max_el], list[i_of_min_el] = list[i_of_min_el], list[i_of_max_el]
    print(list)
replacement(any_list)

#Exersice 4
print ("Exersice 4\n")

d = {1: 'опаньки...', 2: 'приветик', 3: 'че как?', 4: 'Россия!'}
key = int(input('Введите ключ, чтобы получить его значение: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(d)