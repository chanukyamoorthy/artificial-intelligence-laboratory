import random
import time

chr1 = []
chr2 = []
chr3 = []
chr4 = []
#chr5 = []
#chr6 = []

def fitness(t):
    h = 0
    for i in range(8):
        for j in range(i+1,8):
            if (t[i] == t[j]) or (abs(i-j) == abs(t[i] - t[j])):
                h += 1
    return 28-h 

def isvalid(nqueen):
    # print('nq ',end=" ")
    # print(nqueen)
    for i in range(0,7):
        row = nqueen[i]
        #print(row)
        for j in range(i+1,8):
            if(nqueen[i] == nqueen[j] or (abs(i-j) == abs(nqueen[i] - nqueen[j]))):
                # print(row)
                # print(nqueen[j])
                # print(i)
                # print(j)
                return False
    #print('cde')
    return True

chrsel1 = []
chrsel2 = []

   
#chr1 = [8,4,1,3,6,2,7,5]
#chr2 = [8,4,1,3,6,2,7,5]
for i in range(0,8):
    chr1.append(random.randint(1,8))
    chr2.append(random.randint(1,8))
    chr3.append(random.randint(1,8))
    chr4.append(random.randint(1,8))
    #chr5.append(random.randint(1,8))
    #chr6.append(random.randint(1,8))


fitval = []
fitval.append(fitness(chr1))
fitval.append(fitness(chr2))
fitval.append(fitness(chr3))
fitval.append(fitness(chr4))
#fitval.append(fitness(chr5))
#fitval.append(fitness(chr6))

print(fitval)
fitratio = []
fitt = []
tot = 0
for i in range(0,4):
    tot = tot+ fitval[i]

for i in range(0,4):
    fitratio.append(int((fitval[i]/tot)*100))
    ll = []
    ll.append(int((fitval[i]/tot)*100))
    ll.append(i)
    fitt.append(ll)

ff = sorted(fitt, key=lambda x: x[0])
print(ff)
chrsel1 = []
chrsel2 = []
if(ff[3][1] == 0):
    chrsel1 = chr1
if(ff[3][1] == 1):
    chrsel1 = chr2
if(ff[3][1] == 2):
    chrsel1 = chr3
if(ff[3][1] == 3):
    chrsel1 = chr4


if(ff[2][1] == 0):
    chrsel2 = chr1
if(ff[2][1] == 1):
    chrsel2 = chr2
if(ff[2][1] == 2):
    chrsel2 = chr3
if(ff[2][1] == 3):
    chrsel2 = chr4


#print('abcd ')
#print(chrsel1)
#print(chrsel1)

#bestfit(chrsel1,chrsel2)

while(1):
	#sleep(1)
	
    if isvalid(chrsel1) :
        print(chrsel1)
        qboard = []
        for i in range(0,8):
            temp = []
            for j in range(0,8):
                
                temp.append('-')
            qboard.append(temp)
            #print()
        #print(qboard)
        for i in range(0,8):
            qboard[8-chrsel1[i]][i] = 'Q'
        
        for i in range(0,8):
            for j in range(0,8):
                print(qboard[i][j],end=" ")
            print()

        break
    if isvalid(chrsel2) :
        print(chrsel2)
        break
    #time.sleep(1)
    chr1 = chrsel1
    chr2 = chrsel2

    crossover = random.randint(1,7)
    first1 = chrsel1[0:crossover]
    second1 = chrsel1[crossover:8]
    first2 = chrsel2[0:crossover]
    second2 = chrsel2[crossover:8]
    
    ff1 = []
    ff2 = []
    for i in range(0,len(first1)):
        ff1.append(first1[i])
    
    for i in range(0,len(second2)):
        ff1.append(second2[i])

    for i in range(0,len(first2)):
        ff2.append(first2[i])
    
    for i in range(0,len(second1)):
        ff2.append(second1[i])

    
    fit = []
    fit3 = fitness(ff1)
    fit4 = fitness(ff2)

    randgen = random.randint(1,8)
    randind = random.randint(0,7)
    ff1[randind] = randgen

    randgen = random.randint(1,8)
    randind = random.randint(0,7)
    ff2[randind] = randgen

    chr3 = ff1
    chr4 = ff2

    fit1 = fitness(chrsel1)
    fit2 = fitness(chrsel2)
    fit5 = fitness(ff1)
    fit6 = fitness(ff2)
    fit.append(fit1)
    fit.append(fit2)
    fit.append(fit3)
    fit.append(fit4)
    fit.append(fit5)
    fit.append(fit6)
    tot = (fit1+fit2+fit3+fit4+fit5+fit6)
    fitratio = []
    fitt = []
    tot = 0
    for i in range(0,4):
        tot = tot+ fitval[i]

    for i in range(0,4):
        fitratio.append(int((fit[i]/tot)*100))
        ll = []
        ll.append(int((fit[i]/tot)*100))
        ll.append(i)
        fitt.append(ll)

    ff = sorted(fitt, key=lambda x: x[0])
    #print(ff)
    chrsel1 = []
    chrsel2 = []
    if(ff[3][1] == 0):
        chrsel1 = chr1
    if(ff[3][1] == 1):
        chrsel1 = chr2
    if(ff[3][1] == 2):
        chrsel1 = chr3
    if(ff[3][1] == 3):
        chrsel1 = chr4
    

    if(ff[2][1] == 0):
        chrsel2 = chr1
    if(ff[2][1] == 1):
        chrsel2 = chr2
    if(ff[2][1] == 2):
        chrsel2 = chr3
    if(ff[2][1] == 3):
        chrsel2 = chr4
    
    #print(chrsel1)
    #print(chrsel2)
        
 

