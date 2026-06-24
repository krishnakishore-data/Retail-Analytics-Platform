
#dataset sizes
NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 500
NUM_STORES = 50

INITIAL_ORDERS = 50000
MIN_INCREMENTAL_ORDERS = 3000
MAX_INCREMENTAL_ORDERS = 8000

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5

#Business dictionaries
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

PAYMENT_METHOD_WEIGHTS = {
    "UPI": 55,
    "Credit Card": 18,
    "Debit Card": 15,
    "Net Banking": 8,
    "Cash": 4
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
