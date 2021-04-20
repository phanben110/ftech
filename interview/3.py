#arrayInput = [3,1,2,1] 
#m = 5  

#arrayInput = [4,1,2,2] 
#m= 4

arrayInput = [7,5,5,8,3] 
m = 8 

arrayM = [] 
arrayOutput = [] 
check = None 

#check constraints 
if m>=1 and m <= 1000 and len(arrayInput) >=1 and len( arrayInput ) <= m :
    for a in range(len(arrayInput)) : 
        if arrayInput[a] >= 1  and arrayInput[a] <= m : 
            check = True 
        else: 
            check = False 
            break 
        
for i in range(m+1) :
    if i == 0 : 
        pass 
    else :
        arrayM.append(i)

if check == True  :
    while ( len(arrayOutput) <=( len(arrayInput) -1 ) ) : 
    
        for i in range(len(arrayInput)) : 
            for j in range (len(arrayM)) :
    
                if arrayInput[i] == arrayM[j] :
                    #print (j)
                    arrayM.remove(arrayInput[i]) 
                    arrayOutput.append(j) 
                    array = [arrayInput[i]] 
                    arrayNew = array + arrayM
                    print(arrayNew) 
                    break 
            arrayM = arrayNew 
    print ( "final result is : ",  arrayOutput )
else: 
    print ("some thing was wrong" ) 

