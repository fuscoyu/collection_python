# coding=utf-8

# 工厂模式
class DogToy:
    def speak(self):
        print("wang wang")

class CatToy:
    def speak(self):
        print("miao miao")


def toy_factory(toy_type):
    if toy_type == 'dog':
        return DogToy()
    elif toy_type == 'cat':
        return CatToy()


# 构造模式

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None
    
    def __str__(self):
        msg = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(msg)

class ComputeBuilder:
    def __init__(self):
        self.computer = Computer('fx-plus 4200')
    
    def configrue_memory(self, amount):
        self.computer.memory = amount

    def configrue_hdd(self, amount):
        self.computer.hdd = amount

    def configrue_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory), self.builder.configure_hdd(hdd), self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer





# 原型模式

# 单例模式
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance


class MyClass(Singleton):
    pass

c1 = MyClass()
c2 = MyClass()







































 

      
