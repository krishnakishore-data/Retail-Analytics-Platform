import pandas as pd
import numpy as np
import random
import sys
from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta

from watermark.watermark_manager import *
from utils.helpers import *
from config.constants import *
from config.data_quality_rules import *
from logging_framework.logger import logger
from utils.output_manager import save_dataset


fake = Faker("en_IN")

BASE_DIR = Path(__file__).resolve().parent.parent

MASTER_DIR = BASE_DIR / "datasets" / "master"
TRANSACTION_DIR = BASE_DIR / "datasets" / "transactions"
LOG_DIR = BASE_DIR / "logs"

MASTER_DIR.mkdir(parents=True, exist_ok=True)
TRANSACTION_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

def initialize_project():

    LOG_DIR.mkdir(
        exist_ok=True
    )

# ==========================================
# CUSTOMER GENERATION
# ==========================================

def generate_customers():

    customers = []

    cities = list(CITY_STATE_MAP.keys())

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        gender = random.choice(["Male", "Female"])

        if gender == "Male":
            first_name = random.choice(MALE_FIRST_NAMES)
        else:
            first_name = random.choice(FEMALE_FIRST_NAMES)

        last_name = random.choice(LAST_NAMES)

        city = random.choice(cities)
        state = CITY_STATE_MAP[city]

        signup_date = fake.date_between(
            start_date="-4y",
            end_date="today"
        )

        dob = fake.date_between(
            start_date="-70y",
            end_date="-18y"
        )

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{random.randint(100,9999)}@"
            f"{random.choice(EMAIL_DOMAINS)}"
        )

        phone = (
            str(random.choice([9,8,7,6])) +
            "".join(
                str(random.randint(0,9))
                for _ in range(9)
            )
        )

        customers.append({

            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "gender": gender,
            "date_of_birth": dob,
            "city": city,
            "state": state,
            "country": "India",
            "customer_segment": random.choice(CUSTOMER_SEGMENTS),
            "signup_date": signup_date,
            "created_date": signup_date,
            "updated_date": signup_date

        })

    customers_df = pd.DataFrame(customers)

    # ==========================================
    # NULL EMAIL SIMULATION       (2% customers with NULL email)
    # ==========================================

    null_email_count = get_dq_sample_size(len(customers_df), DATA_QUALITY_RULES["null_email_pct"])

    null_email_indices = random.sample(list(customers_df.index),null_email_count)

    customers_df.loc[null_email_indices,"email"] = None

    print(f"Null Emails Injected: {null_email_count}")

    # ==========================================
    # DUPLICATE PHONE SIMULATION   (1% Duplicate Phone Numbers)
    # ==========================================

    duplicate_phone_count = get_dq_sample_size(
        len(customers_df),
        DATA_QUALITY_RULES["duplicate_phone_pct"]
    )

    duplicate_indices = random.sample(list(customers_df.index),duplicate_phone_count)

    for idx in duplicate_indices:

        source_idx = random.choice(list(customers_df.index))
        customers_df.loc[idx,"phone"] = customers_df.loc[source_idx,"phone"]

    print(f"Duplicate Phones Injected: {duplicate_phone_count}")

    # ==========================================
    # MISSING CITY SIMULATION (1% Missing City Values)
    # ==========================================

    missing_city_count = get_dq_sample_size(len(customers_df),DATA_QUALITY_RULES["missing_city_pct"])

    missing_city_indices = random.sample(list(customers_df.index),missing_city_count)

    customers_df.loc[missing_city_indices,"city"] = None

    print(f"Missing Cities Injected: {missing_city_count}")
    #-------------------
    save_dataset(
    customers_df,
    dataset_name="customers",
    destination="datasets"
    )

    save_dataset(
        customers_df,
        dataset_name="customers",
        destination="retail_source",
        load_type="full_load"
    )

    #print(f"Customers generated: {len(customers_df):,}")
    logger.info(f"Customers generated: {len(customers_df):,}")

