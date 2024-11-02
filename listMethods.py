# Muhammad Malik
# 11/1/2024
# list methods

'''Create a function named merge that receives two lists as arguments. 
The function merges the two lists into one sorted list and returns it.
For example the following arguments: merge([1, 4, 2], [2, 5, 9]) will return [1, 2, 2, 4, 5, 9]'''

def merge(lst1, lst2):
    # newLst = 
    for i in range(len(lst2)):
        lst1.append(lst2[i])
        # print(newLst)
        print(lst1)

    lst1.sort()
    print(lst1)



# lsa = [1, 4, 2]
# lsb = [2, 5, 9]

lsa = [ 2]
lsb = [1]

merge(lsa,lsb)
