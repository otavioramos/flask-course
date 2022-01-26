from msilib.schema import Class


class ClassTest:
    def instance_method(self):
        print(f'Called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called instance_method of {cls.__name__}')

    @staticmethod
    def static_method():
        print('Called static_method')


test = ClassTest()
test.instance_method()

ClassTest.class_method()
ClassTest.static_method()