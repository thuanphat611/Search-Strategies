import timeit

#----------------------------------------------------------------
def readFile(maze, path):#'./Input/input.txt'
    global size, start, end
    f = open(path, 'r')

    size = int(f.readline())
    goal = [int (x) for x in f.readline().strip().split(' ')]
    start = goal[0]
    end = goal[1]
    adjacencyList = f.read().split('\n')

    f.close()
    index = 0

    for i in adjacencyList:
        if (i):
            maze[index] = [int(x) for x in i.strip().split(' ')]
        else:
            maze[index] = []
        index += 1
#----------------------------------------------------------------
def traceBack(visited, solution, start):
    if (visited[start] == None):
        solution.insert(0, start)
    else:
        solution.insert(0, start)
        traceBack(visited, solution, visited[int(start)])
#----------------------------------------------------------------
def dfs_algorithm(trace, maze, current, goal, parent = None):
    global goalReached  
    if (not current in trace and not goalReached): #not visited and not reach goal
        print(current, end = ' ')
        trace[current] = parent
        if (current == goal):
            goalReached = True
        if not goalReached:
            for neighbour in maze[current]:
                dfs_algorithm(trace, maze, neighbour, goal, current)

def depthFirstSearch(maze, size, start, end):
    if (start < 0 or end < 0 or start > (size - 1) or end > (size - 1)):
        print('invalid parameters')
        return 

    global goalReached
    goalReached = False
    trace = {}
    solution = []

    print('Node explore:', end = ' ')
    startTime = timeit.default_timer()
    dfs_algorithm(trace, maze, start, end)
    endTime = timeit.default_timer()
    print() #newline
    if not goalReached:
        print('Solution not found')
    else:
        traceBack(trace, solution, end)
        print('Solution:', end = ' ')
        for i in solution:
            print(i, end = ' ')
        print() #newline
        runTime = endTime - startTime 
        print('Time to escape:', runTime * 1000, 'ms')
#-----------------------------------------------------------------
def breadthFirstSearch(maze, size, start, end):
    if (start < 0 or end < 0 or start > (size - 1) or end > (size - 1)):
            print('invalid parameters')
            return 
        
    global goalReached
    goalReached = False
    trace = {}
    solution = []
    frontier = []
    visited = []

    frontier.append(start)
    trace[start] = None
    
    print('Node explore:', end = ' ')
    startTime = timeit.default_timer()
    while (True):
        if not frontier: #check if there are any nodes in frontier
            break

        node = frontier.pop(0)
        visited.append(node)
        print(node, end = ' ')

        if (node == end):
            goalReached = True
            break

        for child in maze[node]:
            if (not child in visited and not child in frontier):
                frontier.append(child)
                trace[int(child)] = node #assign parent be4 adding to frontier (for traceBack)
    endTime = timeit.default_timer()
    print()#newline
    if not goalReached:
        print('Solution not found')
    else:
        traceBack(trace, solution, end)
        print('Solution:', end = ' ')
        for i in solution:
            print(i, end = ' ')
        print()#newline
        runTime = endTime - startTime 
        print('Time to escape:', runTime * 1000, 'ms')
#----------------------------------------------------------------
def uniformCostSearch(maze, size, start, end):
    if (start < 0 or end < 0 or start > (size - 1) or end > (size - 1)):
            print('invalid parameters')
            return 
        
    global goalReached
    goalReached = False
    trace = {}
    solution = []
    frontier = {}
    visited = []

    frontier[start] = 0
    trace[start] = None
    
    print('Node explore:', end = ' ')
    startTime = timeit.default_timer()
    while (True):
        if not frontier: #check if there are any nodes in frontier
            break

        nodeName = list(frontier.keys())[0] #get the firt node name and cost
        nodeCost = list(frontier.values())[0]

        for n in frontier:#find the lowest cost node
            if (frontier[n] < nodeCost):
                nodeName = n
                nodeCost = frontier[n]

        frontier.pop(nodeName)
        visited.append(nodeName)
        print(nodeName, end = ' ')
        
        if (nodeName == end):
            goalReached = True
            break

        for child in maze[nodeName]:
            childCost = nodeCost + 1
            if (not child in visited and not child in frontier):
                trace[int(child)] = nodeName
                frontier[child] = childCost
            elif (not child in visited and child in frontier and childCost < frontier[child]):
                trace[int(child)] = nodeName
                frontier[child] = childCost
    endTime = timeit.default_timer()
    print()#newline
    if not goalReached:
        print('Solution not found')
    else:
        traceBack(trace, solution, end)
        print('Solution:', end = ' ')
        for i in solution:
            print(i, end = ' ')
        print()#newline
        runTime = endTime - startTime 
        print('Time to escape:', runTime * 1000, 'ms')
