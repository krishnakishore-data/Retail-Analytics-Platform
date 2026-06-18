import pandas as pd
import numpy as np
import random
import sys
from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta

fake = Faker("en_IN")

BASE_DIR = Path(__file__).resolve().parent.parent

MASTER_DIR = BASE_DIR / "datasets" / "master"
TRANSACTION_DIR = BASE_DIR / "datasets" / "transactions"
LOG_DIR = BASE_DIR / "logs"

MASTER_DIR.mkdir(parents=True, exist_ok=True)
TRANSACTION_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 500
NUM_STORES = 50

INITIAL_ORDERS = 50000
MIN_INCREMENTAL_ORDERS = 3000
MAX_INCREMENTAL_ORDERS = 8000

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5

# business dictionaries 

PRODUCT_HIERARCHY = {

    "Electronics": [
        "Mobile Phone",
        "Laptop",
        "Tablet",
        "Smart Watch",
        "Headphone",
        "Accessorie",
        "Camera",
        "Gaming Console"
    ],

    "Clothing": [
        "Men T-Shirts",
        "Men Shirts",
        "Men Jeans",
        "Men Trousers",
        "Men Jackets",
        "Men Ethnic Wear",
        "Men Footwear",
        "Men Sportswear",

        "Women Dresses",
        "Tops",
        "Women Jeans",
        "Kurtis",
        "Sarees",
        "Women Jackets",
        "Women Footwear",
        "Women Activewear",

        "Kids Clothing",
        "Kids Footwear",
        "Kids Winter Wear"
    ],

    "Home & Kitchen": [
        "Furniture",
        "Cookware",
        "Kitchen Appliances",
        "Home Decor",
        "Storage & Organization",
        "Bedding",
        "Dining Essentials",
        "Cleaning Supplies"
    ],

    "Sports & Fitness": [
        "Fitness Equipment",
        "Outdoor Sports",
        "Indoor Games",
        "Yoga Accessories",
        "Cycling",
        "Running Gear",
        "Cricket Equipment"
    ],

    "Beauty & Personal Care": [
        "Skincare",
        "Haircare",
        "Cosmetics",
        "Fragrances",
        "Personal Hygiene",
        "Men Grooming",
        "Beauty Tools"
    ]
}

