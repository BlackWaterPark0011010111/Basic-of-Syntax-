# JSON Data Filter

**JSON Data Filter** — is an asynchronous Python script designed to filter data in a JSON file based on a specified key-value pair and save the filtered data to a new JSON file.

This tool is useful for extracting specific records from large JSON datasets.

## Features

- **Asynchronous Operation: Processes large JSON files without blocking execution.
- **Flexible Filtering**: Filters data by any key and value specified in the JSON objects.
- **Logging**: Detailed logging of operations, including errors and warnings.

## Requirements

- **Library `aiofiles`**

  You can install the required libraries using pip:

  ```
  pip install aiofiles

- **Usage:**

To use the script, you need to provide four arguments:

input_file — The path to the input JSON file.
output_file — The path where the filtered data will be saved.
key — The key in the JSON objects that will be used for filtering.
value — The value that will be used for filtering.

- **Example**
You have a JSON file input.json with the following content:

```

    [
        {
            "name": "Harry Potter",
            "age": 17,
            "city": "Hogwarts"
        },

        {
            "name": "Jay Gatsby",
            "age": 32,
            "city": "West Egg"
        },
        {
            "name": "Winnie-the-Pooh",
            "age": 5,
            "city": "Hundred Acre Wood"
        },
    ]
```

If you want to filter data where "name" equals "Harry Potter" and save the result to output.json, you need to run:



![scnd](https://github.com/BlackWaterPark0011010111/Asinc/blob/main/assets/sort.png)




***`(first, enter the filename of the processing script) python filter_json.py (then specify the file from which the key/value is taken) input.json (specify the file where the result should be saved) output.json (and the filter itself) name "Harry Potter"`***




![first](https://github.com/BlackWaterPark0011010111/Asinc/blob/main/assets/results.png)


- **Logging**
The script logs its execution process and any issues encountered to the console:

- Info Logs: General description of the execution process.
- Warning Logs: Indicate potential issues, such as no data remaining after filtering.
- Errors: Indicate critical problems, such as a missing file or JSON parsing errors.
- Running the Script
- You run the script from the command line:

The script command looks like this:
```
python filter_json.py `input> output> key> value>`
