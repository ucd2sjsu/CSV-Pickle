import csv
import pickle
import base64
from collections import OrderedDict

d = open('fsm_params3.csv', 'r')

db = []

#for line in csv.reader(d):
#    db.append(line[-1:])
#    with open('output.csv', 'w', newline = "") as f:
#        writer = csv.writer(f, delimiter = ',')
#        writer.writerows(db)
        
ot = open('output.csv', 'r')

g=[]
#ga=[]
#g2=[]

keys, values = [], []

for line2 in csv.reader(ot):
    ga=str(line2[-1:])
    ga=base64.b64decode(ga)
    ga=pickle.loads(ga)
    g.append(ga)
    print(g)
    for key, value in myOrderedDict.item():
        keys.append(key)
        values.append(value)
        with open('output2.csv', 'w') as h:
            csvwriter = csv.writer(h)
            csvwriter.writerow(keys)
            csvwriter.writerows(values)
    
        #csvwriter = csv.DictWriter(h, fieldnames = ga[0].keys(), dialect=dialect)
        #csvwriter.writeheader()
        #csvwriter.writerows(ga)
        #csvwriter= csv.writer(h, delimiter = ' ')
        #csvwriter.writerows(g)

#for i in range(len(g)):
#    ga=g[i]
#    ga=str(ga)
#    ga=base64.b64decode(ga)
#    ga=pickle.loads(ga)
#    print(ga)
#    with open('output2.csv', 'w') as h:
#        csvwriter = csv.DictWriter(h)
#        csvwriter.writeheader()
#        csvwriter.writerows(ga)
    


#print(gc)
#print(type(gc))
    



#ga=g[56]
#ga=str(ga)
#gb=base64.b64decode(ga)
#gc = pickle.loads(gb)


       
