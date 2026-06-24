import json
from datetime import (datetime, timedelta)
from pathlib import Path


WATERMARK_FILE = (Path("logs") / "watermark.json")

def load_watermark(): #fetches the watermark.json file and displays load date
    #watermark_file = (LOG_DIR /"watermark.json")

    if not WATERMARK_FILE.exists():
        return None

    with open(WATERMARK_FILE,"r") as f:
        return json.load(f)

def update_watermark(load_date):
    #watermark_file = (LOG_DIR /"watermark.json")

    with open(WATERMARK_FILE,"w") as f:
        json.dump({"last_load_date":str(load_date)},f,indent=4)


def update_incremental_watermark():

    watermark = (load_watermark())

    last_load_date = (datetime.strptime(watermark["last_load_date"],"%Y-%m-%d").date())

    next_load_date = (last_load_date+ timedelta(days=1))

    update_watermark(next_load_date)

    print(f"Watermark Updated: "f"{next_load_date}")
