number =  14 

arrayOutput = [] 
while (1): 
    if number == 1: 
        break  
    else : 
        matches = number//2
        advance = number - matches 
        arrayOutput.append( matches ) 
        number = advance 
    
print ( arrayOutput  )
sumOutput = 0 
for i in range ( len(arrayOutput)) : 
    sumOutput += arrayOutput[i] 

print("the result is : ", sumOutput ) 
    
