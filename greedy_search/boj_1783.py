import sys

if __name__=="__main__":
    input = sys.stdin.readline
    width, length = map(int, input().split())

    if length < 6 or width < 2:
        if width == 1:
            print(min(int(length/2)+1, 4))
        else:
            print(min(length+1,4))
    else:
        print(length-1)