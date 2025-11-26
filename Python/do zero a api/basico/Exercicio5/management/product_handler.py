from menu import products

def get_product_by_id(id:int):
    product = {}
    for item in products:
        if item['_id'] == id:
            product = item
            
    if product is not None:
        return product
    else:
        return {}
            
        


def get_product_by_type(type:str):
    product = []
    for item in products:
        if item['type'] == type:
            product.append(item)
            
    if product is not None:
        return product
    else:
        return []


def add_product (original_products:list, title, price, rating, description, type):
    
    if len(original_products) != 0:
        ordenado = sorted(original_products, key=lambda x: x["_id"])
    
        new_id = ordenado[-1]['_id'] + 1
    else:
        
        new_id = 1
    
    product = {
        '_id':new_id,
        'title':title,
        'price':price,
        'rating':rating,
        'description':description,
        'type':type
    }
    
    original_products.append(product)

    
    return product
    