def generate_incremental_customers():

    customers_file = (MASTER_DIR /"customers.csv")

    customers_df = pd.read_csv(customers_file)

    max_customer_id = (customers_df["customer_id"].max())

    new_customer_count = (random.randint(10, 50))

    incremental_customers = []

    for i in range(1,new_customer_count + 1):

        customer_id = (max_customer_id + i)

        gender = random.choice(["Male", "Female"])

        if gender == "Male":
            first_name = random.choice(MALE_FIRST_NAMES)

        else:
            first_name = random.choice(FEMALE_FIRST_NAMES)

        last_name = random.choice(LAST_NAMES)

        city = random.choice(list(CITY_STATE_MAP.keys()))

        state = CITY_STATE_MAP[city]

        customer_segment = random.choices(
            CUSTOMER_SEGMENTS,
            weights=[
                50,
                30,
                15,
                5
            ],k=1)[0]
        
        date_of_birth = fake.date_between(
            start_date="-70y",
            end_date="-18y"
        )

        signup_date = (datetime.today().date())

        email_prefix = (f"{first_name}"f"{last_name}"f"{random.randint(100,999)}").lower()

        email = (f"{email_prefix}@"f"{random.choice(EMAIL_DOMAINS)}")

        phone = ("9"+ "".join(random.choices("0123456789",k=9)))

        created_date = datetime.today().date()

        updated_date = created_date

        incremental_customers.append(
            [
                customer_id,
                first_name,
                last_name,
                email,
                phone,
                gender,
                date_of_birth,
                city,
                state,
                "India",
                customer_segment,
                signup_date,
                created_date,
                updated_date
            ]
        )

    incremental_df = pd.DataFrame(
        incremental_customers,
        columns=[
                "customer_id",
                "first_name",
                "last_name",
                "email",
                "phone",
                "gender",
                "date_of_birth",
                "city",
                "state",
                "country",
                "customer_segment",
                "signup_date",
                "created_date",
                "updated_date"]
    )    

    #incremental_df.to_csv(MASTER_DIR /"customers_incremental.csv",index=False)
    save_dataset(
    incremental_df,
    dataset_name="customers",
    destination="datasets",
    load_type="incremental"
    )

    save_dataset(
        incremental_df,
        dataset_name="customers",
        destination="retail_source",
        load_type="incremental"
    )  #save incremental file

    updated_df = pd.concat([customers_df,incremental_df],ignore_index=True) #appends incremental file to master
    updated_df.to_csv(customers_file,index=False)
        
    #print(f"New Customers Generated: "f"{new_customer_count}")
    logger.info(f"New Customers Generated: "f"{new_customer_count}")
    
# ==========================================
# PRODUCT GENERATION
# ==========================================

def generate_products():

    products = []

    used_product_names = set()

    product_id = 1

    total_subcategories = sum(
        len(subcategories)
        for subcategories in PRODUCT_HIERARCHY.values()
    )

    products_per_subcategory = max(
        11,
        int(NUM_PRODUCTS / total_subcategories)
    )

    for category, subcategories in PRODUCT_HIERARCHY.items():

        for subcategory in subcategories:

            for _ in range(products_per_subcategory):

                if product_id > NUM_PRODUCTS:
                    break

                brand = random.choice(
                    CATEGORY_BRANDS[category]
                )

                supplier = random.choice(
                    SUPPLIERS
                )

                min_price, max_price = get_price_range(
                    category
                )

                selling_price = round(
                    random.uniform(
                        min_price,
                        max_price
                    ),
                    2
                )

                cost_price = round(
                    selling_price *
                    random.uniform(
                        0.60,
                        0.85
                    ),
                    2
                )

                launch_date = fake.date_between(
                    start_date="-5y",
                    end_date="today"
                )

                # Product Model Selection

                if subcategory in PRODUCT_MODELS:

                    model = random.choice(
                        PRODUCT_MODELS[subcategory]
                    )

                else:

                    model = (
                        f"Model {random.randint(100,999)}"
                    )

                product_name = (
                    f"{brand} {model}"
                )

                # Ensure uniqueness

                original_name = product_name

                counter = 1

                while product_name in used_product_names:

                    product_name = (
                        f"{original_name} {counter}"
                    )

                    counter += 1

                used_product_names.add(
                    product_name
                )

                sku = generate_sku(
                    category,
                    subcategory,
                    product_id
                )

                products.append({

                    "product_id": product_id,

                    "sku": sku,

                    "product_name": product_name,

                    "category": category,

                    "subcategory": subcategory,

                    "brand": brand,

                    "supplier_name": supplier,

                    "price": selling_price,

                    "cost_price": cost_price,

                    "launch_date": launch_date,

                    "created_date": launch_date,

                    "updated_date": launch_date

                })

                product_id += 1

            if product_id > NUM_PRODUCTS:
                break

        if product_id > NUM_PRODUCTS:
            break

    products_df = pd.DataFrame(products)

    # ==========================================
    # NEGATIVE PRICE SIMULATION
    # ==========================================

    negative_price_count = get_dq_sample_size(len(products_df),DATA_QUALITY_RULES["negative_price_pct"])

    negative_price_indices = random.sample(list(products_df.index),negative_price_count)

    products_df.loc[negative_price_indices,"price"] = (products_df.loc[negative_price_indices,"price"]* -1)

    print(f"Negative Prices Injected: {negative_price_count}")

    # ==========================================
    # DUPLICATE PRODUCT ID SIMULATION
    # ==========================================

    duplicate_product_count = get_dq_sample_size(len(products_df),DATA_QUALITY_RULES["duplicate_product_id_pct"])

    duplicate_product_indices = random.sample(list(products_df.index),duplicate_product_count)

    for idx in duplicate_product_indices:

        source_idx = random.choice(list(products_df.index))

        products_df.loc[idx,"product_id"] = products_df.loc[source_idx,"product_id"]

    print(f"Duplicate Product IDs Injected: {duplicate_product_count}")



    #products_df.to_csv(MASTER_DIR / "products.csv",index=False)
    save_dataset(
    products_df,
    dataset_name="products",
    destination="datasets"
    )

    save_dataset(
        products_df,
        dataset_name="products",
        destination="retail_source"
    )

    #print(f"Products generated: "f"{len(products_df):,}")
    logger.info(f"Products generated: {len(products_df):,}")
  
