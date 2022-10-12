


# # is_y = False
# # is_n = False

# # if is_y and is_n:
# #     print('works')
# # elif is_y and not is_n :
# #     print("two")
# # elif not is_y:
# #     print('three')
    
# from re import I


# is_l = ["aa","rt", 34, {1,2,3}, ["gt","gh","ge"],"aaa"]
# is_sl = [1,2,3,4,5,6,7]

# for i in is_sl:
#     i+=i
# print(i)

# for i in enumerate(["b","y","e"]):
#     print(i)
    
from itertools import count


picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
def tree():
    for row in picture:
        for pixel in row:
            if pixel:
                print('*', end = '')
            else:
                print(' ', end = '')
        print('\n', end = '')


slist = ["a", "b", "a", "c"]

def sup(n,e):
    return(f"words here {n} you {e} bro")
print(sup("dude", "fuck"))


tree()

def funct(*dos, **kwdos):
    count=0
    for stuff in kwdos.values():
        count += stuff
    return sum(dos) + count
print(funct(1,2,3, c=1, b=2))

def funct(*li):
    evs = []
    for stuff in li:
        if stuff %2 ==0:
            evs.append(stuff)
    return max(evs)
print(funct(8,19,22,4,9,9,6,100))

