import sys

if __name__=="__main__":
    input = sys.stdin.readline
    width, length = map(int, input().split())
    width -= 1
    length -= 1

    if length < 6 or width < 2:
        if width == 1:
            print(min(int(length/2)+1, 4))
        elif width == 0:
            print(1)
        else:
            print(min(length+1,4))
    else:
        print(length-1)