#generate stores
def generate_stores():

    stores = []

    cities = list(
        CITY_STATE_MAP.keys()
    )

    used_store_names = set()

    for store_id in range(
        1,
        NUM_STORES + 1
    ):

        city = random.choice(cities)

        state = CITY_STATE_MAP[city]

        store_brand = random.choice(
            STORE_BRANDS
        )

        store_name = (
            f"{store_brand} {city}"
        )

        if store_name in used_store_names:

            store_name = (
                f"{store_name} {store_id}"
            )

        used_store_names.add(
            store_name
        )

        gender = random.choice(
            ["Male", "Female"]
        )

        if gender == "Male":

            first_name = random.choice(
                MALE_FIRST_NAMES
            )

        else:

            first_name = random.choice(
                FEMALE_FIRST_NAMES
            )

        last_name = random.choice(
            LAST_NAMES
        )

        manager_name = (
            f"{first_name} {last_name}"
        )

        opened_date = fake.date_between(
            start_date="-10y",
            end_date="today"
        )

        stores.append({

            "store_id": store_id,

            "store_name": store_name,

            "city": city,

            "state": state,

            "country": "India",

            "store_type": random.choice(
                STORE_TYPES
            ),

            "opened_date": opened_date,

            "manager_name": manager_name,

            "created_date": opened_date,

            "updated_date": opened_date

        })

    stores_df = pd.DataFrame(
        stores
    )

    # stores_df.to_csv(
    #     MASTER_DIR / "stores.csv",
    #     index=False
    # )
    save_dataset(
    stores_df,
    dataset_name="stores",
    destination="datasets"
    )

    save_dataset(
        stores_df,
        dataset_name="stores",
        destination="retail_source"
    )

    #print(f"Stores generated: "f"{len(stores_df):,}")
    logger.info(f"Stores generated: "f"{len(stores_df):,}")

# ==========================================
# ORDER GENERATION
# ==========================================

