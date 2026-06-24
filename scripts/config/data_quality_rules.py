DATA_QUALITY_RULES = {
    # Customer Issues
    "null_email_pct": 0.02,
    "duplicate_phone_pct": 0.01,
    "missing_city_pct": 0.01,

    # Product Issues
    "negative_price_pct": 0.005,
    "duplicate_product_id_pct": 0.002,

    # Order Issues
    "invalid_payment_method_pct": 0.01,
    "future_order_date_pct": 0.005,
    "missing_customer_id_pct": 0.005,

    # Order Item Issues
    "negative_quantity_pct": 0.005,
    "invalid_product_id_pct": 0.005
}

INVALID_PAYMENT_METHODS = [
    "Crypto",
    "Cheque",
    "Voucher",
    "WalletX",
    "Test"
]
