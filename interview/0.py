import json 
import numpy as np 
import csv 

filePath = "ftech.json" 
fileCsv  = "ftech.csv" 

with open(filePath,"r") as fp : 
    data = json.load(fp) 
print (data )

with open(fileCsv, mode='w') as ben:
            ben = csv.writer(ben, delimiter=',',
                                   quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ben.writerow(data)


