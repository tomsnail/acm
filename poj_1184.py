#http://www.cnblogs.ans/Ackermann/p/5576461.html
import copy
from queue import Queue


sign=[[1,0,0,0,0,0],
      [1,1,0,0,0,0],
      [1,1,1,0,0,0],
      [1,1,1,1,0,0],
      [1,1,1,1,1,0],
      [1,1,1,1,1,1],
      [1,0,0,0,0,1],
      [1,1,0,0,0,1],
      [1,1,1,0,0,1],
      [1,1,1,1,0,1]]


class Data():
    def __init__(self):
        self.num = [0,0,0,0,0,0]
        self.step = 0
        self.status = 0
        self.pos = 0

vi = [[[[[[[ [ 0 for i in range(10)] for i in range(6)]for i in range(6)]for i in range(6)]for i in range(6)]for i in range(6)] for i in range(6) ] for j in range(6)]
ans = [[ 0 for i in range(8)] for i in range(10000)]
si  = [0,0,0,0,0,0,0]
di  = [0,0,0,0,0,0,0]
a = [0,0,0,0,0,0]
b = [0,0,0,0,0,0]
total = 0



def check(t):
    return vi[t.num[0]][t.num[1]][t.num[2]][t.num[3]][t.num[4]][t.num[5]][t.pos][t.status];
def gao(t):
    vi[t.num[0]][t.num[1]][t.num[2]][t.num[3]][t.num[4]][t.num[5]][t.pos][t.status] = 1;


def bfs():
    global total
    total = 0
    q = Queue()
    s = Data()
    t = Data()
    for i in range(6):
        s.num[i] = i
    s.step = s.status = s.pos = 0
    q.put(s)
    vi[0][1][2][3][4][5][0][0] = 1;
    while not q.empty():
        s = q.get()
        for i in range(6):
            ans[total][i] = s.num[i]
        ans[total][6] = s.status
        ans[total][7] = s.step
        total += 1
        t = s
        t.step += 1
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
            tmp = t.status
            t.pos += 1
            if t.pos > t.status or (t.status > 5 and t.pos > t.status - 6) :
                if t.status == 9:
                    t.status = 5
                else:
                    t.status += 1
            if  check(t) == 0:
                gao(t)
                q.put( copy.deepcopy(t))
            t.status = tmp
            t.pos -= 1
            kk = t.num[5]
            t.num[5] = t.num[t.pos]
            t.num[t.pos] = kk
            if t.status < 5:
                t.status += 6
                if t.status > 9:
                    t.status=5
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
    answer = 9999999;
    for i in range(total):
        step = ans[i][7]
        flag = True
        for j in range(6):
            if a[ans[i][j]] != b[j] and sign[ans[i][6]][j] == 0 :
                flag = False
                break;
            tt = abs(a[ans[i][j]] - b[j])
            step = step + tt
        if  flag and step < answer :
            answer=step;
    print(answer);

if __name__ == '__main__':
   main()