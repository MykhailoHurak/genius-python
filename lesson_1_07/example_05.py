class Counter:
    """Count of something"""

    def __init__(self, count_obj, type_obj, max_elements) -> None:
        self.count_obj = count_obj
        self.type_obj = type_obj
        self.max_elements = max_elements
    
    def counter(self):
        print(f"Type of object: {self.type_obj}")
        if isinstance(self.count_obj, (list, dict, str, tuple)):
            count = len(self.count_obj)
            if count > self.max_elements:
                print("Count elements of your object is more than need")
                print(f"More on {count - self.max_elements}")
            else:
                print(f"Count of elements: {count}")
        else:
            print("Your object must be iterable")
    
    def get_attrs(self):
        print(self.__dict__)

    def set_attr(self, attr, value):
        print(attr, value)
        if hasattr(self, attr):
            setattr(self, attr, value)
        else:
            print("Check your attrs")

class ListElements(Counter):
    """Class for list elements"""

    def __init__(self, count_obj, type_obj, max_elements) -> None:
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()
        print("Operation was ended")

    def get_attrs(self):
        super().get_attrs()
        print("Operation was ended")

# -----------------------------------

list_01 = ListElements([1, 2, 3, 4, 5], list, 12)

list_01.counter()
list_01.get_attrs()

list_01.set_attr("count_obj", [1, 2, 3, 4, 5, 6])
list_01.set_attr("max_elements", 10)
list_01.get_attrs()