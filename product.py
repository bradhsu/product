import os # operating system

products = []
if os.path.isfile('products.csv'): # check file
	print('The file exist')
# read the file
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'Product, Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('No products.csv')


while True:
	name = input('Enter name of the product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	products.append([name, price])
print(products)


for p in products:
	print(p[0], ' is $', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')