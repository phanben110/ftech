
arrayInput = [4,3,2,7,8,2,3,1] 
a = len(arrayInput)
arrayOutput = []
check = None

#check Constraints 
n = len (arrayInput ) 
if n >= 1 and n <= 105: 
    for i in range( len (arrayInput) ) : 
        if arrayInput[i] >= 1 and arrayInput[i] <= n : 
            check = True 

        else : 
            check = False 
else :
    check = False 
            
if check == True : 


    for i in range (a) : 
        count = 0  
        for j in range(a): 
            if arrayInput[i] == arrayInput[j] : 
                count+= 1 
                if count >= 2:
                    arrayOutput.append(arrayInput[i]) 
                    print("number i",arrayInput[i])   
            else: 
                pass 
    output = set(arrayOutput)
    result = list(output) 
    print("the result is: ", result   )  

    


