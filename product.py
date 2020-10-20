

products = []
while True:
	name = input('Enter name of the product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	products.append([name, price])
print(products)

print(products[0][0])

for p in products:
	print(p[0], ' is $', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product, Price')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')