def generate_incremental_orders():

    orders_file = (TRANSACTION_DIR /"orders.csv")

    orders_df = pd.read_csv(orders_file)

    customers_df = pd.read_csv(MASTER_DIR /"customers.csv")

    stores_df = pd.read_csv(MASTER_DIR /"stores.csv")

    watermark = load_watermark()

    last_load_date = datetime.strptime(watermark["last_load_date"],"%Y-%m-%d").date()

    incremental_order_date = (last_load_date+ timedelta(days=1))

    new_order_count = (random.randint(3000,8000))

    max_order_id = (orders_df["order_id"].max())

    customer_pool = []

    segment_weights = {
        "Bronze": 1,
        "Silver": 2,
        "Gold": 3,
        "Platinum": 5
    }

    for _, row in customers_df.iterrows():

        weight = segment_weights.get(row["customer_segment"],1)

        customer_pool.extend([row["customer_id"]] * weight)

    store_ids = (stores_df["store_id"].tolist())

    incremental_orders = []

    for i in range(1,new_order_count + 1):

        order_id = (max_order_id + i)

        customer_id = random.choice(customer_pool)

        store_id = random.choice(store_ids)

        order_status = (get_order_status())

        payment_method = (get_payment_method())

        order_total = round(random.uniform(500, 15000),2)

        created_timestamp = datetime.now()

        updated_timestamp = created_timestamp

        incremental_orders.append(
            [
                order_id,
                customer_id,
                store_id,
                incremental_order_date,
                order_status,
                payment_method,
                order_total,
                created_timestamp,
                updated_timestamp
            ]
        )

    incremental_df = pd.DataFrame(incremental_orders,
        columns=[
            "order_id",
            "customer_id",
            "store_id",
            "order_date",
            "order_status",
            "payment_method",
            "order_total",
            "created_timestamp",
            "updated_timestamp"
        ])
    
    #incremental_df.to_csv(TRANSACTION_DIR /"orders_incremental.csv",index=False)
    save_dataset(
    incremental_df,
    dataset_name="orders",
    destination="datasets",
    load_type="incremental"
    )

    save_dataset(
        incremental_df,
        dataset_name="orders",
        destination="retail_source",
        load_type="incremental"
    )

    updated_orders = pd.concat([orders_df,incremental_df],ignore_index=True)

    updated_orders.to_csv(orders_file,index=False)

    #print(f"New Orders Generated: "f"{new_order_count:,}")
    logger.info(f"New Orders Generated: "f"{new_order_count:,}")

def generate_incremental_order_items():

    orders_inc_df = pd.read_csv(
        TRANSACTION_DIR / "orders_incremental.csv"
    )

    products_df = pd.read_csv(
        MASTER_DIR / "products.csv"
    )

    order_items_file = (
        TRANSACTION_DIR / "order_items.csv"
    )

    order_items_df = pd.read_csv(
        order_items_file
    )

    max_order_item_id = (
        order_items_df["order_item_id"]
        .max()
    )

    incremental_order_items = []

    next_item_id = max_order_item_id + 1

    for _, order in orders_inc_df.iterrows():

        order_id = order["order_id"]

        item_count = random.randint(1, 5)

        for _ in range(item_count):

            product = (
                products_df
                .sample(1)
                .iloc[0]
            )

            product_id = product["product_id"]

            quantity = random.randint(1, 3)

            unit_price = product["price"]

            discount = random.choice(DISCOUNTS)

            discount_amount = unit_price * discount

            line_total = round((unit_price - discount_amount)* quantity,2)

            created_timestamp = datetime.now()

            updated_timestamp = created_timestamp

            incremental_order_items.append(
                [
                    next_item_id,
                    order_id,
                    product_id,
                    quantity,
                    unit_price,
                    discount,
                    line_total,
                    created_timestamp,
                    updated_timestamp
                ]
            )

            next_item_id += 1

    incremental_items_df = pd.DataFrame(
        incremental_order_items,
        columns=[
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price",
            "discount",
            "line_total",
            "created_timestamp",
            "updated_timestamp"
        ]
    )

    # incremental_items_df.to_csv(
    #     TRANSACTION_DIR /
    #     "order_items_incremental.csv",
    #     index=False
    # )

    updated_items_df = pd.concat(
        [
            order_items_df,
            incremental_items_df
        ],
        ignore_index=True
    )

    updated_items_df.to_csv(
        order_items_file,
        index=False
    )

    save_dataset(
    incremental_items_df,
    dataset_name="order_items",
    destination="datasets",
    load_type="incremental"
    )

    save_dataset(
        incremental_items_df,
        dataset_name="order_items",
        destination="retail_source",
        load_type="incremental"
    )

    #print(f"New Order Items Generated: "f"{len(incremental_items_df):,}")
    logger.info(f"New Order Items Generated: "f"{len(incremental_items_df):,}")       

