factorial=lambda n: n*factorial(n-1) if n else 1
factorials = lambda n: [y:=1, *[y:=y*i for i in range(1, n+1)]]




class _for:
    def __init__(self,arg1,arg2,arg3):
        print(dir(arg1))
        print(arg1,arg2,arg3)
    def __enter__(self):
        print("entering")
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit")

with _for(i:=1,i<10,i+2):
    print("hello")

