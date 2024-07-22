# Menu dictionary
menu = {
	"Snacks": {
		"Cookie": .99,
		"Banana": .69,
		"Apple": .49,
		"Granola bar": 1.99
	},
	"Meals": {
		"Burrito": 4.49,
		"Teriyaki Chicken": 9.99,
		"Sushi": 7.49,
		"Pad Thai": 6.99,
		"Pizza": {
			"Cheese": 8.99,
			"Pepperoni": 10.99,
			"Vegetarian": 9.99
		},
		"Burger": {
			"Chicken": 7.49,
			"Beef": 8.49
		}
	},
	"Drinks": {
		"Soda": {
			"Small": 1.99,
			"Medium": 2.49,
			"Large": 2.99
		},
		"Tea": {
			"Green": 2.49,
			"Thai iced": 3.99,
			"Irish breakfast": 2.49
		},
		"Coffee": {
			"Espresso": 2.99,
			"Flat white": 2.99,
			"Iced": 3.49
		}
	},
	"Dessert": {
		"Chocolate lava cake": 10.99,
		"Cheesecake": {
			"New York": 4.99,
			"Strawberry": 6.49
		},
		"Australian Pavlova": 9.99,
		"Rice pudding": 4.99,
		"Fried banana": 4.49
	}
}

def place_order():
	# Ask the customer from which menu category they want to order
	print("From which menu would you like to order? ")

	# Create a variable for the menu item number
	i = 1
	# Create a dictionary to store the menu for later retrieval
	menu_items = {}

	# Print the options to choose from menu headings (all the first level
	# dictionary items in menu).
	for key in menu.keys():
		print(f"{i}: {key}")
		# Store the menu category associated with its menu item number
		menu_items[i] = key
		# Add 1 to the menu item number
		i += 1

	# Get the customer's input
	menu_category = input("Type menu number: ")

	# Check if the customer's input is a number
	if menu_category.isdigit():
		# Check if the customer's input is a valid option
		if int(menu_category) in menu_items.keys():
			# Save the menu category name to a variable
			menu_category_name = menu_items[int(menu_category)]
			# Print out the menu category name they selected
			print(f"You selected {menu_category_name}")

			# Print out the menu options from the menu_category_name
			print(f"What {menu_category_name} item would you like to order?")
			i = 1
			menu_items = {}
			print("Item # | Item name                | Price")
			print("-------|--------------------------|-------")
			for key, value in menu[menu_category_name].items():
				# Check if the menu item is a dictionary to handle differently
				if type(value) is dict:
					for key2, value2 in value.items():
						num_item_spaces = 24 - len(key + key2) - 3
						item_spaces = " " * num_item_spaces
						print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
						menu_items[i] = {
							"Item name": key + " - " + key2,
							"Price": value2
						}
						i += 1
				else:
					num_item_spaces = 24 - len(key)
					item_spaces = " " * num_item_spaces
					print(f"{i}      | {key}{item_spaces} | ${value}")
					menu_items[i] = {
						"Item name": key,
						"Price": value
					}
					i += 1

			# 2. Ask customer to input menu item number
			menu_item = input("Type menu item number: ")

			# 3. Check if the customer typed a number
			if menu_item.isdigit():
				# Convert the menu selection to an integer
				menu_item = int(menu_item)
				# 4. Check if the menu selection is in the menu items
				if menu_item in menu_items.keys():
					# Store the item name as a variable
					item_name = menu_items[menu_item]["Item name"]
					# Ask the customer for the quantity of the menu item
					quantity = input(f"How many {item_name} would you like? ")
					# Check if the quantity is a number, default to 1 if not
					if quantity.isdigit():
						quantity = int(quantity)
					else:
						quantity = 1
					# Add the item name, price, and quantity to the order list
					customer_order.append({
						"Item name": item_name,
						"Price": menu_items[menu_item]["Price"],
						"Quantity": quantity
					})
					# Tell the customer that their input isn't valid
				else:
					print(f"{menu_item} was not a menu option.")
			else:
				# Tell the customer they didn't select a menu option
				print("You didn't select a number.")
		else:
			# Tell the customer they didn't select a menu option
			print(f"{menu_category} was not a menu option.")
	else:
		# Tell the customer they didn't select a number
		print("You didn't select a number.")

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = [
  # {
  #   "Item name": "string",
  #   "Price": float,
  #   "Quantity": int
  # }
]

# Set up the greeting and ordering messages
greeting_msg   = "Welcome to the variety food truck."
sale_msg       = "Would you like to place an order?"
reorder_msg    = "Would you like to keep ordering?"
bad_input_msg  = "I didn't understand that."
input_opts_msg = "(Y)es or (N)o: "

# Set up the prompts and reprompts
sale_prompt     = f"{greeting_msg} {sale_msg} {input_opts_msg} "
sale_reprompt   = f"{bad_input_msg} {sale_msg} {input_opts_msg} "
reorder_prompt  = f"{reorder_msg} {input_opts_msg} "
reorder_repromt = f"{bad_input_msg} {reorder_msg} {input_opts_msg} "

# Set up the input logic variables
input_opts      = { "Y": True, "N": False }
input_opts_keys = input_opts.keys()
wants_to_order = None

# Ask the customer if they would like to place an order.
while wants_to_order not in input_opts_keys:
	if wants_to_order is None:
		wants_to_order = input(sale_prompt).upper()
	else:
		wants_to_order = input(sale_reprompt).upper()
	
	# Exit the program if the customer doesn't want to place an order
	is_valid_input = wants_to_order in input_opts_keys
	if is_valid_input and input_opts[wants_to_order] == False:
		print("No problem! Come back when you're ready to order.")
		exit()

# Customers may want to order multiple items, so let's create a continuous loop
while wants_to_order:
	place_order()
	# Ask the customer if they would like to order anything else
	keep_ordering = None

	# 5. Check the customer's input
	while keep_ordering not in input_opts_keys:
		wants_to_order = "N"
		if keep_ordering is None:
			keep_ordering = input(reorder_prompt).upper()
		else:
			keep_ordering = input(reorder_repromt).upper()

		match keep_ordering:
			case "Y":
				wants_to_order = "Y"
			case "N":
				print("Thank you for your order!")
				wants_to_order = ""

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in customer_order:
	# 7. Store the dictionary items as variables
	item_name = item["Item name"]
	price = item["Price"]
	quantity = item["Quantity"]

	# 8. Calculate the number of spaces for formatted printing
	name_spaces = 26 - len(item_name)
	price_spaces = 6 - len(str(price))
	quantity_spaces = 9 - len(str(quantity))

	# 9. Create space strings
	name_spaces = " " * name_spaces
	price_spaces = " " * price_spaces
	quantity_spaces = " " * quantity_spaces

	# 10. Print the item name, price, and quantity
	item_name_text = f"{item_name}{name_spaces}"
	price_text = f"${price}{price_spaces}"
	quantity_text = f"{quantity}{quantity_spaces}"
	print(f"{item_name_text}| {price_text}| {quantity_text}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print("--------------------------|--------|----------")
total_cost = sum([item["Price"] * item["Quantity"] for item in customer_order])
print(f"Total cost: ${format(total_cost, '.2f')}")