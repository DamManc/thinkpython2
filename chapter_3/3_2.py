#Chapter 3
#Ex: 2
#2_1
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)
#2_2
def do_twice(f, v):
    f(v)
    f(v)
def print_spam(v):
    print(v)
do_twice(print_spam, 'ciao')
#2_3
def print_twice(v):
    print(v)
    print(v)
#2_4
def do_twice(f, v):
    f(v)
    f(v)
do_twice(print_twice, 'spam')
#2_5
def do_four(f, v):
    f(v) 
    f(v) 
do_four(print_twice, 'ciao')
