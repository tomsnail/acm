import math

#https://www.cnblogs.com/Jiiiin/p/8680807.html
#Wythoff 发现了这个规律，
#用(ak, bk)(k=0,1,2...)表示所有的cold position, ak = floor(k×Φ), bk = ak+k, Φ = (1+sqrt(5))/2,即黄金分割, floor为向下取整。

def main(a=8,b=4):
    if a>b :
        a,b = b,a
    k = b -a
    x = (1+ math.sqrt(5.0))/2
    t = k*x +k
    if int(t) == b:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
    main(2,1)
    main(4, 7)
    main(4, 4)