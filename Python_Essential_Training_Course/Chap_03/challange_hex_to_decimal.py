hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def hex_to_decimal(hexnum):
    for i in hexnum:
        if i not in hexNumbers:
            return None

        if len(hexnum) == 3:
            return hexNumbers[hexnum[0]] * 256 + hexNumbers[hexnum[1]] * 16 + hexNumbers[hexnum[2]]

        if len(hexnum) == 2:
            return hexNumbers[hexnum[0]] * 16 + hexNumbers[hexnum[1]]

        if len(hexnum) == 1:
            return hexNumbers[hexnum[0]]


print(hex_to_decimal('2A4'))

