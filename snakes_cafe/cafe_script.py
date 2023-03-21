# snakes_cafe

if __name__ == "__main__":
    """
    """

    menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
    print(menu)

    prompt = """***********************************
** What would you like to order? **
***********************************"""
    full_Order = {}
    print(prompt)
    order_Item = input('Enter \'quit\' to quit: ')

    while order_Item != "quit":

        if order_Item in full_Order:
            new_Amount = full_Order.get(order_Item) + 1
            full_Order.update({order_Item: new_Amount})
        else:
            full_Order.update({order_Item: 1})

        print(full_Order)

        print(prompt)
        order_Item = input('Enter \'quit\' to quit: ')



