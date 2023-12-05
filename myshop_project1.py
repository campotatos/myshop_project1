# Setting loveseat description
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32in high x 40in wide x 30in deep. Red or white.
"""
# Setting loveseat price
lovely_loveseat_price = 254.00

# Adding Settee description
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50in high x 54.75in wide x 28in deep. Black
"""
# Setting Settee price
stylish_settee_price = 180.85

# Adding Lamp description
lux_lamp_description = """
Luxurious Lamp. Glass and iron. 36in tall. Brown with cream shade.
"""
# Setting Lamp price
lux_lamp_price = 52.15

# Setting sales tax. Colorado Springs sales tax is 8.2%
sales_tax = .082

# First customer purchase
customer_one_total = 0

# Keeping track of customer_one purchases
customer_one_items = ""

# Customer_one purchase a loveseat
customer_one_total += lovely_loveseat_price

# Adding customer_one purchase to items
customer_one_items += lovely_loveseat_description

# adding lux lamp to customer_one purchase
customer_one_total += lux_lamp_price

# adding lux lamp to customer_one items
customer_one_items += lux_lamp_description

# calculating sales tax
customer_one_tax = customer_one_total * sales_tax

# adding sales tax to customer total
customer_one_total += customer_one_tax

# Print receipt
print("Customer one Items:")
print(customer_one_items)
print("Customer one Total:")
print(customer_one_total)

