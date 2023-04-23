class Person:
    Country = 'china' # class var
    
    def __init__(self, name):
        self.name = name
 
    def print_name(self):
        print(self.name)

    @classmethod
    def print_country(cls):
        print(cls.Country)

    @staticmethod
    def join_name(first_name, last_name):
        return last_name + first_name

def test():
    laowang = Person('laowang')
    laoli = Person('laoli')
    laowang.print_name()
    laoli.print_name()
    print(laowang.Country)
    print(laoli.Country)

test()
