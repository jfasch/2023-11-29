def uniq_conservative(seq):
    seen = set()
    out = []
    for elem in seq:
        if elem not in seen:
            out.append(elem)
            seen.add(elem)
    return out

def uniq_generator(seq):
    seen = set()

    for elem in seq:
        if elem not in seen:
            yield elem
            seen.add(elem)

def uniq_blind(seq):
    return list(dict.fromkeys(seq))

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq_generator(input_list)

for element in output_list:
    print(element)
