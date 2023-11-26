def min_swaps_to_adjacent(row):
    swaps = 0
    posicion = {x: i for i, x in enumerate(row)}
    for i in range(0, len(row), 2):
        expected_pareja = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
        pareja_index = posicion[expected_pareja]
        if pareja_index != i + 1:
            row[i + 1], row[pareja_index] = row[pareja_index], row[i + 1]
            posicion[row[pareja_index]] = pareja_index
            posicion[row[i + 1]] = i + 1
            swaps += 1
    return swaps