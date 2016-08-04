#/usr/bin/python
#coding=utf-8

def fib1(n):
    n = int(n);
    return range(n);

if(__name__ == "__main__"):
    import sys;
    print fib1(sys.argv[1]);
else:
    #print __name__;
    pass;
