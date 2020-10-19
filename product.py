product = []
while True:
	name = input('Enter name of the product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	p = []
	p.append(name)
	p.append(price)
	product.append(p)
print(product)

print(product[0][0])
