#Dounglan Cheung
#LAb10
#Draw a 5x5 E
def E():
    E='|'
    print("{0:>6}".format("-----"))
    print("{0:>2}".format(E))
    print("{0:>4}".format('---'))
    print("{0:>2}".format(E))
    print("{0:>6}".format("-----"))
#Draw a 5x5 F
def F():
    f = '|'
    print("{0:>6}".format("-----"))
    print("{0:>2}".format(f))
    print("{0:>3}".format("--"))
    print("{0:>2}".format(f))
    print("{0:>2}".format(f))
#Draw a 5x5 L
def L():
    l= '|'
    print("{0:>2}".format(l))
    print("{0:>2}".format(l))
    print("{0:>2}".format(l))
    print("{0:>2}".format(l))
    print("{0:>6}".format("-----"))
#Draw a 5x5 T
def T():
    t='|'
    print("{0:>6}".format("-----"))
    print("{0:>4}".format(t))
    print("{0:>4}".format(t))
    print("{0:>4}".format(t))
    print("{0:>4}".format(t))
#Draw a 5x5 I
def I():
    i='*'
    print("{0:>6}".format("*****"))
    print("{0:>4}".format(i))
    print("{0:>4}".format(i))
    print("{0:>4}".format(i))
    print("{0:>6}".format("*****"))
#Draw a 5x5 H
def H():
    h= '|'
    print("{0:>2}".format(h),"{0:>3}".format(h))
    print("{0:>2}".format(h),"{0:>3}".format(h))
    print("{0:>6}".format("-----"))
    print("{0:>2}".format(h),"{0:>3}".format(h))
    print("{0:>2}".format(h),"{0:>3}".format(h))

def main():
    T()
    H()
    E()
    print()
    E()
    L()
    F()
    print()
    F()
    I()
    L()
    E()
main()