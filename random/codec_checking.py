import sys
for i in sys.path:
    print(i)
print("hello world")
print()
import codecs
print(dir(codecs))
import os
print("Codecs Module Path:", os.path.dirname(codecs.__file__))
for p in os.walk(os.path.dirname(codecs.__file__)+"/encodings"):
    print(p)
print(codecs.__file__)
