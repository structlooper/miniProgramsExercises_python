n = input("enter the name : ")

i = 0
temp = ""
while i < len(n):
   if n[i] not in temp:
        print(f"  {n[i]} : {n.count(n[i])}")
        temp += n[i]
   i +=1


  
   
