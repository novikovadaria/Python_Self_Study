string = input()

vowels = 'aeiou'

count = {}.fromkeys(vowels, 0)

for char in string:
    if char in count:
        count[char] += 1

print(count)