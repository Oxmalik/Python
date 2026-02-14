# Create a function named frequency_counter that takes a list data_list as an argument. 
# The function should count the frequency of each item in the list and return a dictionary where 
# the keys are the unique items from the list and the values are the counts of how many times
# each item appears.

# For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return a dictionary like this:

# {1: 1, 2: 2, 3: 3, 4: 4}

def frequency_counter(data_list):
    # count=0
    freq_dict={}
    for num in data_list:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        # freq_dict = {
        #     num: count
        # }
        # print(freq_dict)
    print(freq_dict)


dat_lst = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]

frequency_counter(dat_lst)