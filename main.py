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

# TODO (GONATO): Calculate total price.
def calculate_total_price(order_list):
    return sum(item['total_price'] for item in order_list)

# TODO (MIGUEL): Input customer name and senior id no.
def senior_discount(order_list):
    customer_name = input("\nEnter your name: ").strip()
    senior_id = input(
        "Enter senior ID number (leave blank if not senior citizen): "
    ).strip()

    if senior_id and not senior_id.isdigit():
        print("Invalid senior ID. Please enter a numeric ID or leave blank.")
        return senior_discount(order_list)

    total_amount = calculate_total_price(order_list)
    return total_amount, customer_name, senior_id

# TODO (SARIO): Calculate discount rate.
def calculate_discount(total_amount, senior_id):
    if senior_id:
        discount_rate = DISCOUNT_RATE
        discount = total_amount * discount_rate
        total_amount -= discount
        print(f"\n10% Senior Citizen Discount Applied: -₱{discount:.2f}")
    return total_amount

# TODO (TEVES): Display details
def display_receipt(order_list, final_amount, customer_name, senior_id):
    print("\n**********************************")
    print("         CUSTOMER RECEIPT         ")
    print("**********************************\n")
    print("= = = = = ORDER DETAILS = = = = =")
    for item in order_list:
        print("Product:", item['product_name'])
        print(f"Price:    ₱{item['price']:.2f}")
        print(f"Quantity: {item['quantity']}")
        print(f"Total:    ₱{item['total_price']:.2f}\n")
    
    print("= = = =  CUSTOMER DETAILS = = = =")
    print(f"Customer Name: {customer_name}")
    print("Senior ID No.:", "N/A" if not senior_id else senior_id, "\n")
    
    print("= = = = = = = BILL = = = = = == =")
    print(f"Grand Total: ₱{final_amount:.2f}\n")
    
    print("Thank you for your order!")
    print("\n**********************************\n")

get_order_details()