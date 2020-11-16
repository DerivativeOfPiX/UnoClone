x = 0.25
y = 0.5
final = 0
for i in range(10):
    if(i % 2 == 0):
        final += y
    else:
        final += x
        
print(final)