
for i in [1,2,3,4,5]:
    filename = f"Episodes/{i}.txt"
    with open(filename) as f:
        for line in f:
            print(line)
            break