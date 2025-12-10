# CSV to JSON Converter

A simple and robust Python utility to convert CSV files into JSON format.

## Features

- **Automatic JSON creation**: Converts `.csv` files to `.json` seamlessly.
- **Flexible Destination**: Save the output in the same directory or specify a custom folder.
- **Column Management**:
  - Use the CSV header automatically.
  - Provide your own custom column names.
  - Handle files without headers (generates numerical keys).
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

### 2. Custom Destination

Saves the file to a specific folder (e.g., `backups/data.json`).

```python
csvToJson('data.csv', destination=r'C:\Backups\')
```

### 3. Custom Column Names

Overrides the header found in the CSV file.

```python
csvToJson('data.csv', columnNames=['ID', 'Name', 'Age'])
```

### 4. No Header in CSV

If your CSV doesn't have a header row, pass `None` to generate numerical keys.

```python
csvToJson('data_no_header.csv', columnNames=None)
```

## Requirements

- Python 3.x
- Standard libraries: `csv`, `json`, `os` (no external dependencies required).
