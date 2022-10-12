

#map(action, [1,2,3])

def verb(arg):
    ary = []
    for i in arg:
        ary.append(i*2)
    return ary

print(verb([1,2,3]))