PRODUCT_MODELS = {

    # Electronics

    "Mobile Phones": [
        "Galaxy M35","Galaxy S24","iPhone 15","iPhone 16",
        "OnePlus 13","Nord CE4","Redmi Note 14","Vivo V50",
        "Realme GT","Pixel 9"
    ],

    "Laptops": [
        "Inspiron 15","Pavilion 14","ThinkPad E14",
        "Vivobook 15","Swift Go","MacBook Air M4",
        "IdeaPad Slim","Zenbook 14","Latitude 5440",
        "Aspire Lite"
    ],

    "Tablets": [
        "Galaxy Tab S9","iPad Air","Pad 7",
        "Tab M10","MatePad","Redmi Pad Pro"
    ],

    "Smart Watches": [
        "Watch Ultra","Watch Fit","Fit Pro",
        "Pulse Max","Active Watch","Smart Watch X"
    ],

    "Headphones": [
        "Rockerz 255","AirPods Pro","WH1000XM5",
        "Buds Air","Noise Pods","Neckband X"
    ],

    "Accessories": [
        "Power Bank","Fast Charger","USB Hub",
        "Wireless Charger","Bluetooth Adapter",
        "Laptop Sleeve"
    ],

    "Cameras": [
        "Alpha A6700","EOS R10","D7500",
        "Insta360 X4","Hero 13","Mirrorless Pro"
    ],

    "Gaming Consoles": [
        "PlayStation 5","Xbox Series X",
        "Nintendo Switch","Gaming Console Pro"
    ],

    # Clothing - Men

    "Men T-Shirts": [
        "Crew Neck Tee","Graphic Tee",
        "Polo Tee","Athletic Tee","Solid Tee"
    ],

    "Men Shirts": [
        "Formal Shirt","Casual Shirt",
        "Linen Shirt","Slim Fit Shirt",
        "Checked Shirt"
    ],

    "Men Jeans": [
        "Slim Fit Jeans","Regular Fit Jeans",
        "Stretch Jeans","Skinny Jeans"
    ],

    "Men Trousers": [
        "Formal Trouser","Chino Pants",
        "Cotton Trouser","Stretch Trouser"
    ],

    "Men Jackets": [
        "Bomber Jacket","Denim Jacket",
        "Winter Jacket","Hooded Jacket"
    ],

    "Men Ethnic Wear": [
        "Kurta Set","Sherwani",
        "Ethnic Kurta","Nehru Jacket"
    ],

    "Men Footwear": [
        "Running Shoes","Formal Shoes",
        "Sneakers","Sports Shoes",
        "Slip On Shoes"
    ],

    "Men Sportswear": [
        "Track Pant","Training Shorts",
        "Sports T-Shirt","Gym Vest"
    ],

    # Clothing - Women

    "Women Dresses": [
        "Summer Dress","Floral Dress",
        "Party Dress","Maxi Dress"
    ],

    "Women Tops": [
        "Casual Top","Printed Top",
        "Crop Top","Cotton Top"
    ],

    "Women Jeans": [
        "Skinny Jeans","Mom Fit Jeans",
        "High Rise Jeans","Regular Jeans"
    ],

    "Women Kurtis": [
        "Cotton Kurti","Printed Kurti",
        "Anarkali Kurti","Straight Kurti"
    ],

    "Women Sarees": [
        "Silk Saree","Cotton Saree",
        "Designer Saree","Festive Saree"
    ],

    "Women Jackets": [
        "Winter Jacket","Denim Jacket",
        "Long Coat","Casual Jacket"
    ],

    "Women Footwear": [
        "Sandals","Heels",
        "Flats","Sports Shoes"
    ],

    "Women Activewear": [
        "Yoga Pants","Sports Bra",
        "Training Tights","Workout Top"
    ],

    # Kids

    "Kids Clothing": [
        "Kids T-Shirt","Kids Shirt",
        "Kids Shorts","Kids Jeans"
    ],

    "Kids Footwear": [
        "Kids Sneakers","Kids Sandals",
        "Kids School Shoes"
    ],

    "Kids Winter Wear": [
        "Kids Sweater","Kids Jacket",
        "Kids Hoodie"
    ],

    # Home & Kitchen

    "Furniture": [
        "Office Chair","Dining Table",
        "Sofa Set","Study Table"
    ],

    "Cookware": [
        "Deluxe Cookware Set","Pressure Cooker",
        "Non Stick Pan","Steel Cookware Set"
    ],

    "Kitchen Appliances": [
        "Mixer Grinder","Air Fryer",
        "Microwave Oven","Induction Cooktop"
    ],

    "Home Decor": [
        "Wall Art","Decor Lamp",
        "Indoor Plant Pot","Photo Frame"
    ],

    "Storage & Organization": [
        "Storage Box","Wardrobe Organizer",
        "Drawer Unit","Shoe Rack"
    ],

    "Bedding": [
        "Bedsheet Set","Comforter",
        "Blanket","Pillow Set"
    ],

    "Dining Essentials": [
        "Dinner Set","Serving Bowl",
        "Cutlery Set","Glass Set"
    ],

    "Cleaning Supplies": [
        "Floor Cleaner","Cleaning Kit",
        "Mop Set","Surface Cleaner"
    ],

    # Sports & Fitness

    "Fitness Equipment": [
        "Dumbbell Set","Exercise Bike",
        "Treadmill","Resistance Bands"
    ],

    "Outdoor Sports": [
        "Football","Basketball",
        "Volleyball","Badminton Set"
    ],

    "Indoor Games": [
        "Chess Board","Carrom Board",
        "Table Tennis Set","Ludo Set"
    ],

    "Yoga Accessories": [
        "Yoga Mat","Yoga Block",
        "Yoga Strap","Meditation Cushion"
    ],

    "Cycling": [
        "Mountain Bike","Road Bike",
        "Cycling Helmet","Bike Gloves"
    ],

    "Running Gear": [
        "Running Shoes","Running Shorts",
        "Sports Watch","Hydration Belt"
    ],

    "Cricket Equipment": [
        "English Willow Bat","Cricket Kit",
        "Batting Gloves","Helmet Pro"
    ],

    # Beauty & Personal Care

    "Skincare": [
        "Vitamin C Face Wash",
        "Daily Moisturizer",
        "Sunscreen SPF50",
        "Aloe Vera Gel"
    ],

    "Haircare": [
        "Anti Hairfall Shampoo",
        "Hair Serum",
        "Hair Oil",
        "Conditioner Plus"
    ],

    "Cosmetics": [
        "Matte Lipstick",
        "Foundation Cream",
        "Compact Powder",
        "Eye Liner"
    ],

    "Fragrances": [
        "Body Mist",
        "Perfume Spray",
        "Deodorant",
        "Luxury Perfume"
    ],

    "Personal Hygiene": [
        "Hand Wash",
        "Body Wash",
        "Sanitizer",
        "Soap Bar"
    ],

    "Men Grooming": [
        "Beard Oil",
        "Shaving Kit",
        "Face Scrub",
        "Trimmer Kit"
    ],

    "Beauty Tools": [
        "Hair Dryer",
        "Straightener",
        "Makeup Brush Set",
        "Facial Roller"
    ]
}

