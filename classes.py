from typing import List, Any

class Database:
    def __init__(self, name: str):
        assert isinstance(name, str), "name must be a string"
        self.name = name
        self.tables: List["Table"] = []

class DataColumn:
    def __init__(self, name: str):
        assert isinstance(name, str), "name must be a string"
        self.name = name
        self.data_type = None

    def validate(self, value):
        pass

class Table:
    def __init__(self, name: str):
        assert isinstance(name, str), "name must be a string"
        self.name = name
        self.columns: List["DataColumn"] = []
        self.rows: List["Row"] = []

    def search(self, filter_list: List[Any]):
        assert len(filter_list) == len(self.columns), "filter_list must have the same length as columns"
        filtered_rows = [row for row in self.rows if all(
            filter_val is None or str(row_val) == str(filter_val) for row_val, filter_val in zip(row.values, filter_list))]

        return filtered_rows

    def add_column(self, column: DataColumn):
        if not isinstance(column, DataColumn):
            raise TypeError("column must be an instance of DataColumn")

        for existing_column in self.columns:
            if existing_column.name == column.name:
                raise ValueError("column with this name already exists")

        self.columns.append(column)

class Row:
    def __init__(self, table: "Table", values: List[Any]):
        self.table = table
        self.values = values

    def __getitem__(self, item):
        return self.values[item]

class IntegerDataColumn(DataColumn):
    def __init__(self, name):
        super().__init__(name)
        self.data_type = int

    def validate(self, value):
        return isinstance(value, int)

class RealDataColumn(DataColumn):
    def __init__(self, name):
        super().__init__(name)
        self.data_type = float

    def validate(self, value):
        return isinstance(value, float)

class TextDataColumn(DataColumn):
    def __init__(self, name):
        super().__init__(name)
        self.data_type = str

    def validate(self, value):
        return isinstance(value, str)

class CharDataColumn(DataColumn):
    def __init__(self, name):
        super().__init__(name)
        self.data_type = str

    def validate(self, value):
        return isinstance(value, str) and len(value) == 1
