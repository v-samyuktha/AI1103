import random
success=0
for i in range(10000):
  thisset=set() 
  for j in range(5):
    thisset.add(random.randint(1,10))
  if(len(thisset)<5):
    success+=1
print("Expected:")
print(0.6976)
print("Simulation:")
print(success/10000)