#----------------------------------------------------------------
def geedyBestFirstSearch(maze, size, start, end):
    if (start < 0 or end < 0 or start > (size - 1) or end > (size - 1)):
            print('invalid parameters')
            return 
        
    global goalReached
    goalReached = False
    trace = {}
    solution = []
    frontier = {}
    visited = []

    frontier[start] = abs(end // 10 - start // 10) + abs(end % 10 - start % 10)#manhattan distance
    trace[int(start)] = None
    
    print('Node explore:', end = ' ')
    startTime = timeit.default_timer()
    while (True):
        if not frontier: #check if there are any nodes in frontier
            break

        nodeName = list(frontier.keys())[0] #get the firt node name and cost
        nodeCost = list(frontier.values())[0]

        for n in frontier:#find the lowest cost node
            if (frontier[n] < nodeCost):
                nodeName = n
                nodeCost = frontier[n]

        frontier.pop(nodeName)
        visited.append(nodeName)
        print(nodeName, end = ' ')

        if (nodeName == end):
            goalReached = True
            break

        for child in maze[nodeName]:
            childCost = abs(end // 10 - child // 10) + abs(end % 10 - child % 10)
            if (not child in visited and not child in frontier):
                trace[int(child)] = nodeName
                frontier[child] = childCost
    endTime = timeit.default_timer()
    print()#newline
    if not goalReached:
        print('Solution not found')
    else:
        traceBack(trace, solution, end)
        print('Solution:', end = ' ')
        for i in solution:
            print(i, end = ' ')
        print()#newline
        runTime = endTime - startTime 
        print('Time to escape:', runTime * 1000, 'ms')
#----------------------------------------------------------------
def aStarSearch(maze, size, start, end):
    if (start < 0 or end < 0 or start > (size - 1) or end > (size - 1)):
            print('invalid parameters')
            return 
        
    global goalReached
    goalReached = False
    trace = {}
    solution = []
    frontier = {}
    visited = []

    frontier[start] = abs(end // 10 - start // 10) + abs(end % 10 - start % 10)#manhattan distance
    trace[int(start)] = None
    
    print('Node explore:', end = ' ')
    startTime = timeit.default_timer()
    while (True):
        if not frontier: #check if there are any nodes in frontier
            break

        nodeName = list(frontier.keys())[0] #get the firt node name and cost
        nodeCost = list(frontier.values())[0]

        for n in frontier:#find the lowest cost node
            if (frontier[n] < nodeCost):
                nodeName = n
                nodeCost = frontier[n]

        frontier.pop(nodeName)
        visited.append(nodeName)
        print(nodeName, end = ' ')

        if (nodeName == end):
            goalReached = True
            break

        for child in maze[nodeName]:
            childCost = nodeCost - abs(end // 10 - start // 10) - abs(end % 10 - start % 10) + 1 + abs(end // 10 - child // 10) + abs(end % 10 - child % 10)
            if (not child in visited and not child in frontier):
                trace[int(child)] = nodeName
                frontier[child] = childCost
            elif (not child in visited and child in frontier and childCost < frontier[child]):
                trace[int(child)] = nodeName
                frontier[child] = childCost
    endTime = timeit.default_timer()      
    print()#newline
    if not goalReached:
        print('Solution not found')
    else:
        traceBack(trace, solution, end)
        print('Solution:', end = ' ')
        for i in solution:
            print(i, end = ' ')
        print()#newline
        runTime = endTime - startTime 
        print('Time to escape:', runTime * 1000, 'ms')
#----------------------------------------------------------------
size = 0
start = 0
end = 0
maze = {}

readFile(maze, './Input/input.txt')

print('Depth-first Search:')
depthFirstSearch(maze, size, start, end)

print('Breadth-first Search:')
breadthFirstSearch(maze, size, start, end)

print('Uniform-cost Search:')
uniformCostSearch(maze, size, start, end)

print('Geedy Best First Search:')
geedyBestFirstSearch(maze, size, start, end)

print('A* Search:')
aStarSearch(maze, size, start, end)