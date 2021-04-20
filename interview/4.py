
arrayInput = "AAB" 
list (arrayInput) 
lengh = len(arrayInput) 
arrayOutput = [] 
if lengh > 3 :
    print("sorry, please try againt") 
else : 

    for j in range(lengh) :
        array = 0  
        if j == 0:
            for i in range (lengh): 
        
                arrayOutput.append(arrayInput[i])  
        if j == 1:
            for i in range (lengh) : 
             
                array1 = arrayOutput[i] + arrayInput[j]
                array2 = arrayOutput[j] + arrayInput[i] 
                arrayOutput.append(array1)
                arrayOutput.append(array2)
        if j == 2: 
            for i1 in range ( lengh ) : 
                for i2 in range ( lengh) :
                    if arrayInput[i1] == arrayInput [j] and  arrayInput[i2] == arrayInput[i1] :
                        pass 
    
                    else :
    
                        array3 = arrayInput[i1] + arrayInput[j] + arrayInput[i2]
                   
                        arrayOutput.append( array3 ) 

                     

output = set(arrayOutput) 
result = list(output) 


print ( result  )
print ("final anser is: ", len(result) ) 

