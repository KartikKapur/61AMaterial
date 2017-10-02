class Tree:
    """Tree with a value (entry) and a list of subtrees (branches)"""

    def __init__(self, entry, branches=()):
        self.entry = entry
        self.branches = branches


def print_tree(tree):
    level, curr = [], [tree]
    print(tree.entry)
    while curr:
        child = curr.pop(0)
        level.extend(child.branches)
        if not curr:
            if level:
                print(*[t.entry for t in level])
            level, curr = [], level


def filter_tree(f, t):
    children, branches = [], t.branches[:]
    for b in branches:
        if f(b.entry):
            children.append(filter_tree(f, b))
        else:
            branches.extend(b.branches)
    return Tree(t.entry, children)


t = Tree(1, [Tree(2, [Tree(4, [Tree(5)])]), Tree(3, [Tree(6), Tree(7)])])


# runs in n^2 time
def fun(n):
    count = n
    while (n > 0):
        n -= 1
    return fun(count - 1)


# Naive Fibonacci, takes polynomial time
def fib(n):
    if (n <= 2):
        return n
    return fib(n - 1) + fib(n - 2)


# Better fibonacci, with caching. Takes linear time
cache = {}


def fib(n):
    if (n < 2):
        return n
    if (n - 1 not in cache):
        cache[n - 1] = fib(n - 1)
    if (n - 2 not in cache):
        cache[n - 2] = fib(n - 2)
    return cache[n - 1] + cache[n - 2]


def fibTree(n):
    if (n < 2):
        return Tree(n)
    else:
        left = fibTree(n - 1)
        right = fibTree(n - 2)
        return Tree(left.entry + right.entry, [left, right])



def treeDepth(t):
    i = 0
    l = []
    deepness = depth(t, 0, l)
    while(i < len(l)):
        if(l[i] == deepness):
            return True
        else:
            return False

def depth(t, count=0, l=[]):
        l += [t.entry]
        if(not t.branches):
            return count
        lst = []
        for b in t.branches:
            lst+=[depth(b,count+1,l)]
        return max(lst)



