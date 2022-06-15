import heapq
from queue import PriorityQueue

# variable that hold the output string
outputString=""
heuristicValue={'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsowa': 151, 'Lasi': 226, 
'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

# queue that hold path from source city to distination city
class priorityQueue:
    def __init__(self):
        self.cities = []
    # add to queue
    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    # get from queue
    def pop(self):
        return heapq.heappop(self.cities)[1]
    # check if empty
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

# node class, hold city and distance
class countryNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

# save mapDict map dict
mapDict = {}

def saveCountry(cities):
    for string in cities.split('\n'):
        value = string.split(' ')
        ct1 = value[0]
        ct2 = value[1]
        distinationValue = int(value[2])
        mapDict.setdefault(ct1, []).append(countryNode(ct2, distinationValue))
        mapDict.setdefault(ct2, []).append(countryNode(ct1, distinationValue))
    return mapDict

# save Straight line
def saveStraightLine(valuse):
    global heuristicValue
    h = {}
    for value in valuse.split('\n'):
        value = value.strip().split(" ")
        node = value[0].strip()
        temp = int(value[1].strip())
        h[node] = temp
    heuristicValue=h
    print(heuristicValue)
    return h


def heuristic(node, values):
    return values[node]

# algorithm function
def algorithmFunction(start, end):
    global heuristicValue
    path = {}
    distance = {}
    pathQueue = priorityQueue()
    
    h = heuristicValue
    
    # add start city to queue
    pathQueue.push(start, 0)
    # distance start with 0
    distance[start] = 0
    path[start] = None
    citiesList = []
    # add to queue and calcluate cost and distance 
    while (pathQueue.isEmpty() == False):
        current = pathQueue.pop()
        citiesList.append(current)

        if (current == end):
            break

        for new in mapDict[current]:
            g = distance[current] + int(new.distance)
            if (new.city not in distance or g < distance[new.city]):
                distance[new.city] = g
                f = g + heuristic(new.city, h)
                pathQueue.push(new.city, f)
                path[new.city] = current

    savePath(start, end, path, distance, citiesList)

# make output of path
def savePath(start, end, path, distance, expandedlist):
    global outputString
    bestRoute = []
    i = end
    # loop over queue to get optimal path
    while (path.get(i) != None):
        bestRoute.append(i)
        i = path[i]
    bestRoute.append(start)
    bestRoute.reverse()
    
    outputString+="Path : " + " ->> ".join(bestRoute)
    outputString+="\n\nCost : " + str(distance[end]) +"\n"
    print(outputString)

# search route between start and goal
def searchMap(start,goal):
    global outputString
    global mapDict
    if not bool(mapDict):
        initFunction()
    outputString=""
    if not goal:
        goal="Bucharest"
    print(goal)
    # if cities not in the country
    if start not in mapDict :
        outputString= 'ERROR CITY'
        return outputString 
    else:
        algorithmFunction(start, goal)
        # get output
        return outputString


# ADD NEW MAP
def addMap(graphSet,st):
    # Fetch global variables
    global mapDict
    global heuristicValue
    try:
        mapDict={}
        # intialize mapDict dictionary
        mapDict= saveCountry(graphSet)
        # intialize heuristiv values
        heuristicValue=saveStraightLine(st)
        return "country added successfully"
    except:
        initFunction()
        return "Data not same as expected"
    
#init data for first run 
def initFunction():
    global mapDict
    global heuristicValue
    mapDict={}
    heuristicValue ={
                    'Arad': 366,
                    'Zerind': 374,
                    'Oradea': 380,
                    'Sibiu':  253,
                    'Fagaras':176,
                    'Rimnicu_Vilcea': 193,
                    'Timisoara': 329,
                    'Lugoj': 244,
                    'Mehadia': 241,
                    'Dobreta': 242,
                    'Pitesti':100,
                    'Craiova':160,
                    'Bucharest':0,
                    'Giurgiu':77,
                    'Urziceni': 80,
                    'Vaslui':199,
                    'Iasi':226,
                    'Neamt':234,
                    'Hirsova':151,
                    'Eforie':161
                    }
    str = "Arad Sibiu 140\nArad Timisoara 118\nArad Zerind 75\nBucharest Fagaras 211\nBucharest Giurgiu 90\nBucharest Pitesti 101\nBucharest Urziceni 85\nCraiova Dobreta 120\nCraiova Pitesti 138\nCraiova Rimnicu_Vilcea 146\nDobreta Mehadia 75\nEforie Hirsova 86\nFagaras Sibiu 99\nHirsova Urziceni 98\nIasi Neamt 87\nIasi Vaslui 92\nLugoj Mehadia 70\nLugoj Timisoara 111\nOradea Zerind 71\nOradea Sibiu 151\nPitesti Rimnicu_Vilcea 97\nRimnicu_Vilcea Sibiu 80\nUrziceni Vaslui 142" 
    
    mapDict= saveCountry(str)
    
    return "Reset mapDict map successfully"

def getH():
    global heuristicValue
    print(heuristicValue)
    return heuristicValue