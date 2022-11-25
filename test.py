
l1=['Ali','reza','omid']
l2=[30,12,18]
l3=[18.20,15.50,12.0]

print(zip(l1,l2,l3))

for name,age,avg in zip(l1,l2,l3):
    print("{0},{1},{2}".format(name,age,avg))
    # print(f"{name},{age},{avg}")