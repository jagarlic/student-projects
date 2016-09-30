def makeNode(state, parent, depth, pathCost):
    return [state, parent, depth, pathCost]

def makeState(nw, n, ne, w, c, e, sw, s, se):
    state=[]
    for row in range(3):
        state.append([])
    state[0].append(nw)
    state[0].append(n)
    state[0].append(ne)
    state[1].append(w)
    state[1].append(c)
    state[1].append(e)
    state[2].append(sw)
    state[2].append(s)
    state[2].append(se)
    return(state)

def moveLeft(state):
    if (state == None):
        return None
    newState = []
    for row in range(3):
        for col in range(3):
            newState.append(state[row][col])
    index = newState.index(0)
    if index not in [0, 3, 6]:
        temp = newState[index - 1]
        newState[index - 1] = newState[index]
        newState[index] = temp
        return makeState(
            newState[0], newState[1], newState[2],
            newState[3], newState[4], newState[5],
            newState[6], newState[7], newState[8])
    else:
        return None

def moveRight(state):
    if (state == None):
        return None
    newState = []
    for row in range(3):
        for col in range(3):
            newState.append(state[row][col])
    index = newState.index(0)
    if index not in [2, 5, 8]:
        temp = newState[index + 1]
        newState[index + 1] = newState[index]
        newState[index] = temp
        return makeState(
            newState[0], newState[1], newState[2],
            newState[3], newState[4], newState[5],
            newState[6], newState[7], newState[8])
    else:
        return None

def moveUp(state):
    if (state == None):
        return None
    newState = []
    for row in range(3):
        for col in range(3):
            newState.append(state[row][col])
    index = newState.index(0)
    if index not in [0, 1, 2]:
        temp = newState[index - 3]
        newState[index - 3] = newState[index]
        newState[index] = temp
        return makeState(
            newState[0], newState[1], newState[2],
            newState[3], newState[4], newState[5],
            newState[6], newState[7], newState[8])
    else:
        return None

def moveDown(state):
    if (state == None):
        return None
    newState = []
    for row in range(3):
        for col in range(3):
            newState.append(state[row][col])
    index = newState.index(0)
    if index not in [6, 7, 8]:
        temp = newState[index + 3]
        newState[index + 3] = newState[index]
        newState[index] = temp
        return makeState(
            newState[0], newState[1], newState[2],
            newState[3], newState[4], newState[5],
            newState[6], newState[7], newState[8])
    else:
        return None

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

explored = []

def testProcedure(current):
    for node in current:
        if node == None:
            return False
        if node == goalState:
            return True
        else:
            explored.append(current[0])
            return False

def expandProcedure(current, queue):
    if (moveLeft(current[0]) != None):
        if (moveLeft(current[0]) not in explored):
            left = makeNode(moveLeft(current[0]), current, current[2]+1, current[3]+1)
            queue.insert(0, left)
    if (moveUp(current[0]) != None):
        if (moveUp(current[0]) not in explored):
            up = makeNode(moveUp(current[0]), current, current[2]+1, current[3]+1)
            queue.insert(0, up)
    if (moveDown(current[0]) != None):
        if (moveDown(current[0]) not in explored):
            down = makeNode(moveDown(current[0]), current, current[2]+1, current[3]+1)
            queue.insert(0, down)
    if (moveRight(current[0]) != None):
        if (moveRight(current[0]) not in explored):
            right = makeNode(moveRight(current[0]), current, current[2]+1, current[3]+1)
            queue.insert(0, right)
    return queue

def outputProcedure(numRuns, goal):
    for row in range(3):
        print(goalState[row])
    print('\n')
    while True:
        if(goal[1] == None):
            print("The program ran " + str(numRuns) + " times")
            break
        for row in range(3):
            print(goal[1][0][row])
        print('\n')
        goal = goal[1]

def uninformedSearch(queue, limit, numRuns):
    if len(queue) == 0:
        return False
    elif testProcedure(queue[0]):
        outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print("Limit Reached")
    else:
        limit = limit -1
        numRuns = numRuns + 1
        uninformedSearch(expandProcedure(queue[0], queue[1:len(queue)]), limit, numRuns)

def distances(matrix, goal):
# Calculates how far each tile is from its goal state, and sums those distances
    sum = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(matrix)):
                for l in range(0, len(matrix)):
                    if matrix[k][l] == tile:
                        sum += (k - i) * (k - i) + (j - l) * (j - l)
    return sum

