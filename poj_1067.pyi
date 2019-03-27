import math


def main(a=8,b=4):
    if a>b :
        a,b = b,a
    k = b -a
    x = (1+ math.sqrt(5.0))/2
    t = k*x +k
    if t == b:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()