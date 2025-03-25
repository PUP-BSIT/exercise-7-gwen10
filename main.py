# TODO (BATALLER): Get order details.
DISCOUNT_RATE = 0.10

def get_order_details():
    order_list = []
    
    while True:
        product_name = input("\nEnter product name: ").strip()
        
        price = input("Enter price: ")
        if not price.replace('.', '', 1).isdigit():
            print("Invalid input. Enter a valid number for price.")
            continue
        
        quantity = input("Enter quantity: ")
        if not quantity.isdigit():
            print("Invalid input. Enter a valid number for quantity.")
            continue
        
        order_list.append({
            "product_name": product_name,
            "price": float(price),
            "quantity": int(quantity),
            "total_price": float(price) * int(quantity)
        })
        total_amount = calculate_total_price(order_list)
        
        add_more = input("\nDo you want to add another item? (y/n): ")
        add_more = add_more.strip().lower()
        if add_more != "y":
            break

    total_amount, customer_name, senior_id = senior_discount(order_list)

    final_amount = calculate_discount(total_amount, senior_id)

    display_receipt(order_list, final_amount, customer_name, senior_id)