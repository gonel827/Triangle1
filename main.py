
def check (subAr):
    subAr.sort()
    return subAr[2] < (subAr[1] +  subAr[0])

if __name__ == '__main__':
    ar = []
    for i in range (1,51):
        ar.append(i)
    ar.sort()
    for i in range (-1,-len(ar) + 1, -1):
        end = len (ar) + 1 + i
        if check (ar[-2 + i : end]):
            print (ar[-2 + 1 : end ])
            p = (ar[-2 + i ]+ ar [-1 + i] + ar[i])/2
            print ((p * (p - ar[-2 + i])*(p-ar[-1 + i ]) * (p - ar [i])) ** 0.5)
            break
        else:
            print(ar[-2 + i: end], "no")

