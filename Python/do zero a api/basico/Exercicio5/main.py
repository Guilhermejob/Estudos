from management.product_handler import get_product_by_id, get_product_by_type

product_by_id = get_product_by_id(5)

product_by_type =  get_product_by_type('car')


if __name__ == "__main__":
    print(product_by_id)
    print(product_by_type)
    ...
