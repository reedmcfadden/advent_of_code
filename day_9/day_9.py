#!/usr/bin/env python3

def main():
    lines = open("./day_9/day_9.txt").read().splitlines()
    cityAdjacencyList = {}
    for line in lines:
        tokens = line.split(" ")
        source = tokens[0]
        dest = tokens[2]
        distance = int(tokens[4])
        if source not in cityAdjacencyList:
            cityAdjacencyList[source] = {}
        if dest not in cityAdjacencyList:
            cityAdjacencyList[dest] = {}
        cityAdjacencyList[source][dest] = distance
        cityAdjacencyList[dest][source] = distance

    global shortestPath
    global shortestPathDistance
    global longestPath
    global longestPathDistance
    shortestPath = None
    shortestPathDistance = None
    longestPath = None
    longestPathDistance = None
    for source in cityAdjacencyList:
        visited = set()
        visited.add(source)
        path = [source]
        distance = 0
        findShortestAndLongestPath(cityAdjacencyList, source, visited, path, distance)

    print(f"Part 1:")
    print(f"shortestPath: {shortestPath}")
    print(f"shortestPathDistance: {shortestPathDistance}")
    print()
    print(f"Part 2:")
    print(f"longestPath: {longestPath}")
    print(f"longestPathDistance: {longestPathDistance}")


def findShortestAndLongestPath(cityAdjacencyList, source, visited, path, distance):
    global shortestPath
    global shortestPathDistance
    global longestPath
    global longestPathDistance
    if len(visited) == len(cityAdjacencyList):
        # Part 1
        if shortestPathDistance is None or distance < shortestPathDistance:
            shortestPath = path.copy()
            shortestPathDistance = distance
        # Part 2
        if longestPathDistance is None or distance > longestPathDistance:
            longestPath = path.copy()
            longestPathDistance = distance
        return

    for dest in cityAdjacencyList[source]:
        if dest not in visited:
            visited.add(dest)
            path.append(dest)
            distance += cityAdjacencyList[source][dest]
            findShortestAndLongestPath(cityAdjacencyList, dest, visited, path, distance)
            visited.remove(dest)
            path.pop()
            distance -= cityAdjacencyList[source][dest]


if __name__ == "__main__":
    main()