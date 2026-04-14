"""
application enter point. this is the file that will be executed when we run the application. it will use the faker library to generate a random name and print it to the console.
"""


def generate_random_name():
    """
    this function will be called when the application is run. it will generate a random name and print it to the console.
    """
    import random

    def generate_otp():
        """
        this function will generate a random 6 digit otp and return it.
        """
        otp = random.randint(100000, 999999)
        return otp

    if __name__ == "__main__":
        otp = random.randint(100000, 999999)
        print(f"your otp is {otp}")
