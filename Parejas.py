def min_swaps_to_adjacent(row):
    swaps = 0
    position = {x: i for i, x in enumerate(row)}
    for i in range(0, len(row), 2):
        expected_partner = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
        partner_index = position[expected_partner]
        if partner_index != i + 1:
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            position[row[partner_index]] = partner_index
            position[row[i + 1]] = i + 1
            swaps += 1
    return swaps