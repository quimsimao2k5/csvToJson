import csv
import json
import os

def rct(n):
    'If n is int return n, else returns str(n)'
    try:
        return int(n)
    except Exception:
        return n

def csvToJson(filename:str,destination:str= None,destinationName:str=None,columnNames:list[str] = None, ids = True, delimiter=None):
    """
    Converts a CSV file to JSON.

    Args:
        filename (str): **RAW STRING** Path to the source .csv file.
        destination (str, optional): **RAW STRING** Path to the destination .json file.
            - If None: Creates the file in the same folder as the .csv.
            - If a folder: Creates the file inside that folder.
        destinationName (str, optional): Name of the destination .json file.
            - If None: The result file will have the same name as the .csv file.
            - If a string: The result file takes the given name.
        columnNames (list[str] | str, optional): Defines the column names.
            - If a string: Uses the first line of the .csv file as the header.
            - If a list: Uses the provided list as column names (and validates/ignores the first line of the file).
            - If None: Uses numerical indices (1, 2, 3...) as keys, assuming there is no header.
        ids (bool, optional): Should be true if the first column is made up of identifiers.
            - If True: The attribute names for each row are derived from the value of the first element in that row.
            - If False: The attribute names for each row take on a numeric value.
        delimiter (str, optional): The delimiter used in the CSV file. If None, attempts to sniff it.
    """
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")
    
    if not filename.lower().endswith('.csv'):
        raise ValueError(f"Error: The file '{filename}' does not have the .csv extension.")

    d={}
    with open(filename, 'r', encoding='utf-8-sig') as f:
        if delimiter is None:
            try:
                sample = f.read(1024)
                f.seek(0)
                dialect = csv.Sniffer().sniff(sample)
                delimiter = dialect.delimiter
            except Exception:
                delimiter = ';' # Default fallback
                f.seek(0)
        
        rows = list(csv.reader(f, delimiter=delimiter))
        n = len(rows)
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
        
        if ids:
            atual = 0
            for row in cont:
                if len(row) > len(columnNames):
                    raise ValueError(f"Error: Row starting with '{row[0]}' has {len(row)} columns, but header has {len(columnNames)}.")
                for i,col in enumerate(row):
                    if i == 0:
                        atual = str(col)
                        d[atual]={}
                    else:
                        d[atual][columnNames[i]]=rct(col)
        else:
            for i,row in zip(range(n),cont):
                if len(row) > len(columnNames):
                    raise ValueError(f"Error: Row {i} has {len(row)} columns, but header has {len(columnNames)}.")
                d[i]={}
                for j,col in enumerate(row):
                    d[i][columnNames[j]]=rct(col)

    if destinationName:
        try:
            base_name = destinationName + '.json'
        except Exception as e:
            print("Destination name should be a string. Error: ",e)
            return
    else:
        base_name = os.path.splitext(os.path.basename(filename))[0] + '.json'
    
    if not destination:
        destination = os.path.join(os.path.dirname(filename), base_name)
    else:
        destination = os.path.join(destination, base_name)
    
    
    try:
        with open(destination,'w',encoding="utf-8") as js:
            try:
                json.dump(d,js,ensure_ascii=False, indent=4)
            except Exception as e:
                print("Problem with JSON writing")
                return
    except Exception as e:
        print("Destination provided is invalid: ",e)
