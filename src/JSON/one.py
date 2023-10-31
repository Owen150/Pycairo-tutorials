import json


def read_first_json_line_with_extend(filename):
    try:
        with open(filename, 'r') as json_file:
            # Initialize an empty list to extend the JSON content
            json_content = []

            # Read and extend the first line from the JSON file
            json_content.extend(json_file.readline().strip())

            # Parse the extended list as JSON to create a dictionary
            first_json_dict = json.loads(''.join(json_content))

            return first_json_dict
    except Exception as e:
        print("An error occurred:", str(e))
        return None


# Example usage
file_path = "test.json"  # Replace with the path to your JSON file
json_dict = read_first_json_line_with_extend(file_path)
print(json_dict)
