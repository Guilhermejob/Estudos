from menu import products
from exceptions import is_integer, is_string
from collections import Counter

def get_product_by_id(id:int):
    product = {}
    try:
        is_integer(id)
        for item in products:
            if item['_id'] == id:
                product = item
                
        if product is not None:
            return product
        else:
            return {}
    except TypeError as error:
        print(error.args)
    except ValueError as error:
        print(error.args)
            
        


def get_product_by_type(type:str):
    product = []
    
    try:
        is_string(type)
        for item in products:
            if item['type'] == type:
                product.append(item)
                
        if product is not None:
            return product
        else:
            return []
    except TypeError as error:
        print(error.args)


def add_product (original_products:list, title, price, rating, description, type):
    print(len(original_products))
    
    if len(original_products) != 0:
        ordenado = sorted(original_products, key=lambda x: x["_id"])
    
        new_id = ordenado[-1]['_id'] + 1
    else:
        
        new_id = 1
        
    try:
    
        product = {
            '_id':new_id,
            'title':title,
            'price':price,
            'rating':rating,
            'description':description,
            'type':type
        }
        
        original_products.append(product)

        print(len(original_products))
    
    except KeyError as error:
        print(error.args)
        
    
    return product

def menu_report():
    
    number_of_products = len(products)
    
    avarage_price = round(sum([p['price'] for p in products]) / len(products), 2)
    
    contador = Counter(item["type"] for item in products)
    mais_comum = contador.most_common(1)[0]
    
    return f'Products count: {number_of_products} - Avarage Price: {avarage_price} - Most Commom Type: {mais_comum}'

        
        


        
    

