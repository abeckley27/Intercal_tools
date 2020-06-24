#INTERCAL code creator 9000!


f = open("output.i","w")

def binFlip(num):   #Function converts to backwards binary and back to decimal
    b1 = bin(num)[2:]
    while len(b1) < 8:
        b1 = '0' + b1
    b2 = ''
    i = 7
    while len(b2) < 8:
        b2 = b2 + b1[i]
        i -= 1
    return int(b2, base = 2)


def generate(text):
    # Create INTERCAL code that prints out text
    text = text + '\n'
    f.write("DO ,1 <- #%d \n" %len(text))
    s_index = 0     #This is the position in the string called text
    OutPos = [0]      #This is a list of the positions of the output head
    line = 2        #This is the current line being written
    while s_index < len(text):
        char = d[text[s_index]]
        OutPos.append(binFlip(char))
        if line % 3 == 0:
            p = 'PLEASE '
        else:
            p = ''
        move = OutPos[s_index] - OutPos[-1]
        if move < 0:
            move += 256
        f.write(p + 'DO ,1SUB#%d <- #%d \n' %(s_index + 1,move))
        line += 1
        s_index += 1
    f.write('DO READ OUT ,1 \n')
    f.write('DO GIVE UP')

    f.close()
    
def generate_from_file(fname):
    fin = open(fname, 'r')
    text = fin.read()
    fin.close()
    text = text + '\n'
    f.write("DO ,1 <- #%d \n" %len(text))
    s_index = 0     #This is the position in the string called text
    OutPos = [0]      #This is a list of the positions of the output head
    line = 2        #This is the current line being written
    while s_index < len(text):
        char = d[text[s_index]]
        OutPos.append(binFlip(char))
        if line % 3 == 0:
            p = 'PLEASE '
        else:
            p = ''
        move = OutPos[s_index] - OutPos[-1]
        if move < 0:
            move += 256
        f.write(p + 'DO ,1SUB#%d <- #%d \n' %(s_index + 1,move))
        line += 1
        s_index += 1
    f.write('DO READ OUT ,1 \n')
    f.write('DO GIVE UP')

    f.close()

d = dict()
lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppers = [0]*26
for k in range(26):
    uppers[k] = lowers[k].upper()
    d[uppers[k]] = 65 + k
    d[lowers[k]] = 97 + k
d[' '] = 32
d[':'] = 58
d['\n'] = 10
d['?'] = 63
d["."] = 46
d["'"] = 39
d[","] = 44
for k in range(10):
    d[str(k)] = 48 + k
