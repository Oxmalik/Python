lst = input().split()

new_lst=[]
for index, strng in enumerate(lst):
    if (len(strng)>3 or strng.startswith("a")):
        new_lst.append(index)
        # print(new_lst)
print(new_lst)
