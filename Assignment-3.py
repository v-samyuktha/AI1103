import random
success=0
needed={1,2}
for i in range(10000):
    keys=[1, 2, 3, 4, 5, 6] 
    dropped=random.randint(1,6)
    keys.remove(dropped)
    if keys[random.randint(0,4)] in needed:
        success+=1
    keys.insert(dropped-1,dropped)
print("Expected:")
print(0.3333)
print("Simulation:")
print(success/10000)