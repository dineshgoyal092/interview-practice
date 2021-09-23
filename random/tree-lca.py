ass tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# def sum(t):
#     if t is None:
#         return True
#     elif t.left is None and t.right is None:
#         return True
#     elif t.left is not None and t.right is not None:
#         return sum(t.left) & sum(t.right)
#     else:
#         return False



def sum(t,i,j):
    if t is None:
        return None
    elif t.data == i or t.data ==j:
        return t
    a = sum(t.left,i,j)
    b = sum(t.right,i,j)
    if a and b:
        print(t.data)
        return t
    elif a:
        return a
    elif b:
        return b

def insert(t,key ):
    if t is None:
        m = tree(key)
        return m
    elif t.data > key:
        t.left = insert(t.left,key)
    elif t.data < key:
        t.right = insert(t.right, key)
    return t

def lca(t,i,j):
    if i > j:
        temp = i
        i = j
        j = temp
    if t.data > i and t.data < j:
        return t.data
    elif t.data == j or t.data == i:
        return t.data
    elif t.data > j:
        return lca(t.left,i,j)
    elif t.data < j:
        return lca(t.right,i,j)
    return -1

def find(t,k,i):
    if t is None:
        return i
    if t.data >= k:
        return find(t.left,k,i)
    elif t.data < k and t.data > i:
        return find(t.right,k,t.data)
    return 0


def print_path(t,k,path):
    if t is None:
        return
    path.append(t.data)
    print_path(t.left,k,path)
    print_path(t.right, k, path)
    if len(path) == k:
        for i in path:
            print(i)
        print("---")
    path.pop()





a = [4,8,10,12,14,22]
t = tree(20)
t.left = tree(8)
t.left.right  = tree(12)
for i in range(len(a)):
    t = insert(t,a[i])
print(t.left.right.data)
print(t.left.right.right.data)
print(t.right.data)

print(lca(t,4,14))
print_path(t,3,[])


