from management.product_handler import get_product_by_id, get_product_by_type, menu_report, add_product
from exceptions import check_item_keys
from menu import products

product_by_id = get_product_by_id(5)

product_by_type =  get_product_by_type('drink')

new_product = {
    "title": "Bolinho JS",
    "price": 1.0,
    "rating": 2,
    "description": "Bolinho de JS com cenoura",
    "type": "bakery",
    }

new_product_no_type = {
    "title": "Bolinho JS",
    "price": 1.0,
    "rating": 2,
    "description": "Bolinho de JS com cenoura",
    }

new_product_with_more_keys = {
    "title": "Bolinho JS",
    "price": 1.0,
    "rating": 2,
    "description": "Bolinho de JS com cenoura",
    "type": "bakery",
    "extra_key_1":"extra_value_1",
    "extra_key_2":"extra_value_2"
    }

required_keys = ['description', 'price', 'rating', 'title', 'type']


if __name__ == "__main__":
    
    def only_required_keys(obj:dict):
        
        #COMPREENDENDO DICT COMPREHENSION
        new_dict = {
            key: new_product_with_more_keys[key] # Para cada chave criar um par Chave:valor no novo dict
            for key in new_product_with_more_keys # itera sobre todas as chaves do dict
            if key in required_keys #filtra somente as chaves que estao contidas dentro do required_keys
        }
                
        return new_dict      
    
    try:
        new_product = only_required_keys(new_product_with_more_keys)
        check_item_keys(new_product)
        add_product(products, **new_product)
        print(products[-1])
    except KeyError as error:
        print(error.args) 
    print(product_by_id)
    print(product_by_type)
    print(menu_report())
    ...
