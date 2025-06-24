import sys
if (len(sys.argv)>1):
    length=len(sys.argv)-1
    print(f"parameters: {length}")
    for i in range(1,length+1):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:print("none")