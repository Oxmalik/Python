# Create a program that takes a list and prints:

# For lists with 5 or more items: the first two and last two items
# For lists with less than 5 items: the first and last item only

input_list= input().split(', ')

lst_len = len(input_list)

if lst_len >= 5:
    frst_lst=input_list[:2]+input_list[-2:]
    print(frst_lst)
elif lst_len < 5 :
    scnd_lst=input_list[:1]+input_list[-1:]
    print(scnd_lst)
