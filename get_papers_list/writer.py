import csv
from typing import List, Dict

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    keys = data[0].keys() if data else []
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)