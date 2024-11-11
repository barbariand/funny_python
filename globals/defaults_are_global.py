def funny(test=[]):
    if not test:
        test+=["hello"]
    else:
        test+=["world"]
    return test;
funny()
print(funny())

