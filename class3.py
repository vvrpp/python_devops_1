#grocery = [ 'milk' , 'bread' , 100,100,100, True,False,10.5]
#type(grocery)

shopping_cart = []
#print('total_products in the cart', len(shopping_cart))

shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.append('fruits')
shopping_cart.append('MIX_vegetables')

combo_offer = ['datacable','charger','screenguard','simpin']
shopping_cart.extend(combo_offer)

print('total_products in the cart', len(shopping_cart))

print('products in the cart', shopping_cart)

print('',shopping_cart[3])