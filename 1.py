import codecs
s = codecs.open('space.txt', 'r', 'utf_8_sig')
s1 = [i for i in s]
f = [i.split('*') for i in s1[1:]]
lines = []
for i in f:
    n = int((i[0])[5])
    m = int((i[0])[6])
    t = len(i[1])
    xd = int(((i[3]).split())[0])
    yd = int(((i[3]).split())[1])
    if n > 5:
        x = n+xd
    if n <= 5:
        x = -(n+xd)*4+t
    if m > 3:
        y = m+t+yd
    if m <= 3:
        y = -(n+yd)*m
    lines.append(f'{i[0]} - ({x},{y})')
    with open(r"space_new.txt", "w") as file:
        for  line in lines:
            file.write(line + '\n')
s.close()
file.close()

