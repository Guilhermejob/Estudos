from typing import List
from menu import products

def calculate_tab (tab:List[object]):
    total_price_tab = 0
    
    for item in products:
        for tab_item in tab:
            if item['_id'] == tab_item['_id']:
                total_price_tab += item['price'] * tab_item['amount']
                
    return {'subtotal': f'${round(total_price_tab, 2)}'}


