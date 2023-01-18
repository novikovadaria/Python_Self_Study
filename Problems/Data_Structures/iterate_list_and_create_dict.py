example = [3,6,9,12,15,18,21]

element_count = {}

for item in example:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1