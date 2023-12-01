def f():
    global x
    x = 42
    print('local', x)

x = 666
f()

print('global', x)
