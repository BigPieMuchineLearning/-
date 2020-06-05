
def find_max(m):
    k=0
    for n in m:
        if k<n:
            k=n
        else:
            continue

    print(k)
find_max([2,4,6,7,2,43,5])
