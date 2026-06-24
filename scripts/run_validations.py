from validation.business_validation import *
from validation.incremental_validation import *


def main():
    #business_validation
    validate_payment_distribution()
    validate_customer_segments()
    validate_city_distribution()
    validate_pareto_sales()

    #incremental_validation
    validate_incremental_customers()
    validate_incremental_orders()
    validate_incremental_order_items()


if __name__ == "__main__":
    main()