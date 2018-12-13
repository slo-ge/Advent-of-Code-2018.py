with open('input', 'r') as input:
    claims = input.read().splitlines()  # claim = anspruch
    matrix_size = 1000
    square = [['.' for x in range(matrix_size)] for y in range(matrix_size)]


    def split_values(claim):
        claim = claim.replace(' ', '')
        cid, coords = claim.split('@')
        xy, size = coords.split(':')
        return xy.split(',') + size.split('x') + [cid]


    def count_overlaps(claim, matrix, overlaps):
        x, y, w, h, cid = split_values(claim)
        for wpy in range(0, int(h)):
            for wpx in range(0, int(w)):
                y_real = wpy + int(y)
                x_real = wpx + int(x)
                px = matrix[y_real][x_real]
                if px == '.':
                    matrix[y_real][x_real] = cid
                elif px == 'X':
                    continue
                else:
                    matrix[y_real][x_real] = 'X'
                    overlaps += 1
        return overlaps


    counter = 0
    for item in claims:
        counter = count_overlaps(item, square, counter)

    print('Part 1:', counter)

    for item in claims:
        x, y, w, h, cid = split_values(item)
        skip = False
        for wpy in range(0, int(h)):
            for wpx in range(0, int(w)):
                px = square[wpy + int(y)][wpx + int(x)]
                if px == 'X':
                    skip = True
                    break
            if skip:
                break
        if not skip:
            print('Part 2: ', cid[1:])
