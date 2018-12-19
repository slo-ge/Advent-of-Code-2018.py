from datetime import datetime

with open('input', 'r') as input:
    polymer = input.read()
    start_time = datetime.now()


    def react(polymer):
        found = True
        while found:
            found = False
            for c in range(97, 123):
                letter = chr(c)
                letter_u = letter.upper()
                c1 = letter + letter_u
                c2 = c1[::-1]

                if c1 in polymer or c2 in polymer:
                    polymer = polymer.replace(c1, '').replace(c2, '')
                    found = True
        return polymer


    print("Part 1: ", len(react(polymer)))  # 0:00:00.115975
    print("Part 1-Time:", datetime.now() - start_time)

    start_time = datetime.now()
    most_short = polymer

    for c in range(97, 123):
        letter = chr(c)
        letter_u = letter.upper()
        most_short_candidate = react(polymer.replace(letter, '').replace(letter_u, ''))
        if len(most_short_candidate) < len(most_short):
            most_short = most_short_candidate

    print("Part 2: ", len(react(most_short)))
    print("Part 2-Time", datetime.now() - start_time)
