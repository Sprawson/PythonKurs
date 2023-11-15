import os

def count_words(path):
    # r - raw
    with open(path,'r') as file:
        data = file.read()
    data_split = data.split(" ")

    return len(data_split)

path = r'd:\mydata.txt'
with open(path, 'w') as file:
    file.write("It's raining outside and some cars are driving by")

os.path.isfile(path) and print(f"There are {count_words(path)} words in the file")


