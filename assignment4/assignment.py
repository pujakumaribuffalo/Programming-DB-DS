class IteratorClass:
    # Complete this class! It takes in three inputs when initializing.
    # input#1 x -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#2 y -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#3 operator -- is a string that can either be 'add', 'sub', 'mul', 'div' -- If the specified operator
    # is not one of these, raise a ValueError.

    # Complete the class by writing functions that will turn it into an iterator class.
    # https://www.programiz.com/python-programming/methods/built-in/iter
    # The purpose of the class is to take two lists(x and y), apply the specified operator and return the output
    # as an iterator, meaning you can do "for ele in IteratorClass(x,y,'add')"
    # NOTE: For the / operator, round to two decimal places
    # Raise ValueError when the length is not the same for both inputs
    # Raise ValueError when the operator is not add, sub, mul, or div.

    # BEGIN SOLUTION
    def __init__(self, x, y, operator):
        if not isinstance(x, (list, tuple)):
            raise ValueError("x must be a list or tuple")
        if not isinstance(y, (list, tuple)):
            raise ValueError("y must be a list or tuple")
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")
        if operator not in ["add", "sub", "mul", "div"]:
            raise ValueError("Input operator must be 'add', 'sub', 'mul', or 'div'")

        self.x = x
        self.y = y
        self.operator = operator
        self.index = 0

        self.operators = {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "mul": lambda x, y: x * y,
            "div": lambda x, y: round(x / y, 2)
        }

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.x):
            raise StopIteration
        
        result = self.operators[self.operator](self.x[self.index], self.y[self.index])

        self.index += 1
        return result

    # END SOLUTION


class ListV2:
    # Complete this class to fulfill the following requirement
    # 1) The class only takes one input argument which is a list or a tuple;
    #    Raise ValueError if the input is not a list or tuple
    # 2) The class overload loads +,-,*,/ and returns a ListV2 object as the result
    # 3) The class can handle +,-,*,/ for both list and int/float, meaning the thing to the right of the operator
    #    can be a sequence or a number;
    # 4) The class is an iterator
    # HINT: Study the assert statements in the test file to understand how this class is being used and reverse engineer it!
    # NOTE: For the / operator, round to two decimal places

    # BEGIN SOLUTION

    def __init__(self, lst):
        if not isinstance(lst, (list, tuple)):
            raise ValueError("Input must be a list or a tuple.")
        self.lst = lst
    
    
    def __add__(self, other):
        if isinstance(other, ListV2):
            if len(self.lst) != len(other.lst):
                raise ValueError("Lists must be of the same length.")
            return ListV2([self.lst[i] + other.lst[i] for i in range(len(self.lst))])
        elif isinstance(other, (int, float, list, tuple)):
            if isinstance(other, (list, tuple)):
                if len(self.lst) != len(other):
                    raise ValueError("Lists must be of the same length.")
                return ListV2([self.lst[i] + other[i] for i in range(len(self.lst))])
            return ListV2([ele + other for ele in self.lst])
        else:
            raise ValueError("Addition Operand must be a ListV2 object or a number.")
    
    def __sub__(self, other):
        if isinstance(other, ListV2):
            if len(self.lst) != len(other.lst):
                raise ValueError("Lists must be of the same length.")
            return ListV2([self.lst[i] - other.lst[i] for i in range(len(self.lst))])
        elif isinstance(other, (int, float, list, tuple)):
            if isinstance(other, (list, tuple)):
                if len(self.lst) != len(other):
                    raise ValueError("Lists must be of the same length.")
                return ListV2([self.lst[i] - other[i] for i in range(len(self.lst))])
            return ListV2([ele - other for ele in self.lst])
        else:
            raise ValueError(" subtraction Operand must be a ListV2 object or a number.")

    def __mul__(self, other):
        if isinstance(other, ListV2):
            if len(self.lst) != len(other.lst):
                raise ValueError("Lists must be of the same length.")
            return ListV2([self.lst[i] * other.lst[i] for i in range(len(self.lst))])
        elif isinstance(other, (int, float, list, tuple)):
            if isinstance(other, (int, float)):
               return ListV2([ele * other for ele in self.lst])
            elif isinstance(other, tuple):
                if len(self.lst) != len(list(other)):
                  raise ValueError("Lists must be of the same length.")
            return ListV2([self.lst[i] * list(other)[i] for i in range(len(self.lst))])
        else:
            raise ValueError("Multiplication Operand must be a ListV2 object or a number.")
    
    def __truediv__(self, other):
        if isinstance(other, ListV2): 
            if len(self.lst) != len(other.lst):
                raise ValueError("Lists must be of the same length.")
            return ListV2([round(self.lst[i] / other.lst[i], 2) for i in range(len(self.lst))])
        elif isinstance(other, (int, float, list, tuple)):
            if isinstance(other, (int, float)):
                if other == 0:
                    raise ValueError("Division by zero not allowed.")
                return ListV2([round(x / other, 2) for x in self.lst])
            elif isinstance(other, (list, tuple)):
                if len(self.lst) != len(list(other)):
                    raise ValueError("Lists must be of the same length.")
                if 0 in other:
                    raise ValueError("Division by zero not allowed.")
                return ListV2([round(x / other[i], 2) for i, x in enumerate(self.lst)])
        else:
            raise ValueError("Division Operand must be a ListV2 object or a number.")


    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        result = self.lst[self.index]
        self.index += 1
        return result
    
    def __repr__(self):
        return f"{self.lst}"


    # END SOLUTION


class Pound:
    """
    - class represents weight in lb and oz
    - 1 lb has 16 oz
    - add addition functionality
    - add subtraction functionality. Make sure to raise an error if the resulting value is negative. Infer the error type and message form the test.
    - add a human readable representation that looks like --> 17 lb 4 oz
    - add an unambiguous representation that looks like --> Pound(17, 4)
    
    """
    # BEGIN SOLUTION
    def __init__(self, lb=0, oz=0):
        if oz >= 16:
            lb += oz // 16
            oz = oz % 16
        self.lb = lb
        self.oz = oz

    def __add__(self, other):
        totalOz = self.lb * 16 + self.oz + other.lb * 16 + other.oz
        return Pound(totalOz // 16, totalOz % 16)

    def __sub__(self, other):
        totalOz = self.lb * 16 + self.oz - other.lb * 16 - other.oz
        if totalOz < 0:
            raise ValueError("Resulting weight is negative")
        return Pound(totalOz // 16, totalOz % 16)

    def __repr__(self):
        return f"Pound({self.lb}, {self.oz})"

    def __str__(self):
        return f"{self.lb} lb {self.oz} oz"

    # END SOLUTION