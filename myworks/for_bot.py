user_input = 'my chemical romanc/im not okay'
l_i = list(user_input)
l = len(user_input)
ind = user_input.index('/')
author = []
lyrics = []
for i in l_i[0:ind]:
    author.append(i)

for i in l_i[ind+1:l]:
    lyrics.append(i)

s_l = ''.join(lyrics)
s_a = ''.join(author)
print(s_a, s_l)
