def decimalToBinary(num1:int,num2:int):
    Dict={}
    for i in range(num1,num2+1):
        
        byno=0
        ctr =0
        if i==1:
            b=0
        else:
            #print(i,end='')
            
            #b=0
            temp=i
            while(temp>0):
                byno = ((temp%2)*(10**ctr))+byno
                temp= int(temp/2)
                ctr +=1
        #print(byno)
            dig = list(int(d) for d in str(byno))
            size =len(dig)
            for k in range(size-1):
                if dig[k]==dig[k+1]:
                    if dig[k]==1:
                        #print(": True",end = ' ')
                        #dict[i]='True
                        b=1
                        break
                else:
                    
                    #print(": False", end = ' s')
                    #dict[i]='False'
                    b=0
                    break
        if b== 0:
            Dict[i] = 'False'
        elif b==1:
            Dict[i] = 'True'
    #print(Dict)
    return Dict
        
            
        
           

        

            
        
            
# decimal number
#x=3
#y=4
#[int(x) for x in input("Enter two values: ").split()]
#print("Lower limit is: ", x)
#print("Upper limit is: ", y)
#print()
    

#decimalToBinary(x,y)