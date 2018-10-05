import os
f=os.listdir('.')
for x in f:
    if 'a' in x:
        print(x)

    T = os.path.join('.', x)
    if os.path.isdir(T):
        print(1)
        t=os.listdir(T)
        for y in t:
            if 'a' in y:
                z=os.path.join(T,y)
                print(z)