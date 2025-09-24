import streamlit as st
import json
import os
import sys

def save_to_json(key,value,file_name="data.json"):
    try:
        # Take key and value input
        key = key
        value = value
        # Validate inputs
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Both key and value must be strings.")

        # Load existing data if file exists
        data = {}
        if os.path.exists(file_name):
            try:
                if os.path.getsize(file_name) == 0:  # <-- Empty file check
                    print("Warning: JSON file is empty. Starting fresh.")
                else:
                    with open(file_name, "r") as f:
                        data = json.load(f)
            except json.JSONDecodeError:
                print("Warning: JSON file is corrupted. Starting fresh.")

        # Update dictionary
        data[key] = value

        # Save back to file
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

        print("Data saved successfully!")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: No permission to access the file.")
    except OSError as oe:
        print(f"OS Error: {oe}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_json(file_name="data.json"):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError("JSON file does not exist.")

        if os.path.getsize(file_name) == 0:
            raise ValueError("JSON file is empty.")

        with open(file_name, "r") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("JSON data is not in expected dict format.")

        return data

    except FileNotFoundError as fnf:
        print(f"FileNotFoundError: {fnf}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
    except PermissionError:
        print("Error: No permission to read the file.")
    except OSError as oe:
        print(f"OS Error: {oe}")
    except Exception as e:
        print(f"Unexpected error: {e}")

data = read_json()

st.write(data)

key = st.text_input(
    label="KEY"
)
val = st.text_input(
    label="Value"
)

flag = st.button(
    label="Save",
    on_click=save_to_json,
    args=(
        key,
        val,
    )
)


