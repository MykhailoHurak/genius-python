class BaseInterface:
    """Base class"""

    def __init__(self) -> None:
        pass

    def get_attrs(self) -> None:
        pass

    def print_model(self) -> None:
        pass

    def count_of_price(self) -> None:
        pass

    def call_to_support(self) -> None:
        pass

class SiteInterface(BaseInterface):
    """Interface of our site"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self) -> None:
        print(f"Model of site: {self.model}")

    def count_of_price(self) -> None:
        print(f"Count of site price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support: {self.number}")
        print("You can call from 8 am to 7 pm")

class AppInterface(BaseInterface):
    """Interface of our application"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self) -> None:
        print(f"Model of application: {self.model}")

    def count_of_price(self) -> None:
        print(f"Count of application price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support: {self.number}")
        print("You can call from 8 am to 7 pm")

# --------------------------------

site_user = SiteInterface(6459694, "shop", 1000)
app_user = AppInterface(395495, "android", 3000)

site_user.print_model()
site_user.count_of_price()
site_user.call_to_support()

print("-------")

app_user.print_model()
app_user.count_of_price()
app_user.call_to_support()