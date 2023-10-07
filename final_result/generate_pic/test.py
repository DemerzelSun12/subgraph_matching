
from ReadData import ReadData


data = ReadData()

'''
time: three dimensional list, 8 x 9 x 3. first: dataset, second: query, third: time
query: two dimensional list, 8 x 9. first: dataset, second: query size
name: one dimensional list, 8. dataset name
'''
time, query, name = data.getList()

# Enron
print(name[0]) 
# ['4 6', '5 7', '6 9', '7 10', '8 12', '9 13', '10 15', '11 16', '12 18']
print(query[0])

print(time[0][1])

print(name[7])
print(query[7])
print(time[7][2])