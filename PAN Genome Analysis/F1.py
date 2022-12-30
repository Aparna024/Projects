with open("PORPHYROMONAS.txt") as f:
    seq_a = f.read()

with open("strains.txt") as f:
    seq_b = f.read()
# print(seq_a)
a = tuple(seq_a)
b = tuple(seq_b)
x = 0
nonsense=0
missense=0
silent=0

for i, j in zip(a, b):
    if i != j:
        if (i == "A" and j == "U"):
            print("nonsense", i, "-", j)
            nonsense+=1

        if (i == "C" and j == "G"):
            print("missense", i, "-", j)
            missense+=1
        if (i == "G" and j == "C"):
            print("missense", i, "-", j)
            missense+=1
        if (i == "T" and j == "A"):
            print("silent", i, "-", j)
            silent+=1
print("nonsense: ",nonsense,"missense:",missense,"silent:",silent,sep='\n')
dict={"Count of nonsense":nonsense,"Count of missense": missense,"Count of silent":silent}
print(dict)