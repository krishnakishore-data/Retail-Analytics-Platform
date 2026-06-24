import random
from datetime import (datetime, timedelta)
from config.constants import *

#sku genertaor
def generate_sku(category, subcategory, product_id):

    category_code = {
        "Electronics": "ELE",
        "Clothing": "CLO",
        "Home & Kitchen": "HOM",
        "Sports & Fitness": "SPO",
        "Beauty & Personal Care": "BEA"
    }

    subcategory_code = "".join(
        word[:3].upper()
        for word in subcategory.split()[:1]
    )

    return (
        f"{category_code[category]}-"
        f"{subcategory_code}-"
        f"{str(product_id).zfill(4)}"
    )

#price generator
def get_price_range(category):

    ranges = {
        "Electronics": (2000, 80000),
        "Clothing": (300, 5000),
        "Home & Kitchen": (500, 30000),
        "Sports & Fitness": (200, 15000),
        "Beauty & Personal Care": (100, 4000)
    }

    return ranges[category]

#Weighted Order Status
def get_order_status():

    return random.choices(
        population=[
            "Delivered",
            "Shipped",
            "Processing",
            "Cancelled",
            "Returned"
        ],
        weights=[
            75,
            10,
            8,
            5,
            2
        ],
        k=1
    )[0]

def get_payment_method():

    return random.choices(
        population=list(
            PAYMENT_METHOD_WEIGHTS.keys()
        ),
        weights=list(
            PAYMENT_METHOD_WEIGHTS.values()
        ),
        k=1
    )[0]

#helper functions
def generate_order_timestamp():

    start_date = datetime(
        2024,
        1,
        1
    )

    end_date = datetime.now()

    time_between = (
        end_date - start_date
    )

    random_seconds = random.randint(
        0,
        int(time_between.total_seconds())
    )

    return (
        start_date +
        timedelta(
            seconds=random_seconds
        )
    )

# ==========================================
# DATA QUALITY SIMULATION CONFIGURATION
# ==========================================
def get_dq_sample_size(total_records, percentage):
    return max(1,int(total_records * percentage))
