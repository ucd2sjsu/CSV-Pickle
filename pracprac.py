import csv
import pickle
import base64

d = open('fsm_params3.csv', 'r')

db = []

#for line in csv.reader(d):
#    db.append(line[-1:])
#    with open('output.csv', 'w', newline = "") as f:
#        writer = csv.writer(f, delimiter = ',')
#        writer.writerows(db)

ot = open('output.csv', 'r')

with open('output.csv') as outfile:
    reader=csv.DictReader(outfile)
    for row in reader:
        row=str(row)
        row=base64.b64decode(row)
        print(row)
           
