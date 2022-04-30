
from collections import Counter, namedtuple, OrderedDict, defaultdict
from collections import deque 

# --- list functions ---

ll = []
ll.append(1)
ll.pop()
ll.extend([4,5,6])
ll.clear()
ll.index(4)
ll[-2]
for item in ll:
    print(item)

if 4 in ll:
    print("4 is present in list")

ll.sort() # changes ll
newll = sorted(ll)

ll.remove("abc") # will raise ValueError if "abc" is not present in the list

# ----- counter -----# 

# a = "aabbbcccccddaaa"
a = [1,2,3,4,4,3,2,1,1,1,2,3] 
my_counter = Counter(a)

print(my_counter)
print(my_counter.keys())
print(my_counter.values())


# ---- named tuple --- #
Point = namedtuple("Point", ['x','y'])
pt = Point(x=1,y=2)
print(pt)

# --- OrderedDict ---- #

od = OrderedDict()
od['1'] = 'a'
od['a'] = 2
od['c'] = 3

print(od)


# ---- defaultdict ---- #
# dd = defaultdict(lambda: 2)
dd = defaultdict(int)
dd['a'] = 3
dd['b'] = 31
dd['c'] = 32

print(dd['x'])
print(dd)


# ----- deque -----

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft('a')
d.appendleft('b')
print(d)
d.popleft()
d.pop()
print(d)
d.extend([4,5,6])
d.extendleft([9,10,11])

