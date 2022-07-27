# 2022-07 Karstein Kvistad
# Import receips from COOP app and clean up data

import sys
 #print(sys.argv[0])  # Script file name
print(sys.argv[1])  # Argument #1
#print(sys.argv[2])  # Argument #2

from tkinter import Y
from petl import fromcsv, look, cut, tocsv 
import petl as etl
import pdftables_api
importedfile = sys.argv[1]
table1 = fromcsv(importedfile)   #Load the table
tabledone1, tabledone2, newitem = [], [], []
print()
print('##### Read complete receipt #####')
print()
print('Lines of receipt: ', len(table1))
table2 = etl.rowslice(table1, 6, len(table1)-28)    # Select the last n data rows. 
table3 = etl.setheader(table2, ['Vare', 'Antall', 'Stykkpris', 'Slett1', 'Rabatt', 'Sum'])   # Replace headers
onlystuff = etl.cutout(table3, 'Slett1')
#print(onlystuff)
print()
print('##### Removed useless text #####')
print()
print('Lines of goods: ', len(onlystuff))
#for all in onlystuff:
#    print(all)
addedrows = etl.addrownumbers(onlystuff,1,1,'Rad')  # Add row numbering
print()
print('##### Added row numbering to', len(addedrows), 'items #####')
#print(etl.look(addedrows, style='minimal'))
#print(asearch)  # Search any table
#print(len(asearch))
#print(etl.search(addedrows, 'Stykkpris', '..'))  # Search any table
#print(len(etl.search(addedrows, 'Stykkpris', '..')))

for x in range(1,len(addedrows)):
    y1 = list(addedrows[x-1])
    y2 = list(addedrows[x])
    y4 = y2
    if y4[1] != '':
        if not '%' in y4[4]:
            y4[4] = ''       
        tabledone1.append(y4)
print()
print('##### Removed all blanc lines #####')

for z in range(1,len(tabledone1)):
    if 'Rabatt' in tabledone1[z][1]:
        #print('RABATT: ', tabledone1[z][2] + ' ' + tabledone1[z][3])
        tabledone1[z-1][4] = tabledone1[z][2] + ' ' + tabledone1[z][3]
        tabledone1[z] = ['','','','','','',]
print()
print('##### Moved all "Rabatt" lines #####')

for z in range(1,len(tabledone1)):
    if 'Antall' in tabledone1[z][1]:
        #print('ANTALL: ', tabledone1[z][2] + ' ' + tabledone1[z][3])
        y1[2] = y2[1]
        y1[3] = y2[2]
        y4 = y1

        tabledone1[z-1][2] = tabledone1[z][1]
        tabledone1[z-1][3] = tabledone1[z][2]
        tabledone1[z] = ['','','','','','',]
print()
print('##### Moved all "Artikkel" lines #####')
 
#tabledone = etl.setheader(tabledone1, ['Linje', 'Vare', 'Antall', 'Stykkpris', 'Rabatt', 'Sum'])   # Replace headers
tabledone = etl.pushheader(tabledone1, ['Linje', 'Vare', 'Antall', 'Stykkpris', 'Rabatt', 'Sum'])   # Replace headers
#print(tabledone)
print()
print('##### Added new header #####')

for x in tabledone:
    if x[1] != '':
        tabledone2.append(x)
print()
print('##### Removed all blanc lines #####')
print()

tabledone3 = etl.cutout(tabledone2, 'Linje')
print('##### Removed old numbering column #####')
print()

tabledone4 = etl.addrownumbers(tabledone3,1,1,'Rad')  # Add row numbering
print('##### Added NEW row numbering to', len(tabledone4), 'items #####')
print()
           
for all in tabledone4:
    print(all)

tocsv(tabledone4, importedfile[:-4] +'_done.csv')   # Save to new file