def generate_orders_and_items():

    customers_df = pd.read_csv(MASTER_DIR / "customers.csv")

    SEGMENT_WEIGHTS = {
        "Bronze": 1,
        "Silver": 2,
        "Gold": 3,
        "Platinum": 5
    }
    
    products_df = pd.read_csv(MASTER_DIR / "products.csv")

    stores_df = pd.read_csv(MASTER_DIR / "stores.csv")

    CITY_WEIGHTS = {
        "Mumbai": 15,
        "Bangalore": 15,
        "Hyderabad": 12,
        "Delhi": 12,
        "Chennai": 8,
        "Pune": 8
    }

    weighted_customers = []
    for _, row in customers_df.iterrows():
        weight = SEGMENT_WEIGHTS[row["customer_segment"]]
        weighted_customers.extend([row["customer_id"]] * weight)


    product_ids = (products_df["product_id"].tolist())

    TOP_PRODUCT_PERCENT = 0.20

    top_product_count = int(
        len(product_ids)
        * TOP_PRODUCT_PERCENT
    )

    top_products = product_ids[
        :top_product_count
    ]

    remaining_products = product_ids[
        top_product_count:
    ]

    weighted_products = (
        top_products * 3
        +
        remaining_products * 1
    )

    store_ids = (stores_df["store_id"].tolist())

    weighted_stores = []
    for _, row in stores_df.iterrows():
        city = row["city"]
        weight = CITY_WEIGHTS.get(city,2)
        weighted_stores.extend([row["store_id"]] * weight)

    product_price_lookup = dict(
        zip(
            products_df["product_id"],
            products_df["price"]
        )
    )

    orders = []

    order_items = []

    order_item_id = 1

    for order_id in range(
        1,
        INITIAL_ORDERS + 1
    ):

        order_timestamp = (generate_order_timestamp())

        order_status = (get_order_status())

        payment_method = get_payment_method()

        customer_id = (random.choice(weighted_customers))

        store_id = (random.choice(weighted_stores))

        number_of_items = (random.randint(1, 5))

        selected_products = []
        while len(selected_products) < number_of_items:
            product = random.choice(weighted_products)

            if product not in selected_products:
                selected_products.append(product)

        order_total = 0

        for product_id in selected_products:

            quantity = random.randint(1, 5)

            if random.random() < DATA_QUALITY_RULES["negative_quantity_pct"]:
                quantity = quantity * -1

            #original_product_id = product_id

            unit_price = (product_price_lookup[product_id])

            if random.random() < DATA_QUALITY_RULES["invalid_product_id_pct"]:
                product_id = f"P{random.randint(900000,999999)}"

            discount = random.choice(
                DISCOUNTS
            )

            line_total = round(
                quantity *
                unit_price *
                (1 - discount),
                2
            )

            order_total += line_total

            order_items.append({

                "order_item_id":
                    order_item_id,

                "order_id":
                    order_id,

                "product_id":
                    product_id,

                "quantity":
                    quantity,

                "unit_price":
                    unit_price,

                "discount":
                    discount,

                "line_total":
                    line_total,

                "created_timestamp":
                    order_timestamp,

                "updated_timestamp":
                    order_timestamp

            })

            order_item_id += 1

        orders.append({

            "order_id":
                order_id,

            "customer_id":
                customer_id,

            "store_id":
                store_id,

            "order_date":
                order_timestamp.date(),

            "order_status":
                order_status,

            "payment_method":
                payment_method,

            "order_total":
                round(order_total, 2),

            "created_timestamp":
                order_timestamp,

            "updated_timestamp":
                order_timestamp

        })

    orders_df = pd.DataFrame(orders)

    # ==========================================
    # INVALID PAYMENT METHOD SIMULATION
    # ==========================================

    invalid_payment_count = get_dq_sample_size(len(orders_df),DATA_QUALITY_RULES["invalid_payment_method_pct"])

    invalid_payment_indices = random.sample(list(orders_df.index),invalid_payment_count)

    for idx in invalid_payment_indices:
        orders_df.loc[idx,"payment_method"] = random.choice(INVALID_PAYMENT_METHODS)

    print(f"Invalid Payment Methods Injected: {invalid_payment_count}")


    # ==========================================
    # FUTURE ORDER DATE SIMULATION
    # ==========================================

    future_order_count = get_dq_sample_size(len(orders_df),DATA_QUALITY_RULES["future_order_date_pct"])

    future_order_indices = random.sample(list(orders_df.index),future_order_count)

    for idx in future_order_indices:
        future_date = (datetime.today()+ timedelta(days=random.randint(1, 30))).date()

        orders_df.loc[idx,"order_date"] = future_date

    print(f"Future Order Dates Injected: {future_order_count}")

    # ==========================================
    # MISSING CUSTOMER ID SIMULATION
    # ==========================================

    missing_customer_count = get_dq_sample_size(len(orders_df),DATA_QUALITY_RULES["missing_customer_id_pct"])

    missing_customer_indices = random.sample(list(orders_df.index),missing_customer_count)

    orders_df.loc[missing_customer_indices,"customer_id"] = None

    print(f"Missing Customer IDs Injected: {missing_customer_count}")



    order_items_df = pd.DataFrame(order_items)

    #orders_df.to_csv(TRANSACTION_DIR / "orders.csv",index=False)
    #order_items_df.to_csv(TRANSACTION_DIR /"order_items.csv",index=False)

    save_dataset(
    orders_df,
    dataset_name="orders",
    destination="datasets"
    )

    save_dataset(
        orders_df,
        dataset_name="orders",
        destination="retail_source",
        load_type="full_load"
    )

    save_dataset(
    order_items_df,
    dataset_name="order_items",
    destination="datasets"
    )

    save_dataset(
        order_items_df,
        dataset_name="order_items",
        destination="retail_source",
        load_type="full_load"
    )

    #print(f"Orders generated: "f"{len(orders_df):,}")
    logger.info(f"Orders generated: {len(orders_df):,}")

    #print(f"Order Items generated: "f"{len(order_items_df):,}")
    logger.info(f"Order Items generated: {len(order_items_df):,}")


