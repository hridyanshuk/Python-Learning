def printYes():
    print('Yes')

def printNo():
    print('No')

def findIndex(item, listVar):
    for counter, temp in enumerate(listVar):
        if temp==item:
            return counter
    return 'Not Found'
