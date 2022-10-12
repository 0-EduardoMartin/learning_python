

#map(action, [1,2,3])

# this returns an object location
def verb(arg):
    ary = []
    for i in arg:
        ary.append(i*2)
    return ary

print(map(verb,[1,2,3]))

#this is how map returns a list doing a for loop for you
def verb(arg):
  return arg*2 #map removed the necessity to creat a for loop

print(list(map(verb,[1,2,3])))
