import random

gcount=0
bcount=0

for i in range(10000):
  if random.randint(1,40)<26:
    gcount+=1
  else:
    bcount+=1

probgirl=gcount/10000
probboy=bcount/10000
print("Expected: ")
print(0.625,0.375)
print("Simulation: ")
print(probgirl, probboy)