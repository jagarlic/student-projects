# PROBLEM 1

def sumOfMultiples(upper):
    upper = upper - 1
    sum = 0
    while (upper >= 3):
        if (upper % 3 == 0 or upper % 5 == 0):
            sum = sum + upper
        upper = upper - 1
    return sum

print(sumOfMultiples(10));

# PROBLEM 2

def recursiveFib(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return recursiveFib(num-1)+recursiveFib(num-2)

print(recursiveFib(10))

def iterativeFib(num):
    if(num == 0):
        return 0
    if(num == 1 or num == 2):
        return 1

    temp1 = 1
    temp2 = 1

    for x in range(3, num):
        temp3 = temp2
        temp2 = temp2 + temp1
        temp1 = temp3

    return temp1 + temp2

print(iterativeFib(10))

# PROBLEM 3

def f(x):
    return 2 * (x ** 3)

def g(c):
    return 4 * (c ** 2) + 3

def t(d):
    return (d ** 4) + 15 * d

def deriv(f, x):
    return (f(x + .01) - f(x))/.01

print(deriv(g, 5))
print(deriv(f, 5))
print(deriv(t, 3))

# PROBLEM 4

def matrixMultiply(m1, m2):
    rowsm1 = len(m1)
    colsm1 = len(m1[0])
    rowsm2 = len(m2)
    colsm2 = len(m2[0])

    if (colsm1 != rowsm2):
        return 'Invalid input'

    m3 = [[0 for r in range(colsm2)] for c in range(rowsm1)]

    for x in range(rowsm1):
        for r in range(colsm2):
            for i in range(colsm1):
                m3[x][r] += m1[x][i] * m2[i][r]

    return m3

print(matrixMultiply([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))

# PROBLEM 5

def levenshteinDistance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    result = min([levenshteinDistance(s1[:-1], s2)+1,
               levenshteinDistance(s1, s2[:-1])+1,
               levenshteinDistance(s1[:-1], s2[:-1]) + cost])

    return result

print(levenshteinDistance("doggo", "datboi"))
