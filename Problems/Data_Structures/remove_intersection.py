set1 = {4,6,9,12,15,24,21}
set2 = {4,8,12,16,20,24,21}

intersection = set1.intersection(set2)

for item in intersection:
    set1.remove(item)