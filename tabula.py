import sys
import pdftables_api
import petlstuff
filename = sys.argv[1]
print(filename)

c = pdftables_api.Client('5qtkuxun8zqy')
c.csv(filename, filename[:-4])

#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

petlstuff(filename[:-4],'.csv')