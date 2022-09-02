d={}
def most_frequent(inp):
    for i in inp:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
k=most_frequent('mmgkkwwwiii')
print(k)