def expandProcedureWithdistance(current, queue):
    rightDistance = 10000
    leftDistance = 10000
    upDistance = 10000
    downDistance = 10000

    if (moveUp(current[0]) != None):
        if (moveUp(current[0]) not in explored):
            upDistance = distances(moveUp(current[0]), goalState)
    if (moveDown(current[0]) != None):
        if (moveDown(current[0]) not in explored):
            downDistance = distances(moveDown(current[0]), goalState)
    if (moveRight(current[0]) != None):
        if (moveRight(current[0]) not in explored):
            rightDistance = distances(moveRight(current[0]), goalState)
    if (moveLeft(current[0]) != None):
        if (moveUp(current[0]) not in explored):
            leftDistance = distances(moveLeft(current[0]), goalState)

    smallest = min(upDistance, downDistance, rightDistance, leftDistance)

    if (smallest == upDistance):
        up = makeNode(moveUp(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, up)
    elif (smallest == downDistance):
        down = makeNode(moveDown(current[0]), current, current[2]+1, current[3]+ 1)
        queue.insert(0, down)
    elif (smallest == leftDistance):
        left = makeNode(moveLeft(current[0]), current, current[2] + 1, current[3] + 1)
        queue.insert(0, left)
    else:
        right = makeNode(moveRight(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, right)
    return queue

def misplacedTiles(current, goal):
    #returns the number of tiles that are not in their correct place
    count = 0
    i = 1
    for row in range(3):
        for col in range(3):
            if current[row][col] != goal[row][col]:
                count+=1
    return count - 1

def expandProcedureWithmispalced(current, queue):
    leftMisplacedTiles = 10000
    rightMisplacedTiles = 10000
    upMisplacedTiles = 10000
    downMisplacedTiles = 10000
    if (moveLeft(current[0]) != None):
        if (moveLeft(current[0]) not in explored):
            leftMisplacedTiles = misplacedTiles(moveLeft(current[0]), goalState)
    if (moveUp(current[0]) != None):
        if (moveUp(current[0]) not in explored):
            upMisplacedTiles = misplacedTiles(moveUp(current[0]), goalState)
    if (moveDown(current[0]) != None):
        if (moveDown(current[0]) not in explored):
            downMisplacedTiles = misplacedTiles(moveDown(current[0]), goalState)
    if (moveRight(current[0]) != None):
        if (moveRight(current[0]) not in explored):
            rightMisplacedTiles = misplacedTiles(moveRight(current[0]), goalState)

    smallest = min(upMisplacedTiles, downMisplacedTiles, rightMisplacedTiles, leftMisplacedTiles)

    if (smallest == upMisplacedTiles):
        up = makeNode(moveUp(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, up)
    elif (smallest == downMisplacedTiles):
        down = makeNode(moveDown(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, down)
    elif (smallest == leftMisplacedTiles):
        left = makeNode(moveLeft(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, left)
    elif (smallest == rightMisplacedTiles):
        right = makeNode(moveRight(current[0]), current, current[2]+1, current[3]+1)
        queue.insert(0, right)
    return queue

def informedSearchMisplaced(queue, limit, numRuns):
    if len(queue) == 0:
        return False
    elif testProcedure(queue[0]):
        return outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print "Limit Reached"
    else:
        limit = limit -1
        numRuns = numRuns + 1
        informedSearchMisplaced(expandProcedureWithmispalced(queue[0], queue[1:len(queue)]), limit, numRuns)

def informedSearchDistance(queue, limit, numRuns):
    if len(queue) == 0:
        return False
    elif testProcedure(queue[0]):
        return outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print "Limit Reached"
    else:
        limit = limit -1
        numRuns = numRuns + 1
        informedSearchDistance(expandProcedureWithdistance(queue[0], queue[1:len(queue)]), limit, numRuns)

def testUninformedSearch(init, goal, limit):
    rootNode = makeNode(init, None, 0, 0)
    startQueue = [rootNode]
    uninformedSearch(startQueue, limit, 0)

def testInformedSearchMisplaced(init, goal, limit):
    rootNode = makeNode(init, None, 0, 0)
    startQueue = [rootNode]
    informedSearchMisplaced(startQueue, limit, 0)

def testInformedSearchDistance(init, goal, limit):
    rootNode = makeNode(init, None, 0, 0)
    startQueue = [rootNode]
    print(informedSearchDistance(startQueue, limit, 0))

initialState = makeState(1, 2, 3, 4, 5, 6, 0, 7, 8)
goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, 0)
testUninformedSearch(initialState, goalState, 1000)
#testInformedSearchDistance(initialState, goalState, 2000)
#testInformedSearchMisplaced(initialState, goalState, 2000)
