import pytest
from dict_mixin import DictConverterMixin

class ClassContainingDict:
    def __init__(self) -> None:
        self.leg_numbers = {
            "cat": 4,
            "dog": 4,
            "human": 2,
            "whale": 0,
            "starfish": 5
        }

class ClassContainingList:
    def __init__(self) -> None:
        self.my_list = ["dog", "cat", "hen"]

class ClassContainingBuiltinTypes:
    def __init__(self) -> None:
        self.int_example = 4
        self.str_example = "hello"
        self.float_example = 3.0

class ClassContainingHiddenField:
    def __init__(self) -> None:
        self.__hidden =  {"something": "else"}

class ClassContainingObjContainingDict(DictConverterMixin):
    def __init__(self) -> None:
        self.my_obj = ClassContainingDict()

class ClassContainingObjContainingList(DictConverterMixin):
    def __init__(self) -> None:
        self.my_obj = ClassContainingList()

class ClassContainingObjContainingBuiltinTypes(DictConverterMixin):
    def __init__(self) -> None:
        self.my_obj = ClassContainingBuiltinTypes()

class ClassContainingObjContainingHiddenField(DictConverterMixin):
    def __init__(self) -> None:
        self.my_obj = ClassContainingHiddenField()

class ClassContainingObjWithDictConverterMixin(DictConverterMixin):
    def __init__(self) -> None:
        self.dict_convertable_mixin = ClassContainingObjContainingDict()

@pytest.mark.parametrize(
      "obj_to_convert,expected_dict",
      [
          (ClassContainingObjContainingDict(), {
                "my_obj": {
                    "leg_numbers": {
                        "cat": 4,
                        "dog": 4,
                        "human": 2,
                        "whale": 0,
                        "starfish": 5
                    }
                }
          }),
          (ClassContainingObjContainingList(), {
              "my_obj": {
                  "my_list": ["dog", "cat", "hen"]
              }
          }),
          (ClassContainingObjContainingBuiltinTypes(), {
                "my_obj": {
                    "int_example":  4,
                    "str_example": "hello",
                    "float_example": 3.0
                }
          }),
          (ClassContainingObjContainingHiddenField(), {
              "my_obj": {
                  "hidden":  {"something": "else"}
              }
          }),
          (ClassContainingObjWithDictConverterMixin(), {
                "dict_convertable_mixin": {
                    "my_obj": {
                        "leg_numbers": {
                            "cat": 4,
                            "dog": 4,
                            "human": 2,
                            "whale": 0,
                            "starfish": 5
                        }
                    }
                }
          })
      ]
)
def test_dict_mixin_correctly_converts_class(obj_to_convert, expected_dict):
    result = obj_to_convert.to_dict()
    assert result == expected_dict
