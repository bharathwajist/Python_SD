for i in range(10):
    print(i, end=" ")

print()
i = 0
while(i<10):
    i+=1
    if(i >= 6):
        print("\nLoop has broken")
        break
    else:
        print(i,end=" ")