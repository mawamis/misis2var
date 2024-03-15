import codecs
s = codecs.open('space.txt', 'r', 'utf_8_sig')
s1 = [i[:-2] for i in s]
f = [i.split('*') for i in s1[1:]]
question = input()
while question != 'stop':
    for k in range(len(f)):
        n = f[k]
        if question not in n:
            print('error.. er.. ror..')
            break
        else:
            if n[0] == question:
                print(f'Корабль {n[0]} был отправлен с планеты: {n[1]} и его направление движения было: {n[3]}')
                break
    question = input()
s.close()
