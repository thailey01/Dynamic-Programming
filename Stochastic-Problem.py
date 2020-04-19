'''
This program is for solving a stochastic dynamic programming problem similar
to problem 19.31 in Schaum's Operations Research Second Edition
April 19, 2020
'''
import numpy as np
import sys

numOfSites = int(input('How many sites can be developed? ' ))
money = int(input('How many units of money are at our disposal? '))

initialTable = np.zeros((numOfSites,money+1), dtype=float)
probArray = np.zeros((numOfSites), dtype=float)

print('Now we will create our initial table')
print('\nInput the probability of finding oil, if it exists,'
      ' with the amount of money allocated to that site')
for i in range(initialTable.shape[0]):
    print('Site', i+1)
    for j in range(initialTable.shape[1]):
        initialTable[i][j] = float(input(str(j) + ' money allocated:'))
    print('~~~~~~~~~~~~~~~\n')

print('Now enter the probability that oil exists at each site')
for i in range(probArray.shape[0]):
    probArray[i] = float(input('Site ' + str(i+1) + ': '))
print('\n\n')
# The next block of code is for printing out the table in a way that 
# looks similar to what is given in the book
print('The following table displays the probability of finding oil at each'
          ' site if it exists\n')
for i in range(initialTable.shape[0]+1):
    for j in range(initialTable.shape[1]+1):
        if i==0 and j ==0:
            print('\t\t|\t', end='')
        elif i==0 and j!=0:
            print(j-1,'\t|\t', end='')
        elif i!=0 and j==0:
            print('Site', i, '\t|\t', end='')
        else:
            print(initialTable[i-1][j-1], '\t', end='')
    if i == 0:
        print()
        for k in range(initialTable.shape[1]*2+2):
            print('____', end='')
    print()

# f is our expected return for each site and it's probability of finding oil
f = np.zeros([initialTable.shape[0],initialTable.shape[1]], dtype=float)
#The return table is for m_j(u)
returnTable = np.zeros((numOfSites, money+1), dtype=float)
#The decision table is for d_j(u)
decisionTable = np.zeros((numOfSites, money+1), dtype=int)


for i in range(f.shape[0]):
    for j in range(0, f.shape[1]):
        f[i][j] = probArray[i] * initialTable[i][j]
      
for i in range(int(f.shape[0]/2)):
    f[[f.shape[0]-i-1, i],:] = f[[i, f.shape[0]-i-1], :]

#fill in last stage of the return and decision tables
for j in range(returnTable.shape[1]):
    returnTable[0][j] = f[0][j]
    decisionTable[0][j] = j

for i in range(1, returnTable.shape[0]):
    for j in range(1, returnTable.shape[1]):
        tempMax = -1 * sys.maxsize
        tempK = -1
        for k in range(j+1):
            if f[i][k] + returnTable[i-1][j-k] > tempMax:
                tempMax = f[i][k] + returnTable[i-1][j-k]
                tempK = k
        returnTable[i][j] = tempMax
        decisionTable[i][j] = tempK

for i in range(int(decisionTable.shape[0]/2)):
    decisionTable[[decisionTable.shape[0]-i-1, i],:] = decisionTable[[i, decisionTable.shape[0]-i-1], :]
    returnTable[[returnTable.shape[0]-i-1, i],:] = returnTable[[i, returnTable.shape[0]-i-1], :]


allocation = np.zeros((numOfSites), dtype=int)
maxReturn = returnTable[0][returnTable.shape[1]-1]
allocation[0] = decisionTable[0][decisionTable.shape[1]-1]

for i in range(1, allocation.shape[0]):
    index = money - sum(allocation)
    allocation[i] = decisionTable[i][index]
    
print('\nThe maximum return is', maxReturn)
print('This is possible with the following allocations')
for i in range(allocation.shape[0]):
    print('Site', i+1, 'should recieve', allocation[i], 'units of money')

'''
:::output for problem 19.31:::
    
How many sites can be developed? 3

How many units of money are at our disposal? 8
Now we will create our initial table

Input the probability of finding oil, if it exists, with the amount of money allocated to that site
Site 1

0 money allocated:0

1 money allocated:0

2 money allocated:.1

3 money allocated:.2

4 money allocated:.3

5 money allocated:.5

6 money allocated:.7

7 money allocated:.9

8 money allocated:1
~~~~~~~~~~~~~~~

Site 2

0 money allocated:0

1 money allocated:.1

2 money allocated:.2

3 money allocated:.3

4 money allocated:.4

5 money allocated:.6

6 money allocated:.7

7 money allocated:.8

8 money allocated:1
~~~~~~~~~~~~~~~

Site 3

0 money allocated:0

1 money allocated:.1

2 money allocated:.1

3 money allocated:.2

4 money allocated:.3

5 money allocated:.5

6 money allocated:.8

7 money allocated:.9

8 money allocated:1
~~~~~~~~~~~~~~~

Now enter the probability that oil exists at each site

Site 1: .4

Site 2: .3

Site 3: .2



The following table displays the probability of finding oil at each site if it exists

		|	0 	|	1 	|	2 	|	3 	|	4 	|	5 	|	6 	|	7 	|	8 	|	
________________________________________________________________________________
Site 1 	|	0.0 	0.0 	0.1 	0.2 	0.3 	0.5 	0.7 	0.9 	1.0 	
Site 2 	|	0.0 	0.1 	0.2 	0.3 	0.4 	0.6 	0.7 	0.8 	1.0 	
Site 3 	|	0.0 	0.1 	0.1 	0.2 	0.3 	0.5 	0.8 	0.9 	1.0 	

The maximum return is 0.4
This is possible with the following allocations
Site 1 should recieve 8 units of money
Site 2 should recieve 0 units of money
Site 3 should recieve 0 units of money
'''