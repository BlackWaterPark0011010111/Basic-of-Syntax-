import json
import logging
import argparse
from typing import Any, Dict, List
import asyncio
import aiofiles
from contextlib import AsyncExitStack

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def read_json(file_path: str) -> List[Dict[str, Any]]:
    """Async reading of data from a JSON"""
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            data = await file.read()
            return json.loads(data)
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON from {file_path}: {e}")
        return []

async def write_json(file_path: str, data: List[Dict[str, Any]]) -> None:
    """Async writing of data to a JSON file"""
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            await file.write(json.dumps(data, ensure_ascii=False, indent=4))
        logging.info(f"Filtered data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")

def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter data by a specific key-value pair"""
    return [item for item in data if item.get(key) == value]

async def main(input_file: str, output_file: str, key: str, value: Any) -> None:
    """Main async function to filter data in JSON format"""
    logging.info("Starting to filter data...")
    async with AsyncExitStack() as stack:
        data = await read_json(input_file)
        if data:
            filtered_data = filter_data(data, key, value)
            await write_json(output_file, filtered_data)
            logging.info("Data filtering complete.")
        else:
            logging.warning("No data found for filtering.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter data in a JSON file by a specified key-value pair.")
    parser.add_argument("input_file", type=str, help="Path to the input JSON file")
    parser.add_argument("output_file", type=str, help="Path to save the filtered JSON data")
    parser.add_argument("key", type=str, help="Key to filter by")
    parser.add_argument("value", type=str, help="Value to filter by")
    args = parser.parse_args()

    try:
        asyncio.run(main(args.input_file, args.output_file, args.key, args.value))
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
