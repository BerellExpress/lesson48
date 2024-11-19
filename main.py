from pprint import pprint


def introspection_info(obj):
    result = {}

    # Определение типа объекта
    result["type"] = type(obj).__name__

    # Получение всех атрибутов объекта
    attributes = dir(obj)
    result["attributes"] = attributes

    # Фильтрация методов объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    result["methods"] = methods

    # Определение модуля, к которому относится объект
    try:
        module = obj.__class__.__module__
        result["module"] = module
    except AttributeError:
        result["module"] = "__main__"

    return result

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return f"My method with value: {self.value}"


my_object = MyClass(42)
info = introspection_info(my_object)
pprint(info)