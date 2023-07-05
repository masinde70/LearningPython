def sunsetViews(buildings, direction):
    candidateBuildings = []

    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1

    idx = startIdx
    while idx > 0 and idx < len(buildings):
        buildingHeight = buildings[idx]
        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            candidateBuildings.pop()

        candidateBuildings.append(idx)

        idx += step

    if direction == "WEST":
        

