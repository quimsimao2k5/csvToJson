# CSV to JSON Converter

A simple and robust Python utility to convert CSV files into JSON format.

## Index

- [Features](#features)
- [Usage](#usage)
- [Outputs](#outputs)
- [Requirements](#requirements)

## Features

- **Automatic JSON creation**: Converts `.csv` files to `.json` seamlessly.
- **Flexible Destination**: Save the result in the same directory or specify a custom folder, with or without a custom name.
- **Column Management**:
  - Use the CSV header automatically.
  - Provide your own custom column names.
  - Handle files without headers (generates numerical keys).
- **Row Management**
  - Use the first column of each row to identify the content of each row.
  - Use numerical values ​​to identify the content of each row.
- **Validation**: Checks for file existence, correct extension, and empty files.
- **UTF-8 Support**: Handles special characters correctly.

## Usage

Import the function into your Python script:

```python
from csvToJson import csvToJson
```

### 1. Basic Conversion

Converts `data.csv` to `data.json` in the same folder.

```python
csvToJson('data.csv')
```

### 2. Custom Destination or Destination Name

Saves the file to a specific folder (e.g., `backups/data.json`).
When using '\' in the filename or destination folder, you need to use a raw string. Instead of using 'C:\Folder\' use r'C:\Folder\'
You don't have to name both simultaneously; you can name the file without specifying the destination folder, or vice versa.

```python
csvToJson('data.csv', destination=r'C:\Backups\', destionationName = 'dataJSON')
csvToJson('data.csv', destination=r'C:\Backups\')
csvToJson('data.csv', destionationName = 'dataJSON')
```

### 3. Custom Column Names

Overrides the header found in the `csv` file.

```python
csvToJson('data.csv', columnNames=['ID', 'Name', 'Age'])
```

### 4. Automatic Column Names

If the `csv` dataset already has a header, and you want to use those names to name attributes, you can write **any string**.

```py
csvToJson('data.csv', columnNames='Auto')
```

### 5. No Header in CSV

If your `csv` doesn't have a header row, pass `None` to generate numerical keys.

```python
csvToJson('data_no_header.csv', columnNames=None)
```

### 6. Row Names

If the first column in your `csv` dataset contains unique identifiers (for example: unique names, unique numbers), you can set (in fact, it's already set by default) the `ids` parameter to `True`. Otherwise, you need to set it to `False`.

```py
#if the first column doesnt contain unique id's
csvToJson('data.csv', ids=False)
```

## Outputs

Using this file as an example:

```ini
name, age, gender, height
john, 21, male, 180
mary, 29, female, 167
albert, 90, nb, 191
jose, 55, male, 152
```

The resulting file looks like this: (using the automatic header option)

```js
{
  "john": {
    "age": 21,
    "gender": "male",
    "height": 180
  },
  "mary": {
    "age": 29,
    "gender": "female",
    "height": 167
  },
  "albert": {
    "age": 90,
    "gender": "nb",
    "height": 191
  },
  "jose": {
    "age": 55,
    "gender": "male",
    "height": 152
  }
}
```

## Requirements

- Python 3.x
- Standard libraries: `csv`, `json`, `os` (no external dependencies required).
