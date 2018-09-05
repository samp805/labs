import numpy as np

def main(arr):
    trans = arr.transpose()
    row1 = trans[0]
    firstcol = row1.transpose()
    print(trans @ firstcol)
    print('Done!')



if __name__ == '__main__':
    arr = [1,2,3,4]
    r = list()
    r.append(arr)
    r.append(arr)
    n = np.array(r)
    main(n)
