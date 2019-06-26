f = ["lol", "láál", "lol", 21]
if f.count("lol") == 2 and any(isinstance(x, int) for x in f):
    for x in range(len(f)):
        if isinstance(f[x], int):
            f[x] = "kutya"
print(f)