import codecs
s = codecs.open('space.txt', 'r', 'utf_8_sig')
s1 = [i[:-2] for i in s]
f = [i.split('*') for i in s1[1:]]
num = []
for i in f:
    num.append(abs(int((i[0])[-3:])))
n = sorted(num)[:10]
for i in f:
    for k in n:
        if (abs(int((i[0])[-3:]))) == k:
            print(i[0])
s.close()
