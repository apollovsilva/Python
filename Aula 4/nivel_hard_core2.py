def do_twice (f,g):
    f (g)
    f (g)

def print_twice (h):
    print(h)
    print(h)

# do_twice (print_twice,'spam')

def do_four (x,y):
    do_twice(x,y)
    do_twice(x,y)


do_four(print,'spam')
