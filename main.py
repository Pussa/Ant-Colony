from random import choices
ants = 100000 # Количество муравьев
matrix = list()
matrix.append(list(map(int, input().split()))) # Получение матрицы 
for i in range(1, len(matrix[0])):
    matrix.append(list(map(int, input().split())))
cs = len(matrix)
a =0.1
b = 2.5  #Задание значения костант 
Q = 1

def sig(cs, t, a, n, b):
    sigma = 0                                       
    for i in range(cs):
        for j in range(cs):
            sigma = sigma + t[i][j] ** a * n[i][j] ** b
    return sigma

def nn(matrix,cs):
    n = [[1 / matrix[i][j] if matrix[i][j] != 0 else 0 for j in range(cs)] for i in range(cs)]
    return n

n = nn(matrix,cs)
t = [[Q for j in range(cs)] for i in range(cs)]     #Ферамон
sigma = sig(cs,t,a,n,b) 
p = [[(t[i][j]**a*n[i][j]**b)/sigma for j in range(cs)] for i in range(cs)]      # Расчет начальной матрицы вероятностей

L = 0
LL= 1000000000000000
zapomnit = 0
index_otkuda = 0
count = 0
for ant in range (ants):
    ants_mass = [j for j in range(cs)] #Список посещенных городов
    zxc = ant%cs #Определение первого города
    ants_mass[zxc] = -1
    index_otkuda = zxc
    L = 0
    count = 0
    choice =-1                     #Алгоритм выбора пути
    count2 = 0

    while(count!=cs):
        while(choice==-1):
            choice = choices(ants_mass,weights=p[index_otkuda])[0]
            if (choice>-1) :
                ants_mass[choice] = -1
                count2+=1

            if (count2==cs-2):

                L = L + matrix[index_otkuda][choice]
                index_otkuda =choice
                count2 +=1
                ants_mass[choice] = -1
                for w in range (cs):
                    if ants_mass[w]!=-1:
                        zapomnit =ants_mass[w]

                choice =zapomnit
              

            if count2 ==cs or count2 ==cs-1:
               
                break

        L = L+matrix[index_otkuda][choice]

        t[index_otkuda][choice] = t[index_otkuda][choice] + Q / L
        sigma = sigma + t[index_otkuda][choice] ** a * n[index_otkuda][choice] ** b  # Обновление вероятностей после обновления уровня ферамона
        p[index_otkuda][choice] = (t[index_otkuda][choice] ** a * n[index_otkuda][choice] ** b) / sigma
        index_otkuda = choice
        count += 1
        choice =-1
    if L +matrix[index_otkuda][zxc] <LL  :
        LL =L +matrix[index_otkuda][zxc]
          


print(LL)
