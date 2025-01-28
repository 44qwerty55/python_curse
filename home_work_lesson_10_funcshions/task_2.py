"""
task 2
Требования:
Проверять входные данные (цена и количество должны быть положительными)
Имена товаров не должны повторяться

"""
def add_product(products: list, name: str, price: float, quantity: int) -> list:
    """
    Добавляет новый товар в список.
    Проверяет, что цена и количество положительные.
    """
    try:
        if price <= 0 or quantity <= 0:
            return products
    except ValueError:
        print(f"price: '{price}' quantity: {quantity}")

    try:
        for product in products:
            if product['name'].lower() == name.lower():
                return products
    except ValueError:
        print(f"name: '{name}' exist")

    # Add new product
    new_product = {
        'name': name,
        'price': round(price, 2),
        'quantity': quantity
    }
    products.append(new_product)
    return products




def find_products(products: list, max_price: float = None, min_quantity: int = None) -> list:
    """
    Находит товары по заданным критериям:
    - Не дороже max_price (если указано)
    - Количество не меньше min_quantity (если указано)
    """
    result = []
    for product in products:
        # Check if matches search criteria
        price_ok = True if max_price is None else product['price'] <= max_price
        quantity_ok = True if min_quantity is None else product['quantity'] >= min_quantity

        if price_ok and quantity_ok:
            result.append(product)

    return result

def update_price(products: list, product_name: str, new_price: float) -> bool:
    """
    Обновляет цену товара.
    Возвращает True если товар найден и обновлен, False если не найден.
    """
    if new_price <= 0:
        print("Error: new price must be positive")
        return False

    for product in products:
        if product['name'].lower() == product_name.lower():
            product['price'] = round(new_price, 2)
            return True

    print("Product not found")
    return False
# Additional functions

def remove_product(products: list, product_name: str) -> list:
    """Removes product from list by name"""
    initial_length = len(products)
    products = [p for p in products if p['name'].lower() != product_name.lower()]

    if len(products) == initial_length:
        print("Product not found")

    return products


def calculate_total_value(products: list) -> float:
    """Calculates total value of all products"""
    total = sum(p['price'] * p['quantity'] for p in products)
    return round(total, 2)

# Example usage:
if __name__ == "__main__":
    # Initial product list
    products = [
        {'name': 'Apples', 'price': 89.90, 'quantity': 150},
        {'name': 'Bananas', 'price': 69.90, 'quantity': 120},
        {'name': 'Oranges', 'price': 99.90, 'quantity': 80}
    ]

    # Demonstrate functions
    print("Initial list:")
    print(products)

    # Add new product
    products = add_product(products, "Pears", 129.90, 50)
    print("\nAfter adding pears:")
    print(products)

    # Find products cheaper than 100
    affordable = find_products(products, max_price=100.00)
    print("\nProducts cheaper than 100:")
    print(affordable)

    # Update price
    updated = update_price(products, "Apples", 94.90)
    print("\nAfter updating apple price:")
    print(products)

    # Remove product
    products = remove_product(products, "Bananas")
    print("\nAfter removing bananas:")
    print(products)

    # Calculate total value
    total = calculate_total_value(products)
    print(f"\nTotal value of all products: ${total}")