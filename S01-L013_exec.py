import os


path = os.curdir + "/Data/"
files = os.listdir(path)

for name in files:
    with open(path+name,"r") as file:
        print(f"-"*30)
        print(f"Executing: {name}...")
        source = file.read()
        exec(source)
        print(f"Finished executing: {name}...")


