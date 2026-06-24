import pandas as pd

#weighted payment validation
def validate_payment_distribution():
    orders_df = pd.read_csv("datasets/transactions/orders.csv")
    print("Payment Method Distribution")

    distribution = (orders_df["payment_method"].value_counts(normalize=True).mul(100).round(2))
    #print(distribution)


#weighted customers influence validation
def validate_customer_segments():
    customers_df = pd.read_csv("datasets/master/customers.csv")
    orders_df = pd.read_csv("datasets/transactions/orders.csv")

    segment_lookup = dict(zip(customers_df["customer_id"],customers_df["customer_segment"]))

    orders_df["customer_segment"] = (orders_df["customer_id"].map(segment_lookup))
    print("Customer Segment Distribution")

    segment_orders = (orders_df["customer_segment"].value_counts())
    #print(segment_orders)


#weighted cities validation
def validate_city_distribution():
    stores_df = pd.read_csv("datasets/master/stores.csv")
    orders_df = pd.read_csv("datasets/transactions/orders.csv")
    
    store_city_lookup = dict(zip(stores_df["store_id"],stores_df["city"]))
    orders_df["city"] = (orders_df["store_id"].map(store_city_lookup))

    print("City Distribution")
    #print(orders_df["city"].value_counts().head(20))

#80/20: 20% products creates 80% orders(revenue) validation
def validate_pareto_sales():
    order_items_df = pd.read_csv("datasets/transactions/order_items.csv")
    top_products = (order_items_df.groupby("product_id")["line_total"].sum().sort_values(ascending=False))

    total_revenue = (top_products.sum())
    top_20_percent = int(len(top_products)* 0.20)
    top_revenue = (top_products.head(top_20_percent).sum())
    share = round(top_revenue/total_revenue* 100,2)

    #print(f"\nTop 20% Products Revenue Share: "f"{share}%")
    print(f"Pareto Validation")