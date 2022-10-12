

#map(action, [1,2,3])

# this returns an object location
def verb(arg):
    ary = []
    for i in arg:
        ary.append(i*2)
    return ary

print(map(verb,[1,2,3]))

#this is how map returns a list
def verb(arg):
  return arg*2

print(list(map(verb,[1,2,3])))
