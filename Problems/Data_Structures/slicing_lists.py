
list1 = [3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]

list3=[]
odd_elements = list1[1::2]

even_elements = list2[0::2]

list3.extend(odd_elements)
list3.extend(even_elements)