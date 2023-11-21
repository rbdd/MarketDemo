from datetime import datetime
class User:
    None

    
class Category:
    None


class Product:
    def __init__(self, product_id: int, product_name: str):
        if type(product_id) is not int or product_id < 0:
            raise ValueError("Product ID should be a positive integer!")
        self.__product_id = product_id

        if type(product_name) is str and product_name.strip() != "":
            self.__product_name = product_name.strip()
        else:
            self.__product_name = None

        self.__price = None
        self.__listed_date = None
        self.__description = None
        self.__image_url = None
        self.__categories: list = []
        self.__reviews: list = []
        self.__quantity = None
        self.__seller: User = None

    @property
    def seller(self) -> User:
        return self.__seller

    @User.setter
    def seller(self, seller: User):
        if isinstance(seller, User):
            self.__seller = seller
        else:
            self.__seller = None

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, new_product_name):
        if type(new_product_name) is str and new_product_name.strip() != "":
            self.__product_name = new_product_name.strip()
        else:
            self.__product_name = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if isinstance(price, (int, float)) and price >= 0:
            self.__price = price
        else:
            raise ValueError("Price must be a positive number!")

    @property
    def listed_date(self):
        return self.__listed_date

    @listed_date.setter
    def listed_date(self, listed_date: str):
        if isinstance(listed_date, str):
            try:
                # Check if the listed_date string is in the correct date format (e.g., "Oct 21, 2008")
                datetime.strptime(listed_date, "%b %d, %Y")
                self.__listed_date = listed_date
            except ValueError:
                raise ValueError("listed date must be in 'Oct 21, 2008' format!")
        else:
            raise ValueError("listed date must be a string in 'Oct 21, 2008' format!")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if isinstance(description, str) and description.strip() != "":
            self.__description = description
        else:
            self.__description = None

    @property
    def image_url(self):
        return self.__image_url

    @image_url.setter
    def image_url(self, image_url: str):
        if isinstance(image_url, str) and image_url.strip() != "":
            self.__image_url = image_url
        else:
            self.__image_url = None

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def genres(self) -> list:
        return self.__categories

    def add_genre(self, category: Category):
        if not isinstance(category, category) or category in self.__categories:
            return
        self.__categories.append(category)

    def remove_genre(self, category: Category):
        if not isinstance(category, category):
            return
        try:
            self.__categories.remove(category)
        except ValueError:
            print(f"Could not find {category} in list of categories.")
            pass

    def __repr__(self):
        return f"<Product {self.__product_id}, {self.__product_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__product_id == other.__product_id

    def __hash__(self):
        return hash(self.__product_id)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__product_id < other.product_id



class Wishlist:
    None
