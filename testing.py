import string


stringRow = '# console swm-2md-01-01.ssf1	{ include con-2md-02-01.ssf1; port 11; } # verified 2020-09-11 # Temporary until we get console in Rack 1'
row = stringRow.split()
print(len(row))
row.pop(0)
print(row)

testString = ['hello', 'swm-2md-01-01.ssf1']

newString = testString[1].split('.')
print(newString)
#print(row[1])
#print(stringRow.index(row[1]))
#print(len(row[1]))
#print(stringRow[stringRow.index(row[1]) : (stringRow.index(row[2])) - 6])
#print(stringRow.split())