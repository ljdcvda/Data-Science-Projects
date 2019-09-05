
with open('AviationData.txt') as file:
    aviation_data = file.readlines()

aviation_list = []
for line in aviation_data:
    aviation_list.append(line.split('|'))
    
lax_code = []

for row in aviation_list:
    if 'LAX94LA336' in row:
        print('FOUND')
        lax_code.append(row)

print(aviation_list[:2])
