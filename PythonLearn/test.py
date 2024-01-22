a="manageriAl"
vow="aeiouAEIOU"

            
dict={}
for j in a:
    if j in vow:
        if j in dict:
            dict[j]=dict[j]+1
            
        else:
            dict[j]=1
            
for key,value in dict.items():
    print(key*value,end="")
            
          

            
            
        
        
  