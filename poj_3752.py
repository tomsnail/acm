
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

s = [[]]
count = 0
m = 0
n = 0

def rotation():
    global s
    global n
    global m
    s = [[0]*n for i in range(m)]
    addLetter(0,0,1)
    for i in range(m):
        print(s[i])

def addLetter(x,y,d):
    global count
    global s
    global n
    global m
    if x<0 or x>=m or y<0 or y>=n:
        return
    if count>=n*m:
        return
    if s[x][y] == 0:
        s[x][y] = letters[count%26]
        count+=1
    if d == 1 :
        if y+1== n or s[x][y+1]!=0:
            addLetter( x+1, y,   2)
        else:
            addLetter( x, y + 1,  d)
    elif d==2:
        if x+1==m or s[x+1][y]!=0 :
            addLetter( x, y - 1  , 3)
        else:
            addLetter( x + 1, y, d)
    elif d==3:
        if y - 1 < 0 or s[x][y-1] != 0:
            addLetter( x-1, y, 4)
        else:
            addLetter( x , y-1, d)
    elif d==4:
        if x - 1 < 0 or s[x-1][y] != 0:
            addLetter( x, y + 1, 1)
        else:
            addLetter( x-1, y, d)
    else:
        return


def inputs(text):
    number = input(text);
    if number.isdigit():
        return int(number)
    else:
        return inputs(text)

def main():
    global n
    global m
    m = inputs("请输入行数：")
    n = inputs("请输入列数：")
    rotation()


main();