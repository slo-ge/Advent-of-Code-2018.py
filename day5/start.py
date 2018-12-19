with open('input', 'r') as input:
    polymer = input.read()


    def react(polymer):
        found = True
        while found:
            found = False
            for c in range(97, 123):
                c1 = chr(c) + chr(c).upper()
                c2 = c1[::-1]
                if c1 in polymer or c2 in polymer:
                    polymer = polymer.replace(c1, '').replace(c2, '')
                    found = True
        return polymer


    print("Part 1: ", len(react(polymer)))  # 0:00:00.115975

    most_short = min([react(polymer.replace(chr(c), '').replace(chr(c).upper(), ''))
                      for c in range(97, 123)], key=len)

    print("Part 2: ", len(react(most_short)))
