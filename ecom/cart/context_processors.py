from .cart import Cart

#Create context processors so cart would work every page

def cart(request):
    #Return the default data from the cart
    return {'cart': Cart(request)}