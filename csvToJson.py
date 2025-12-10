import csv
import json
import os

def csvToJson(filename:str,destination:str= None,columnNames:list[str] = None):
    """
    Converts a CSV file to JSON.

    Args:
        filename (str): **RAW STRING** Path to the source .csv file.
        destination (str, optional): **RAW STRING** Path to the destination .json file.
            - If None: Creates the file in the same folder as the .csv, with the same name.
            - If a folder: Creates the file inside that folder, keeping the original name.
        columnNames (list[str] | str, optional): Defines the column names.
            - If a string: Uses the first line of the .csv file as the header.
            - If a list: Uses the provided list as column names (and validates/ignores the first line of the file).
            - If None: Uses numerical indices (1, 2, 3...) as keys, assuming there is no header.
    """
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")
    
    if not filename.lower().endswith('.csv'):
        raise ValueError(f"Error: The file '{filename}' does not have the .csv extension.")

    d={}
    with open(filename, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))

        if not rows:
            raise ValueError(f"Error: The file '{filename}' is empty.")

        cont = iter(rows)

        if isinstance(columnNames,str):
            columnNames = next(cont)
        elif columnNames!=None:
            fields = next(cont)
            
            if len(columnNames) != len(fields):
                raise ValueError(f"Format Error: Provided {len(columnNames)} column names, but the file has {len(fields)} columns.")

            for i in range(len(fields)):
                if fields[i] != columnNames[i]:
                    print(f"Header Conflict: At position {i}, user provided '{columnNames[i]}', but file contains '{fields[i]}'.")
                    print('Using the provided names')
        else:
            if rows:
                columnNames = list(range(len(rows[0])+1))
            else:
                columnNames = []
        
        atual = 0
        for row in cont:
            for i,col in enumerate(row):
                if i == 0:
                    atual = str(col)
                    d[atual]={}
                else:
                    d[atual][columnNames[i]]=col
    
    if not destination:
        destination = os.path.splitext(filename)[0] + '.json'
    else:
        base_name = os.path.basename(filename)
        new_filename = os.path.splitext(base_name)[0] + '.json'
        destination = os.path.join(destination, new_filename)
    
    with open(destination,'w') as js:
        json.dump(d,js)