class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class User(metaclass=SingletonMeta):
    def __init__(self):
        self.__user_name = "name"
        self.__user_age = 18
    def get_user_data(self):
        print(f"user name: {self.__user_name}\nuser age: {self.__user_age}")

    def set_user_data(self, name, age):
        print(f"[Old data]\nuser name: {self.__user_name}\nuser age: {self.__user_age}")
        self.__user_name= name
        self.__user_age= age
        print(f"[New data]\nuser name: {self.__user_name}\nuser age: {self.__user_age}")


if __name__ == "__main__":
    # The client code.

    s1 = User()
    s2 = User()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        s1.get_user_data()
        s2.set_user_data("QA", "22")
        s1.get_user_data()
    else:
        print("Singleton failed, variables contain different instances.")