#supporting lists
STORE_TYPES = [
    "Mall",
    "Standalone",
    "Online Fulfillment",
    "Airport"
]

CUSTOMER_SEGMENTS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

DISCOUNTS = [
    0.00,
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30
]

EMAIL_DOMAINS = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com"
]

LAST_NAMES = [
    "Sharma",
    "Reddy",
    "Patel",
    "Gupta",
    "Singh",
    "Verma",
    "Rao",
    "Nair",
    "Iyer",
    "Agarwal",
    "Jain",
    "Yadav",
    "Mishra",
    "Pandey",
    "Kumar",
    "Das",
    "Mehta",
    "Choudhary",
    "Joshi",
    "Kapoor",
    "Bhat",
    "Kulkarni",
    "Pillai",
    "Shetty",
    "Chatterjee"
]

MALE_FIRST_NAMES = [
"Rahul","Arjun","Vikram","Krishna","Sai",
"Karthik","Pranav","Aditya","Akash","Rohit",
"Abhishek","Ankit","Amit","Sandeep","Naveen",
"Harsha","Varun","Tarun","Manoj","Rajesh",
"Vivek","Deepak","Suresh","Ramesh","Ganesh",
"Surya","Mahesh","Nikhil","Ashwin","Ajay",
"Vijay","Raghav","Mohan","Lokesh","Naresh",
"Vinay","Yash","Arnav","Dhruv","Shreyas",
"Tejas","Ritik","Kunal","Pavan","Srinivas",
"Balaji","Madhav","Anand","Shiva","Vamsi",
"Satish","Prakash","Bhanu","Chandra","Rishi",
"Pradeep","Ranjith","Gokul","Dinesh","Murali",
"Jagadeesh","Kiran","Santosh","Ravindra","Rohit",
"Rakesh","Siddharth","Uday","Venkat","Yogesh",
"Zubair","Imran","Faizan","Ayaan","Rehan"
]

FEMALE_FIRST_NAMES = [
"Priya","Ananya","Sneha","Pooja","Lakshmi",
"Divya","Meera","Kavya","Aishwarya","Nandini",
"Deepika","Shreya","Neha","Ritu","Swathi",
"Harika","Bhavya","Sravani","Keerthana","Anusha",
"Madhuri","Jyothi","Pallavi","Sushmita","Rashmi",
"Preethi","Vaishnavi","Sowmya","Monika","Komal",
"Ritika","Khushi","Ishita","Diya","Aditi",
"Shruti","Pavithra","Amrutha","Chandana","Anjali",
"Pragya","Rani","Mounika","Geetha","Sarika",
"Sangeetha","Padma","Vani","Uma","Revathi",
"Reshma","Niharika","Tanya","Madhavi","Manasa",
"Anupama","Archana","Bindu","Harini","Kalyani",
"Navya","Sanjana","Trisha","Yamini","Zara",
"Farah","Ayesha","Sana","Nazia","Hina",
"Rekha","Latha","Bhargavi","Tejaswini","Indu"
]

CITY_STATE_MAP = {

    "Mumbai":"Maharashtra",
    "Pune":"Maharashtra",
    "Nagpur":"Maharashtra",
    "Nashik":"Maharashtra",
    "Aurangabad":"Maharashtra",

    "Hyderabad":"Telangana",
    "Warangal":"Telangana",
    "Karimnagar":"Telangana",

    "Bangalore":"Karnataka",
    "Mysore":"Karnataka",
    "Hubli":"Karnataka",
    "Mangalore":"Karnataka",

    "Chennai":"Tamil Nadu",
    "Coimbatore":"Tamil Nadu",
    "Madurai":"Tamil Nadu",
    "Salem":"Tamil Nadu",

    "Lucknow":"Uttar Pradesh",
    "Kanpur":"Uttar Pradesh",
    "Agra":"Uttar Pradesh",
    "Varanasi":"Uttar Pradesh",

    "Delhi":"Delhi",
    "New Delhi":"Delhi",

    "Jaipur":"Rajasthan",
    "Udaipur":"Rajasthan",

    "Ahmedabad":"Gujarat",
    "Surat":"Gujarat",
    "Vadodara":"Gujarat",

    "Kolkata":"West Bengal",
    "Howrah":"West Bengal",

    "Bhopal":"Madhya Pradesh",
    "Indore":"Madhya Pradesh",

    "Patna":"Bihar",
    "Ranchi":"Jharkhand",

    "Bhubaneswar":"Odisha",
    "Cuttack":"Odisha",

    "Kochi":"Kerala",
    "Thiruvananthapuram":"Kerala",

    "Visakhapatnam":"Andhra Pradesh",
    "Vijayawada":"Andhra Pradesh"
}

