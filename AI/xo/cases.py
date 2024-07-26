x_col = [i for i in range(0, 3)]
y_col = [i for i in range(0, 3)]
z_col = [i for i in range(0, 9)]
a_col = [i for i in range(0, 72)]
b_col = [i for i in range(0, 72*9)]
c_col = [i for i in range(0, 72*9*9)]
d_col = [i for i in range(0, 72*9*9*9)]
e_col = [i for i in range(0, 72*9*9*9*9)]
f_col = [i for i in range(0, 72*9*9*9*9*9)]
g_col = [i for i in range(0, 72*9*9*9*9*9*9)]

cases = []
caseslv2 = []
caseslv3 = []
caseslv4 = []
caseslv5 = []
caseslv6 = []
caseslv7 = []
caseslv8 = []
caseslv9 = []

board = [['#' for _ in range(3)] for _ in range(3)]

for x in x_col:
    for y in y_col:
        board[x][y] = 'X'
        cases.append([row[:] for row in board])  # Create a copy of the board
        print(f'{cases}\n')
        board[x][y] = '#'

for z in z_col:
    for x in x_col:
        for y in y_col:
            if cases[z][x][y] == 'X':
                pass
            else:
                cases[z][x][y] = 'O'
                caseslv2.append([row[:] for row in cases[z]])  # Create a copy of the board
                print(f'{caseslv2}\n\n{len(caseslv2)}')
                cases[z][x][y] = '#'

for a in a_col:
    for x in x_col:
        for y in y_col:
            if caseslv2[a][x][y] == 'X' or caseslv2[a][x][y] == 'O':
                pass
            else:
                caseslv2[a][x][y] = 'X'
                caseslv3.append([row[:] for row in caseslv2[a]])  # Create a copy of the board
                caseslv2[a][x][y] = '#'

for b in b_col:
    for x in x_col:
        for y in y_col:
            if b < len(caseslv3) and x < 3 and y < 3:
                if caseslv3[b][x][y] == 'X' or caseslv3[b][x][y] == 'O':
                    pass
                else:
                    caseslv3[b][x][y] = 'O'
                    caseslv4.append([row[:] for row in caseslv3[b]])
                    caseslv3[b][x][y] = '#'

for c in c_col:
    for x in x_col:
        for y in y_col:
            if c < len(caseslv4) and x < 3 and y < 3:
                if caseslv4[c][x][y] == 'X' or caseslv4[c][x][y] == 'O':
                    pass
                else:
                    caseslv4[c][x][y] = 'X'
                    caseslv5.append([row[:] for row in caseslv4[c]])
                    caseslv4[c][x][y] = '#'

# ... and so on for the rest of the loops


for d in d_col:
    for x in x_col:
        for y in y_col:
            if d < len(caseslv5) and x < 3 and y < 3:
                if caseslv5[d][x][y] == 'X' or caseslv5[d][x][y] == 'O':
                    pass
                else:
                    caseslv5[d][x][y] = 'O'
                    if len(caseslv6) < len(d_col):
                        caseslv6.append([row[:] for row in caseslv5[d]])
                    caseslv5[d][x][y] = '#'

for e in e_col:
    for x in x_col:
        for y in y_col:
            if e < len(caseslv6) and x < 3 and y < 3:
                if caseslv6[e][x][y] == 'X' or caseslv6[e][x][y] == 'O':
                    pass
                else:
                    caseslv6[e][x][y] = 'X'
                    if len(caseslv7) < len(e_col):
                        caseslv7.append([row[:] for row in caseslv6[e]])
                    caseslv6[e][x][y] = '#'

for f in f_col:
    for x in x_col:
        for y in y_col:
            if f < len(caseslv7) and x < 3 and y < 3:
                if caseslv7[f][x][y] == 'X' or caseslv7[f][x][y] == 'O':
                    pass
                else:
                    caseslv7[f][x][y] = 'O'
                    if len(caseslv8) < len(f_col):
                        caseslv8.append([row[:] for row in caseslv7[f]])
                    caseslv7[f][x][y] = '#'

for g in g_col:
    for x in x_col:
        for y in y_col:
            if g < len(caseslv8) and x < 3 and y < 3:
                if caseslv8[g][x][y] == 'X' or caseslv8[g][x][y] == 'O':
                    pass
                else:
                    caseslv8[g][x][y] = 'X'
                    if len(caseslv9) < len(g_col):
                        caseslv9.append([row[:] for row in caseslv8[g]])
                    caseslv8[g][x][y] = '#'

print(caseslv9, len(caseslv9)+len(cases)+len(caseslv2)+len(caseslv3)+len(caseslv4)+len(caseslv5)+len(caseslv6)+len(caseslv7)+len(caseslv8))
with open("lv1.txt", "w") as lv1:
    
        lv1.write(str(cases))

with open("lv2.txt", "w") as lv2:
    
        lv2.write(str(caseslv2))
with open("lv3.txt", "w") as lv3:
    
        lv3.write(str(caseslv3))
with open("lv4.txt", "w") as lv4:
    
        lv4.write(str(caseslv4))
with open("lv5.txt", "w") as lv5:
    
        lv5.write(str(caseslv5))
with open("lv6.txt", "w") as lv6:
    
        lv6.write(str(caseslv6))
with open("lv7.txt", "w") as lv7:
    
        lv7.write(str(caseslv7))
with open("lv8.txt", "w") as lv8:
    
        lv8.write(str(caseslv8))
with open("lv9.txt", "w") as lv9:
    
        lv9.write(str(caseslv9))



