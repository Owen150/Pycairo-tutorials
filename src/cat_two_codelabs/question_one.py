import json
from typing import List, Dict, Any


def read_jsonline(filepath: str) -> List[Dict[str, Any]]:
    shape_coordinates = []

    with open(filepath, 'r') as file:
        data = json.load(file)
        shape_coordinates.extend(data)

    return shape_coordinates


# Test the function
test_file_path = "test.json"
coordinates = read_jsonline(test_file_path)
print(coordinates)

