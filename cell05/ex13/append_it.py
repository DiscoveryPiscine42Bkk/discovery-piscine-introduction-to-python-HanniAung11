import sys
import re
if len(sys.argv)>1:
    for word in sys.argv[1:]:
        if not re.search(r'ism',word):
            print(word+"ism")
else:print("none")