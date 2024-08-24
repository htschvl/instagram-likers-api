import os
import json
from typing import Any, Dict

def save_json(data: Dict[str, Any], filename: str) -> None:
    try:
        output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../output')
        os.makedirs(output_directory, exist_ok=True)

        base_name, extension = os.path.splitext(filename)
        file_path = os.path.join(output_directory, filename)

        file_counter = 1
        while os.path.exists(file_path):
            new_filename = f"{base_name} {file_counter}{extension}"
            file_path = os.path.join(output_directory, new_filename)
            file_counter += 1

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)  

        print(f"File saved at: {file_path}")
    except Exception as save_error:
        print(f"Error saving JSON file: {save_error}")
        raise

def load_json(filename: str) -> Dict[str, Any]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON file {filename}.")
        raise
    except Exception as load_error:
        print(f"Unknown error loading JSON file: {load_error}")
        raise

def test_json_handling() -> None:
    try:
        test_data = {"example": "data", "special_char": "rebeca \u30c4"}
        save_json(test_data, "example.json")
        loaded_data = load_json("example.json")
        print(f"Loaded data: {loaded_data}")
    except Exception as execution_error:
        print(f"Execution failed: {execution_error}")

if __name__ == "__main__":
    test_json_handling()
