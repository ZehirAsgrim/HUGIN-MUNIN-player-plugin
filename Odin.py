import pickle
import sys
import random
length = 40
population = 21
userID = sys.argv[2]
#################################################################################
if  sys.argv[1] == '2':

    try:
        with open(str(userID)+'.pickle','rb') as file:
            eq=pickle.load(file)

    except :
        eq = []
        eq.append([])
        eq[0].append(0)#eq[0][0] is serial number
        #initialnization
        eq.append([])
        eq[1].append([-1.5, -2, -2, -2.5, -2.5, -3, -3, -3, -3, -3,
                    -2, -1, 0.5, 1.5, 2, 3, 3.5, 4, 4, 4,
                    4, 4, 4, 3.5, 3.5, 3, 3, 2.5, 2, 1.5,
                    1.5, 1, 0.5, 0.5, 0, -0.5, -0.5, -1, -1, -1.5])
        eq[1].append([5, 4.5, 4.5, 4.5, 4, 4, 4, 3.5, 3.5, 3.5,
                    3, 3, 2.5, 2.5, 2, 1.5, 1.5, 1, 1, 0.5,
                    0.5, 0.5, 0, -0.5, -0.5, -0.5, -1, -1.5, -2, -2,
                    -2.5, -2.5, -3, -3, -3.5, -3.5, -3.5, -4, -4, -4.5])
        eq[1].append([4.5, 4.5, 4.5, 4, 4, 4, 3.5, 3.5, 3.5, 3,
                    3, 2.5, 2.5, 2.5, 2, 1, -1, -1.5, -1.5, -1.5,
                    -1.5, -1.5, -1.5, -1, -0.5, -0.5, 0, 1, 1.5, 2,
                    2.5, 2.5, 2.5, 3, 3, 3, 3, 3.5, 3.5, 3.5])
        eq[1].append([4.5, 4, 4, 4, 3.5, 3.5, 3, 2.5, 2, 1.5,
                    1.5, 1, 1, 1, 1.5, 2, 2.5, 3, 3, 2.5,
                    2.5, 2, 2, 1.5, 1.5, 1, 1, 0, -0.5, -1,
                    -2, -2, -2.5, -3, -3.5, -3.5, -4, -4, 4, -4.5])
        eq[1].append([-3, -2.5, -2, -2, -1.5, -1.5, -1, -1, -1, -0.5,
                    0, 0.5, 1, 1.5, 2, 3, 3.5, 4, 4, 3.5,
                    3.5, 3, 3, 2, 1.5, 1, 0, -0.5, -1, -1,
                    -1.5, -0.5, 0, 1, 2, 2, 1.5, 1.5, 1, 1])
        eq[1].append([4.5, 4, 3.5, 3.5, 3, 3, 2, 1, 0.5, 0,
                    0, 0, 0, 0, -0.5, -1, -1, -1.5, -1.5, -1.5,
                    -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1, -1, -0.5,
                    0, 1, 1.5, 2, 3, 3, 3.5, 3.5, 4, 4.5])
        eq[1].append([-1.5, -1.5, -1.5, -1, -1, -1, -0.5, -0.5, -0.5, 0,
                    0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4, 4,
                    4, 4, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5,
                    0, -0.5, -0.5, -0.5, -1, -1, -1, -1.5, -1.5, -1.5])
        eq[1].append([5, 4.5, 4.5, 4.5, 4.5, 4, 4, 3.5, 3.5, 3.5,
                    3, 3, 2.5, 2.5, 2, 1.5, 1.5, 1, 1, 1,
                    0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        eq[1].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5,
                    0.5, 1, 1, 1.5, 2, 2, 2.5, 2.5, 3, 3,
                    3.5, 3.5, 3.5, 4, 4, 4, 4.5, 4.5, 4.5, 5])
        eq[1].append([5, 5, 5, 5, 5, 5, 4.5, 4.5, 4.5, 4,
                    3, 2.5, 2, 1, 1.5, 1.5, 1.5, 2, 2, 2,
                    2, 2, 2, 2.5, 2.5, 3, 3.5, 3.5, 3.5, 4,
                    4, 4, 3.5, 3.5, 3.5, 3, 3, 2.5, 2.5, 2])
        eq[1].append([-5, -4.5, -4.5, -4.5, -4, -4, -4, -3.5, -3.5, -3.5,
                    -3, -3, -3, -2.5, -2, -1.5, -1.5, -1, -1, -1,
                    -0.5, -0.5, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        eq[1].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, -0.5, -0.5,
                    -1, -1, -1, -1.5, -1.5, -2, -2.5, -3, -3, -3,
                    -3.5, -1.5, 0.5, 2.5, 4.5, 4.5, 4.5, 5, 5, 5])
        eq[1].append([5, 4.5, 4.5, 4, 4, 4, 3.5, 3.5, 3, 3,
                    2.5, 2, 2, 1.5, 1, 0.5, 0, -0.5, -0.5, -0.5,
                    -1, -1, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2,
                    2.5, 2.5, 3, 3, 3.5, 3.5, 4, 4, 4, 4.5])
        eq[1].append([3, 3.5, 4, 4, 4.5, 5, 5, 5, 5, 5,
                    4, 3, 2, 1.5, 1, 0, -1, -2, -2, -2,
                    -1.5, -1.5, -1.5, -1, 0, 1, 2, 2.5, 2.5, 2.5,
                    3, 3, 3, 3, 3, 3.5, 3.5, 3.5, 4, 4])
        eq[1].append([4.5, 4.5, 4.5, 4, 4, 4, 3, 2, 1.5, 1,
                    1, 0.5, 0.5, 0, -0.5, -1, -1.5, -2, -1, -0.5,
                    0, 1, 2, 1.5, 1.5, 1.5, 1, 1, 1, 1.5,
                    1.5, 2, 3, 3.5, 4, 4, 4, 4.5, 4.5, 5])
        eq[1].append([3.5, 4, 4, 4.5, 4.5, 5, 5, 5, 5, 5,
                    3.5, 2.5, 1, 0, 0.5, 1, 1, 1.5, 2, 2.5,
                    2.5, 3, 3.5, 4, 4.5, 4.5, 5, 5, 4.5, 4.5,
                    4.5, 4.5, 4, 4, 4, 3, 2, 1, 0.5, 0])
        eq[1].append([-3.5, -3, -2.5, -2, -1, -0.5, -0.5, -0.5, 0, 0,
                    0.5, 0.5, 0.5, 1, 2, 2.5, 3, 4, 4, 4,
                    4.5, 4.5, 4.5, 4.5, 4.5, 5, 5, 5, 4.5, 4.5,
                    4.5, 4, 3, 2.5, 2, 1.5, 1, 1, 0.5, 0])
        eq[1].append([5, 4.5, 4.5, 4, 4, 4, 3, 2.5, 2, 1.5,
                    2, 2, 2.5, 3, 2, 1, 0, -1, -1, -1,
                    -1, -1, -1, -0.5, 0, 1, 1.5, 1, 0.5, 0,
                    -0.5, 0, 1, 1.5, 2, 2, 2.5, 2.5, 2.5, 3])
        eq[1].append([3, 2.5, 2.5, 2.5, 2, 2, 1.5, 1, 0.5, 0,
                    1, 1.5, 2, 2.5, 2.5, 3, 3, 3, 2.5, 2,
                    2, 1.5, 1.5, 2, 2.5, 3, 3.5, 3.5, 4, 4,
                    4.5, 4, 4, 3.5, 3, 3, 3.5, 3.5, 3.5, 4])
        eq[1].append([4, 3.5, 3.5, 3, 3, 3, 2.5, 2, 2, 1.5,
                    1.5, 1.5, 2, 2, 1, 0, -0.5, -1.5, -1.5, -1.5,
                    -1.5, -1.5, -1.5, -1, -1, -0.5, 0, 0.5, 1, 1,
                    1.5, 2, 2.5, 2.5, 3, 3, 3.5, 3.5, 3.5, 4])
        eq[1].append([5, 4.5, 4.5, 4, 4, 4, 3, 2, 1, 0,
                    0, 0, 0, 0, -0.5, -1, -1.5, -2, -1.5, -1,
                    -1, -0.5, 0, -0.5, -0.5, -0.5, -1, -2, -3, -4,
                    -5, -2, 0, 2, 5, 4, 3, 2.5, 2, 1])
        #like or not
        for i in range(population):
            eq[1][i].append(0)
        #shuffle
        random.shuffle(eq[1])
    #output eq
    n = eq[0][0] % population
    for i in range(length):
        print(float(eq[-1][n][i]))
    print(eq[0][0])
    file = open(str(userID)+'.pickle', 'wb')
    pickle.dump(eq, file)
    file.close()
    with open('eq_'+str(userID)+'.txt', 'w') as fp:
        fp.write('{')
        for i in range(length):
            fp.write('"band'+str(i+1)+'":')
            fp.write(str(float(eq[-1][n][i])))
            if i+1 < length:
                fp.write(',')
        #fp.write(', "serial num":'+str(eq[0][0]))
        fp.write('}')
