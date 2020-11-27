data = {}

def createSubset(n,m,string):
    subsetToCreate = n//m
    extra = n%m
    subsets = []
    chars = list(sorted(string))

    for i in range(subsetToCreate):
        singleSet = list()
        total = 0
        counter = m

        if i == 0:
            counter = m + extra
        
        while total != counter:
            singleSet.append(chars.pop(0))
            total += 1
            
        subsets.append(singleSet)

    print(subsets)


if __name__ == "__main__":
    n,m = input().split()
    n,m = int(n), int(m)
    string = input().strip()

    data = {chr(i):i-96 for i in range(97, 123)}

    createSubset(n,m,string)