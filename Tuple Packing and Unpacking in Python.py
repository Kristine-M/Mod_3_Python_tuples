# task 1

# You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the 
# quantity. Your task is to unpack each tuple and print the order details 
# in a user-friendly format.

# Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
    # More orders...
]
# Write a function to iterate over the list of orders.
# Unpack each tuple in the list and format the details for display.

def unpack(orders):
    result = ""
    name = ""
    item = ""
    amount = 0
    
    for customer in orders:
        name = customer[0]
        item = customer[1] 
        amount = customer[2]
        
        result += name + " ordered " + str(amount) + " " + item + "\n"
        
    return result

print(unpack(orders))