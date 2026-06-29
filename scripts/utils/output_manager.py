from pathlib import Path

from config.storage_config import OUTPUT_CONFIG

# Dataset metadata
DATASET_CONFIG = {
    "customers": {
        "category": "master",
        "supports_incremental": True,
    },
    "products": {
        "category": "master",
        "supports_incremental": False,
    },
    "stores": {
        "category": "master",
        "supports_incremental": False,
    },
    "orders": {
        "category": "transactions",
        "supports_incremental": True,
    },
    "order_items": {
        "category": "transactions",
        "supports_incremental": True,
    },
}


def save_dataset(df, dataset_name, destination, load_type=None):
    """
    Save a dataframe to either:
        1. datasets (GitHub sample datasets)
        2. Retail_Source (Operational Source System)
    """

    dataset = DATASET_CONFIG[dataset_name]
    category = dataset["category"]

    root = Path(OUTPUT_CONFIG[destination]["root"])

    # -------------------------
    # GitHub datasets structure
    # -------------------------
    if destination == "datasets":

        file_name = (
            f"{dataset_name}_incremental.csv"
            if load_type == "incremental"
            else f"{dataset_name}.csv"
        )

        output_path = root / category / file_name

    # -------------------------
    # Retail Source structure
    # -------------------------
    else:

        if dataset["supports_incremental"]:

            folder = "incremental" if load_type == "incremental" else "full_load"

            file_name = (
                f"{dataset_name}_incremental.csv"
                if load_type == "incremental"
                else f"{dataset_name}.csv"
            )

            output_path = (
                root
                / category
                / dataset_name
                / folder
                / file_name
            )

        else:

            file_name = f"{dataset_name}.csv"

            output_path = (
                root
                / category
                / dataset_name
                / file_name
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Saved -> {output_path}")