CATEGORY_BRANDS = {

    "Electronics": [
        "Samsung","Apple","OnePlus","Xiaomi",
        "Realme","Oppo","Vivo","Lenovo",
        "HP","Dell","Asus","Acer",
        "Sony","LG","Boat"
    ],

    "Clothing": [
        "Levis","Allen Solly","Peter England",
        "Van Heusen","Louis Philippe",
        "Wrogn","US Polo","Zara",
        "H&M","Nike","Adidas",
        "Puma","Roadster","Max",
        "FabIndia"
    ],

    "Home & Kitchen": [
        "Prestige","Pigeon","Butterfly",
        "Hawkins","Ikea","Nilkamal",
        "Godrej","Whirlpool",
        "Philips","Bajaj"
    ],

    "Sports & Fitness": [
        "Nike","Adidas","Puma",
        "Reebok","Yonex",
        "Cosco","Nivia",
        "SG","MRF",
        "Decathlon"
    ],

    "Beauty & Personal Care": [
        "Lakme","Mamaearth",
        "Biotique","Himalaya",
        "Dove","Nivea",
        "Loreal","Maybelline",
        "Nykaa","Ponds"
    ]
}

STORE_BRANDS = [
    "RetailHub",
    "SmartMart",
    "UrbanCart",
    "MegaStore",
    "ShopSphere"
]

SUPPLIERS = [
    "Reliance Retail Supply Chain",
    "Tata Consumer Distribution",
    "Aditya Birla Distribution",
    "Metro Cash and Carry",
    "Redington India",
    "Ingram Micro India",
    "TVS Supply Chain Solutions",
    "Mahindra Logistics",
    "Delhivery Fulfillment",
    "Blue Dart Distribution",
    "Ecom Express Supply Chain",
    "Safexpress Logistics",
    "Allcargo Supply Chain",
    "Snowman Logistics",
    "Future Retail Distribution"
]
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

#helper function
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

#generate_customers
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
            start_date="-60y",
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

    customers_df.to_csv(
        MASTER_DIR / "customers.csv",
        index=False
    )

    print(
        f"Customers generated: {len(customers_df):,}"
    )

#generate products
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

    products_df.to_csv(
        MASTER_DIR / "products.csv",
        index=False
    )

    print(
        f"Products generated: "
        f"{len(products_df):,}"
    )
  
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

    stores_df.to_csv(
        MASTER_DIR / "stores.csv",
        index=False
    )

    print(
        f"Stores generated: "
        f"{len(stores_df):,}"
    )

#generate orders and items
def generate_orders_and_items():

    customers_df = pd.read_csv(
        MASTER_DIR / "customers.csv"
    )

    products_df = pd.read_csv(
        MASTER_DIR / "products.csv"
    )

    stores_df = pd.read_csv(
        MASTER_DIR / "stores.csv"
    )

    customer_ids = (
        customers_df["customer_id"]
        .tolist()
    )

    product_ids = (
        products_df["product_id"]
        .tolist()
    )

    store_ids = (
        stores_df["store_id"]
        .tolist()
    )

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

        order_timestamp = (
            generate_order_timestamp()
        )

        order_status = (
            get_order_status()
        )

        payment_method = (
            random.choice(
                PAYMENT_METHODS
            )
        )

        customer_id = (
            random.choice(
                customer_ids
            )
        )

        store_id = (
            random.choice(
                store_ids
            )
        )

        number_of_items = (
            random.randint(1, 5)
        )

        selected_products = (
            random.sample(
                product_ids,
                min(
                    number_of_items,
                    len(product_ids)
                )
            )
        )

        order_total = 0

        for product_id in selected_products:

            quantity = random.randint(
                1,
                5
            )

            unit_price = (
                product_price_lookup[
                    product_id
                ]
            )

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

    orders_df = pd.DataFrame(
        orders
    )

    order_items_df = pd.DataFrame(
        order_items
    )

    orders_df.to_csv(
        TRANSACTION_DIR / "orders.csv",
        index=False
    )

    order_items_df.to_csv(
        TRANSACTION_DIR /
        "order_items.csv",
        index=False
    )

    print(
        f"Orders generated: "
        f"{len(orders_df):,}"
    )

    print(
        f"Order Items generated: "
        f"{len(order_items_df):,}"
    )

if __name__ == "__main__":

    generate_customers()

    generate_products()

    generate_stores()

    generate_orders_and_items()