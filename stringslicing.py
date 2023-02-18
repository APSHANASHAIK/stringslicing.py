product='iphone 14 pro max | Rs.100000 | new '
name=product[:product.index ("|")]
print(name)
price=product[product.index("|")+1:product.rindex("|")]
print(price)
condition=product[product .rindex ("|")+1:]
print(condition)