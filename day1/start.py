with open('input', 'r') as input: 
    list_values = [int(value) for value in input.read().splitlines()]
    # Part 1
    print("Part 1:", sum(list_values))

    # Part 2
    found = False
    temp = {}
    cum_sum = 0 
    while not found: 
        for item in list_values: 
            if cum_sum in temp: 
                print("Part 2:", cum_sum)
                found = True
                break
            else: 
                temp[cum_sum] = True
            cum_sum += item
