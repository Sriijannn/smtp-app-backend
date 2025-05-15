import csv
from io import StringIO
from typing import List, Tuple

def parse_csv_data(csv_text: str) -> List[Tuple[str, str]]:
    """
    Parses CSV string and returns list of (name, email)
    """
    f = StringIO(csv_text)
    reader = csv.DictReader(f)
    return [(row["name"], row["email"]) for row in reader if row.get("email")]
