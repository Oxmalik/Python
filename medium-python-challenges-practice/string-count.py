# Create a program that receives a string as input, and it prints how many times the character s is in the string.

# Some chars might be uppercase, use char.lower() to convert it to lowercase.

text = input()
count=0

for chr in text:
    if chr.lower() == 's':
        count+=1
    # print(count)
# print(f"count: {count}")
print(count)
