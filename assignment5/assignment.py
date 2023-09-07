
# - ListV2
#  - __init__
#     - self.values
#  - __add__
#  - __sub__
#  - __mul__
#  - __truediv__
#  - append
#  - mean
#  - __iter__
#  - __next__
#  - __repr___
 
# - DataFrame
#  - __init__
#      - self.index - a dictionary to map text to row index
#      - self.data (dict of ListV2 where each column is a key)
#      - self.columns a simple list
#  - set_index
#  - __setitem__
#  - __getitem__
#  - loc
#  - iteritems
#  - iterrows
#  - as_type
#  - drop
#  - mean
#  - __repr__

class ListV2:
    def __init__(self, values):
        self.values = list(values)
        
    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Lists must have same length")
        return ListV2([self.values[i] + other.values[i] for i in range(len(self.values))])
    
    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Lists must have same length")
        return ListV2([self.values[i] - other.values[i] for i in range(len(self.values))])
    
    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Lists must have same length")
        return ListV2([self.values[i] * other.values[i] for i in range(len(self.values))])
    
    def __truediv__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Lists must have same length")
        return ListV2([self.values[i] / other.values[i] for i in range(len(self.values))])
    
    def append(self, value):
        self.values.append(value)
    
    def mean(self):
        print("sum", sum(self.values), len(self.values))
        return sum(self.values) / len(self.values)
    
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):
        if self.current_index >= len(self.values):
            raise StopIteration
        value = self.values[self.current_index]
        self.current_index += 1
        return value
    
    def __repr__(self):
        return f"ListV2({self.values})"
    
    
class DataFrame:
    def __init__(self, data, columns):
        self.index = {}
        self.data = {}
        self.columns = list(columns)
        for i, col in enumerate(columns):
            self.data[col] = ListV2([ele[i] for ele in data])
        
        for i, row in enumerate(data):
            self.index[i] = row[0]
        print(self.index)
    
    def set_index(self, cols):
        index = {}
        for i, ele in enumerate(self.data['StudentName']):
            index[ele] = cols[i]
        self.index = index
        print(self.index)
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        elif isinstance(key, slice):
            start = key.start
            stop = key.stop
            step = key.step
            if start is None:
                start = 0
            if stop is None:
                stop = len(self.data[self.columns[0]])
            if step is None:
                step = 1
            new_data = []
            for i in range(start, stop, step):
                new_data.append(self.get_row(i))
            return DataFrame(new_data, self.columns)
        elif isinstance(key, tuple):
            rows, cols = key
            start_row = rows.start or 0
            end_row = rows.stop or len(self.index)
            start_col = cols.start or 0
            end_col = cols.stop or len(self.columns)
            rows = range(start_row, end_row)
            cols = range(start_col, end_col)
            new_data = []
            for i in rows:
                new_data.append(self.get_row(i)[start_col:end_col])
            return DataFrame(new_data, self.columns[start_col:end_col])
        else:
            col_data = []
            for k in key:
                col_data.append(self.data[k])
            new_data = []
            for data in col_data:
                new_data.append(data.values)
            data = []
            for _, ele in enumerate(zip(*new_data)):
                data.append([e for e in list(ele)])
            return DataFrame(data, key)
    
    def loc(self, label):
        if isinstance(label, tuple):
            row_name, col_name = label
            self.columns = col_name
            index = {}
            id = []
            for i, k in enumerate(self.index):
                if k in row_name:
                    id.append(i)
            for k in row_name:
                index[k] = self.index[k]
            self.index = index
            for k in col_name:
                data_col = []
                print(self.data[k].values)
                for i in id:
                    data_col.append(self.data[k].values[i])
                self.data[k] = ListV2(data_col)
            for i, k in enumerate(self.index):
                self.index[k] = i
            return self
        else:   
            return self.get_row(label)
    
    def iteritems(self):
        data = {}
        for col in self.columns:
            data[col] = self.data[col].values
        return data
    
    def iterrows(self):
        row_data = []
        for i, key in enumerate(self.index.keys()):
            row_d = self.get_row(i)
            row_data.append((key, tuple(row_d)))
        return row_data
    
    def as_type(self, col, dtype):
        self.data[col] = ListV2([dtype(ele) for ele in self.data[col].values])
    
    def drop(self, labels):
        if isinstance(labels, str):
            labels = [labels]
        for label in labels:
            del self.data[label]
            self.columns.remove(label)
    
    def mean(self):
        return {col: sum(self.data[col].values) / len(self.data[col].values) for col in self.columns}
    
    def __repr__(self):
        print(self.index)
        header = [""] + self.columns
        row_strings = ','.join(header) + "\n"
        for i, key in enumerate(self.index.keys()):
            row_strings += str(key) + ',' + ','.join(str(ele) for ele in self.get_row(i)) + "\n"
        print(row_strings)
        return row_strings[:-1]
    
    def get_row(self, index):
        return [self.data[col].values[index] for col in self.columns]
    

if __name__ == "__main__":
    columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
    df = DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
    df[1:4, :3].__repr__()


        

      