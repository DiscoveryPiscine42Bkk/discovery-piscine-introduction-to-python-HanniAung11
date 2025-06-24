#!/usr/bin/env python3

import sys
def shrink(text):
    print(text[:8])  
def enlarge(text):
    result = text + 'Z' * (8 - len(text))
    print(result)
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
else:
    print("none")
