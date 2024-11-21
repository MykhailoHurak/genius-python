class A:
    """Class A"""
    name_a = "class A is a Parent"
    is_main_class = True

class B(A):
    """Class B"""
    name_b = "class B is a Child"
    is_main_class = False

class C(B):
    """Class C"""
    pass

example = C()
print(example.name_a)
print(example.name_b)
print(example.is_main_class)