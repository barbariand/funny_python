e=1
def deletes_e():
    global e
    try:
        raise Exception("fail")
    except Exception as e:
        pass
print(e)
deletes_e()
print(e)
