from typing import List, Tuple, Set, Dict
from collections import defaultdict

class Region:
    type: str
    plots: Set[Tuple[int, int]]
    perimeter: int
    sides: int

    def __init__(self, type, startIndex):
        self.type = type
        self.plots = set([startIndex])
        self.perimeter = 0
        self.sides = 0

    def contains(self, index: Tuple[int, int]):
        return index in self.plots

    def area(self):
        return len(self.plots)

    def __str__(self):
        return f'[type={self.type}, area={len(self.plots)}, perimeter={self.perimeter}, sides={self.sides}, plots={self.plots}]'

    def __repr__(self):
        return self.__str__()

def readFile(fileName):
    lines: List[List[str]] = []
    with open(fileName, "r") as file:
        for line in file:
            lines.append([c for c in line.strip()])

    return lines

def isInnerPoint(map, point):
    return point[1] >= 0 and point[1] < len(map) and point[0] >= 0 and point[0] < len(map[0])

def getSides(type, map ,index):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    sides = set()
    for direction in directions:
        newIndex = (index[0] + direction[0], index[1] + direction[1])

        if not isInnerPoint(map, newIndex) or map[newIndex[1]][newIndex[0]] != type:
            sides.add(direction)

    return sides

def plotRegion(region: Region, map, index):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    sides = getSides(region.type, map, index)
    region.perimeter += len(sides)
    region.sides += len(sides)

    neighbors = [d for d in directions if d not in sides]
    for direction in neighbors:
        newIndex = (index[0] + direction[0], index[1] + direction[1])
        if region.contains(newIndex):
            neighborSides = getSides(region.type, map, newIndex)
            region.sides -= len(sides.intersection(neighborSides))

    for direction in neighbors:
        newIndex = (index[0] + direction[0], index[1] + direction[1])
        if not region.contains(newIndex):
            region.plots.add(newIndex)
            plotRegion(region, map, newIndex)

def calculateCost(regions: Dict[str, List[Region]]):
    fullCost = 0
    discountCost = 0
    for _, regionType in regions.items():
        for region in regionType:
            fullCost += region.area() * region.perimeter
            discountCost += region.area() * region.sides

    return (fullCost, discountCost)

def main():
    map = readFile('data_files/data_day12.txt')

    regions: Dict[str, List[Region]] = defaultdict(list)

    for y in range(len(map)):
        for x in range(len(map[y])):
            plotType = map[y][x]

            plotRegions = regions.get(plotType)
            if plotRegions is None or next((r for r in plotRegions if r.contains((x, y))), None) is None:
                newRegion = Region(plotType, (x, y))
                regions[plotType].append(newRegion)
                plotRegion(newRegion, map, (x, y))
                #print(newRegion)

    fullCost, discountCost = calculateCost(regions)
    print("[Part 1] Total fencing cost:", fullCost)
    print("[Part 2] Discounted fencing cost:", discountCost)

if __name__ == "__main__":
    main()