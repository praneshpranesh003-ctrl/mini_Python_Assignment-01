

# ------------------------------------
# Part A - Spot the Bug
# ------------------------------------

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Bug Demonstration")

print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))



# Explanation:
# cart=[] is created only once when the function is defined.
# The same list is reused every time the function is called
# without providing a cart argument.


# ------------------------------------
# Part B - Correct Version
# ------------------------------------

def add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print("\nPart B - Fixed Function")

print(add_item("apple"))
print(add_item("banana"))

# ------------------------------------
# Part C - Shopping Cart Program
# ------------------------------------
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):

    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):

    try:

        price_tuple[0] = new_price

    except TypeError as e:

        print("\nTypeError:", e)

        # Tuples are immutable.
        # Their values cannot be changed after creation.


def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)

    final_total = total - discount_amount

    return final_total


# ------------------------------------
# Create Two Independent Carts
# ------------------------------------

customer1 = create_cart("Pranesh", 10)

customer2 = create_cart("Rahul", 5)
add_to_cart(customer1, "Laptop", 50000)

add_to_cart(customer1, "Mouse", 700, 2)

add_to_cart(customer2, "Book", 400, 2)

add_to_cart(customer2, "Pen", 20, 5)

print("\nCustomer 1 Cart")

print(customer1)
print("\nCustomer 2 Cart")
print(customer2)


# Display totals

print("\nCustomer 1 Total:", calculate_total(customer1))

print("Customer 2 Total:", calculate_total(customer2))


# Demonstrate tuple immutability

price_data = (500,)

update_price(price_data, 800)


# ------------------------------------
# Discussion Points
# ------------------------------------

# 1. Why is discount=0 safe but cart=[] dangerous?

# discount=0 is safe because integers are immutable.

# cart=[] is dangerous because lists are mutable.

# The same list object is reused across function calls.


# 2. What is the difference between rebinding and mutating?

# Rebinding:
# Assigning a variable to a completely new object.

# Example:
# x = [1, 2]
# x = [5, 6]

# Mutating:
# Changing the existing object.

# Example:
# x = [1, 2]
# x.append(3)


# 3. Which are mutable?

# list -> Mutable

# tuple -> Immutable

# dict -> Mutable

# set -> Mutable

# str -> Immutable

# int -> Immutable


# 4. When you pass a list into a function and modify it,
# do changes reflect outside?

# Yes.

# Because both the original variable and the function
# parameter refer to the same list object in memory.