#################################################################################
elif sys.argv[1] == '0' or sys.argv[1] == '1':
    with open(str(userID)+'.pickle','rb') as file:
        eq=pickle.load(file)
    n = eq[0][0] % population
    if sys.argv[1] == '0':
        eq[-1][n][length] -= 1
    else:
        eq[-1][n][length] += 1

    eq[0][0]+=1
    if eq[0][0] % population == 0: #end of a generation
        parents = []
        for i in range(population):
            if (eq[-1][i][length] > 0):
                parents.append(eq[-1][i])

        #check if end
        if len(parents) == 0:
            for i in range(len(eq[1])):
                parents.append([])
                for j in range(11):
                    parents[-1].append(0)

        if len(parents) == 1:
            parents.append(parents[-1])


        #crossover
        children = []
        target_number = len(eq[1]) - len(parents)
        while len(children) < target_number:
            male = random.randint(0, len(parents)-1)
            female = random.randint(0, len(parents)-1)
            if male != female:
                cross_pos = random.randint(1, length-1)#random cross position
                father = parents[male]
                mother = parents[female]
                child = []
                for i in range(length):
                    if i < cross_pos:
                        child.append(father[i])
                    else:
                        child.append(mother[i])
                child.append(0)
                children.append(child)

        eq.append([])
        for i in range(len(parents)):
            eq[-1].append(parents[i])
        for i in range(len(children)):
            eq[-1].append(children[i])

        #mutation
        mutation_rate = 0.5
        for i in range(population):
            if random.random() < mutation_rate:
                if random.random() < 0.5:
                    eq[-1][i][random.randint(0,length-1)]*=-1
                else:
                    eq[-1][i][random.randint(0,length-1)] = round(max(min(random.gauss(0,5),10),-10),1)
        #shuffle
        random.shuffle(eq[-1])

        #print('end')#########################for test
    for i in range(length):
        print(float(eq[-1][n][i]))
    print(eq[0][0])
    file = open(str(userID)+'.pickle', 'wb')
    pickle.dump(eq, file)
    file.close()
    with open('eq_'+str(userID)+'.txt', 'w') as fp:
        fp.write('{')
        for i in range(length):
            fp.write('"band'+str(i+1)+'":')
            fp.write(str(float(eq[-1][n][i])))
            if i+1 < length:
                fp.write(',')
        #fp.write(',"serial num":'+str(eq[0][0]))
        fp.write('}')
