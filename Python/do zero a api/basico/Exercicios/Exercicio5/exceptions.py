def is_integer (id):
    
    if type(id) is not int:
        raise TypeError('Product id must be an int')
    
    if id < 0:
        raise ValueError('Product id must be positive')
    
    return id

def is_string (value):
    
    if type(value) is not str:
        raise TypeError('product type must be a str')
    
    return value

def check_item_keys(item:dict):
    required_keys = ['description', 'price', 'rating', 'title', 'type']
    
    for key in required_keys:
        if key not in item:
            print('NÃO ESTA')
            raise KeyError(f'field {key} is required')
        

