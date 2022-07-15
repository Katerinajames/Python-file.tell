
f=open("d.txt","w")
f.write("Hello,there")
f.close()

print("--------------------------")
f=open("d.txt","r") 
k=f.read(3)
print(k)
print("---------------------")
g=f.tell()
print(g)
f.close()
