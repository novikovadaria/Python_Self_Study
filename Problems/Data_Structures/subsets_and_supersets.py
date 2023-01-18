set1 = {4,16,20}
set2 = {4,8,12,16,20,24,21}

print(set1.issuperset(set2))
print(set2.issubset(set1))

if set1.issubset(set2):
    set1.clear()

if set2.issubset(set1):
    set2.clear()