import pandas as pd

#incremental customers validation
def validate_incremental_customers():
    customers = pd.read_csv("datasets/master/customers.csv")
    print(customers.shape)

    customers_inc = pd.read_csv("datasets/master/customers_incremental.csv")
    print(customers_inc.shape)

#incremental orders validation
def validate_incremental_orders():
    orders = pd.read_csv("datasets/transactions/orders.csv")
    orders_inc = pd.read_csv("datasets/transactions/orders_incremental.csv")
    #print(orders.columns.tolist())
    print(orders.shape)
    print(orders_inc.shape)

#increemntal order items validation
def validate_incremental_order_items():
    orders_inc = pd.read_csv("datasets/transactions/orders_incremental.csv")
    items_inc = pd.read_csv("datasets/transactions/order_items_incremental.csv")
    items = pd.read_csv("datasets/transactions/order_items.csv")

    #print(items.columns.tolist())
    print(items.shape)
    #print(orders_inc.shape)
    print(items_inc.shape)


