A = [
    [1,2],
    [3,2]
]
B = [
    [3,2],
    [1,1]
]
def show (matr):
    for line in matr:
        print ("|", end = ' ')

        
        for el in line:
            print (el, end = " ")
        print ('|')
    print ('\n')
show(A)
show(A)

def mul_mat (m1,m2):
    result = []
    for i in range(len(m1)):
        matr_rol = []
        for j in range(len(m1[1])):
            sum = 0
            for k in range(len(m1)):
                sum += m1[i][k]*m2[k][j]
            matr_rol.append (sum)
        result.append(matr_rol)
    return result 
mul_mat(A,B)
show(mul_mat(A,B))
