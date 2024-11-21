class A:
    """Class A"""
    name_a = "class A is a Parent"
    is_main_class = True

    def print_hello(self):
        print("Hello!!!!!!!!!!!!!!!!!!!!")

class B(A):
    """Class B"""
    name_b = "class B is a Child"
    is_main_class = False

    def print_hello(self):
        print("Hello!!!!!!!!!!!!!!!!!!!!")

class C(B):
    """Class C"""
    pass

example = C()

example.print_hello()