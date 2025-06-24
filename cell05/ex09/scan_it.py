import re
import sys
if (len(sys.argv)==3):
    key=sys.argv[1]
    text=sys.argv[2]
    mat=re.findall(re.escape(key),text)
    if(mat):
        print(len(mat))
    else:print("none")
    
else:print("none")