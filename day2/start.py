from collections import Counter

with open('input', 'r') as input: 
    boxes = input.read().splitlines()
    
    def calculate_difference_of_occurrences(boxes): 
        ufta = '' 
        for box in boxes:
            letter_counter = Counter(box)
            # remove all single occurred letters
            filtered_counter = { k:str(v) for k,v in letter_counter.items() if v > 1 }
            # remove all duplicated items, sort it, and join values to str
            ufta  += ''.join(list(set(filtered_counter.values())))
        occurrences = Counter(ufta)
        print('Part 1: ', occurrences['2'] * occurrences['3'])
        
    calculate_difference_of_occurrences(boxes)

    def found_equality_by_one_letter(boxes): 
        for box_a in boxes: 
            boxes_b = list(boxes)
            boxes_b.remove(box_a)
            for box_b in boxes_b: 
                diff_counter = 0
                found = False
                for i in range(0, len(box_a)):  # 26
                    if box_a[i] != box_b[i]: 
                        diff_counter += 1
                    elif diff_counter > 1: 
                        break
                    elif i == len(box_a) - 1:
                        found = True
                if found: 
                    diff = ''
                    for i, letter in enumerate(box_a): 
                        if letter == box_b[i]: 
                            diff += letter
                    print('Part 2:', diff)
                    return 
    
    found_equality_by_one_letter(boxes)
                