def sunsetViews(buildings, direction):
    candidateBuildings = []

    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    