def run_validation():

    customers_inc = pd.read_csv(MASTER_DIR /"customers_incremental.csv")

    orders_inc = pd.read_csv(TRANSACTION_DIR /"orders_incremental.csv")

    order_items_inc = pd.read_csv(TRANSACTION_DIR /"order_items_incremental.csv")

    assert (customers_inc["customer_id"].isnull().sum()== 0)

    assert (orders_inc["order_id"].is_unique)

    assert (order_items_inc["order_item_id"].is_unique)

    print("\nValidation Passed")

def generate_data_quality_report():
    from datetime import datetime

    customers_df = pd.read_csv(MASTER_DIR / "customers.csv")
    products_df = pd.read_csv(MASTER_DIR / "products.csv")
    orders_df = pd.read_csv(TRANSACTION_DIR / "orders.csv")
    order_items_df = pd.read_csv(TRANSACTION_DIR / "order_items.csv")


    # ==========================================
    # CUSTOMER METRICS
    # ==========================================

    null_emails = (customers_df["email"].isna().sum())
    duplicate_phones = (customers_df["phone"].duplicated().sum())
    missing_cities = (customers_df["city"].isna().sum())


    # ==========================================
    # PRODUCT METRICS
    # ==========================================   

    negative_prices = (products_df["price"] < 0).sum()

    duplicate_products = (products_df["product_id"].duplicated().sum())

    # ==========================================
    # ORDER METRICS
    # ==========================================

    invalid_payments = (~orders_df["payment_method"].isin(PAYMENT_METHODS)).sum()

    future_orders = (pd.to_datetime(orders_df["order_date"]).dt.date > datetime.today().date()).sum()

    missing_customer_ids = (orders_df["customer_id"].isna().sum())

    # ==========================================
    # ORDER ITEM METRICS
    # ==========================================

    negative_quantities = (order_items_df["quantity"] < 0).sum()

    valid_products = set(products_df["product_id"].astype(str))

    invalid_product_ids = (~order_items_df["product_id"].astype(str).isin(valid_products)).sum()


    customer_total = len(customers_df)
    product_total = len(products_df)
    order_total = len(orders_df)
    order_item_total = len(order_items_df)
    
    customer_defects = (
        null_emails
        + duplicate_phones
        + missing_cities
    )

    product_defects = (
        negative_prices
        + duplicate_products
    )

    order_defects = (
        invalid_payments
        + future_orders
        + missing_customer_ids
    )

    order_item_defects = (
        negative_quantities
        + invalid_product_ids
    )

    customer_quality_score = round(
        (
            (customer_total - customer_defects)
            / customer_total
        ) * 100,
        2
    )

    product_quality_score = round(
        (
            (product_total - product_defects)
            / product_total
        ) * 100,
        2
    )

    order_quality_score = round(
        (
            (order_total - order_defects)
            / order_total
        ) * 100,
        2
    )

    order_item_quality_score = round(
        (
            (order_item_total - order_item_defects)
            / order_item_total
        ) * 100,
        2
    )

    customer_status = (
        "PASS"
        if customer_quality_score >= 95
        else "FAIL"
    )

    product_status = (
        "PASS"
        if product_quality_score >= 95
        else "FAIL"
    )

    order_status = (
        "PASS"
        if order_quality_score >= 95
        else "FAIL"
    )

    order_item_status = (
        "PASS"
        if order_item_quality_score >= 95
        else "FAIL"
    )

    # ==========================================
    # OVERALL PLATFORM QUALITY
    # ==========================================

    overall_records = (
        customer_total
        + product_total
        + order_total
        + order_item_total
    )

    overall_defects = (
        customer_defects
        + product_defects
        + order_defects
        + order_item_defects
    )

    overall_quality_score = round(
        (
            (overall_records - overall_defects)
            / overall_records
        ) * 100,
        2
    )

    overall_status = (
        "PASS"
        if overall_quality_score >= 95
        else "FAIL"
    )

    # ==========================================
    # REPORT
    # ==========================================

    report = f"""
=====================================
DATA QUALITY REPORT
=====================================

Report Generated:
{datetime.now()}

-------------------------------------
CUSTOMERS
-------------------------------------

Total Records: {customer_total}

Null Emails: {null_emails}
Duplicate Phones: {duplicate_phones}
Missing Cities: {missing_cities}

Total Defects: {customer_defects}

Quality Score: {customer_quality_score}%

Status: {customer_status}

-------------------------------------
PRODUCTS
-------------------------------------

Total Records: {product_total}

Negative Prices: {negative_prices}
Duplicate Product IDs: {duplicate_products}

Total Defects: {product_defects}

Quality Score: {product_quality_score}%

Status: {product_status}

-------------------------------------
ORDERS
-------------------------------------

Total Records: {order_total}

Invalid Payment Methods: {invalid_payments}
Future Order Dates: {future_orders}
Missing Customer IDs: {missing_customer_ids}

Total Defects: {order_defects}

Quality Score: {order_quality_score}%

Status: {order_status}

-------------------------------------
ORDER ITEMS
-------------------------------------

Total Records: {order_item_total}

Negative Quantities: {negative_quantities}
Invalid Product IDs: {invalid_product_ids}

Total Defects: {order_item_defects}

Quality Score: {order_item_quality_score}%

Status: {order_item_status}

=====================================
OVERALL PLATFORM QUALITY
=====================================

Total Records: {overall_records}

Total Defects: {overall_defects}

Quality Score: {overall_quality_score}%

Status: {overall_status}
"""

    report_file = LOG_DIR / "data_quality_report.txt"

    with open(report_file, "w") as file:
        file.write(report)

    #print("Data Quality Report Generated Successfully")
    logger.info("Data Quality Report Generated Successfully")

def run_full_load():
    generate_customers()
    generate_products()
    generate_stores()
    generate_orders_and_items()
    generate_data_quality_report()
    
    update_watermark(datetime.today().date())

    print("\nFull load completed.")

def run_incremental_load():
    generate_incremental_customers()
    generate_incremental_orders()
    generate_incremental_order_items()
    run_validation()
    update_incremental_watermark()

    print("\nIncremental Load Completed")


if __name__ == "__main__":
    #run_full_load()
    initialize_project()

    mode = (
        sys.argv[1].lower()
        if len(sys.argv) > 1
        else "full"
    )

    if mode == "full":
        run_full_load()

    elif mode == "incremental":
        run_incremental_load()

    elif mode == "validate":
        run_validation()

    else:
        print(
            "Invalid mode"
        )

    print("Data Quality Framework Loaded Successfully")

    #print(DATA_QUALITY_RULES)

    #print(get_dq_sample_size(5000,DATA_QUALITY_RULES["null_email_pct"]))