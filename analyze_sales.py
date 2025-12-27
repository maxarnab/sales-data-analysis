import json
from typing import Dict, Tuple, List


def load_sales_data(filepath: str) -> Dict[str, Dict[str, int]]:
    """
    Load sales data from a JSON file.
    """
    with open(filepath, "r") as file:
        return json.load(file)


def analyze_sales(sales: Dict[str, Dict[str, int]]) -> Tuple[Dict[str, int], List[str]]:
    """
    Calculate total sales per person and identify high achievers.
    """
    totals = {}

    for month, month_data in sales.items():
        for person, amount in month_data.items():
            totals[person] = totals.get(person, 0) + amount

    high_achievers = [
        person for person, total in totals.items() if total > 600
    ]

    return totals, high_achievers


def main():
    sales_data = load_sales_data("sales.json")
    totals, high_achievers = analyze_sales(sales_data)

    print("Total sales per person:")
    for person, total in totals.items():
        print(f"  {person}: {total}")

    print("\nPeople with sales above 600:")
    for person in high_achievers:
        print(f"  {person}")


if __name__ == "__main__":
    main()
