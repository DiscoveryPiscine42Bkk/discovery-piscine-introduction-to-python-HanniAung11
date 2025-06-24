import sys
length=len(sys.argv)
if(length>2):
    for i in range(length-1,0,-1):
        print(sys.argv[i])
else : print("none")