def sunsetView(buildings, direction):
    result = []
    n = len(buildings)
    maxValue = 0

    for idx in range(n - 1, -1,-1) if direction == 'EAST' else range(0, n, 1):
        if buildings[idx] > maxValue:
            maxValue = buildings[idx]
            result.append(idx)
    return result[::-1] if direction == 'EAST' else result