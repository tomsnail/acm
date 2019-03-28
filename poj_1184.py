#http://www.cnblogs.com/Ackermann/p/5576461.html
import copy
from queue import Queue


sign=[[1,0,0,0,0,0],[1,1,0,0,0,0],[1,1,1,0,0,0],[1,1,1,1,0,0],[1,1,1,1,1,0],[1,1,1,1,1,1],[1,0,0,0,0,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,1,0,1]]


class Data():
    def __init__(self):
        self.num = [0,0,0,0,0,0]
        self.st = 0
        self.sta = 0
        self.pos = 0

vi = [[[[[[[ [ 0 for i in range(10)] for i in range(6)]for i in range(6)]for i in range(6)]for i in range(6)]for i in range(6)] for i in range(6) ] for j in range(6)]
com = [[ 0 for i in range(8)] for i in range(10000)]
si  = [0,0,0,0,0,0,0]
di  = [0,0,0,0,0,0,0]
a = [0,0,0,0,0,0]
b = [0,0,0,0,0,0]
cnt = 0



def check(t):
    return vi[t.num[0]][t.num[1]][t.num[2]][t.num[3]][t.num[4]][t.num[5]][t.pos][t.sta];
def gao(t):
    vi[t.num[0]][t.num[1]][t.num[2]][t.num[3]][t.num[4]][t.num[5]][t.pos][t.sta] = 1;


def bfs():
    global cnt
    cnt = 0
    q = Queue()
    s = Data()
    t = Data()
    for i in range(6):
        s.num[i] = i
    s.st = s.sta = s.pos = 0
    q.put(s)
    vi[0][1][2][3][4][5][0][0] = 1;
    while not q.empty():
        s = q.get()
        for i in range(6):
            com[cnt][i] = s.num[i]
        com[cnt][6] = s.sta
        com[cnt][7] = s.st
        cnt += 1
        t = s
        t.st += 1
        if t.pos > 0:
            kk = t.num[0]
            t.num[0] = t.num[t.pos]
            t.num[t.pos] = kk
            if  check(t) == 0:
                gao(t)
                q.put(copy.deepcopy(t))
            kk = t.num[0]
            t.num[0] = t.num[t.pos]
            t.num[t.pos] = kk
        if t.pos < 5 :
            tmp = t.sta
            t.pos += 1
            if t.pos > t.sta or (t.sta > 5 and t.pos > t.sta - 6) :
                if t.sta == 9:
                    t.sta = 5
                else:
                    t.sta += 1
            if  check(t) == 0:
                gao(t)
                q.put( copy.deepcopy(t))
            t.sta = tmp
            t.pos -= 1
            kk = t.num[5]
            t.num[5] = t.num[t.pos]
            t.num[t.pos] = kk
            if t.sta < 5:
                t.sta += 6
                if t.sta > 9:
                    t.sta=5
            if check(t) == 0:
                gao(t)
                q.put(copy.deepcopy(t))

def main():
    bfs();
    si = "123456"
    di = "654321"
    for i in range(6):
        a[i] = ord(si[i])-ord('0');
        b[i] = ord(di[i])-ord('0');
    ans = 9999999;
    for i in range(cnt):
        st = com[i][7]
        flag = True
        for j in range(6):
            if a[com[i][j]] != b[j] and sign[com[i][6]][j] == 0 :
                flag = False
                break;
            tt = abs(a[com[i][j]] - b[j])
            st = st + tt
        if  flag and st < ans :
            ans=st;
    print(ans);

if __name__ == '__main__':
   main()