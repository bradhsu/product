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
