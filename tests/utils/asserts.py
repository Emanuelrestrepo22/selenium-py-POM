import pytest
import test
from tests.utils.locators import Locators
from time import sleep as wait
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
from tests.utils.locators import Locators
from typing import Tuple
dataType = Union[str, int, float, bool, list, tuple, set, dict]
Test = Tuple[WebDriver, Locators] 

class Expect:
    # * Definición de funciones para realizar Asserciones con valores dados
    def __init__(self, actualValue: dataType):
        if not isinstance(actualValue, (str, int, float, bool, list, Tuple, set, dict)):
            raise ValueError(f'DataType not supported. try: {dataType}')
        self.value = actualValue

    def toBeEqual(self, expectedValue: dataType):
        if not isinstance(expectedValue, (str, int, float, bool, list, tuple, set, dict)):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value == expectedValue
        wait(1)

    def toNotBeEqual(self, expectedValue: dataType):
        if not isinstance(expectedValue, (str, int, float, bool, list, tuple, set, dict)):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value != expectedValue
        wait(1)

    def toContain(self, innerValue: str):
        if not isinstance(self.value, str):
            raise ValueError(f'Value type not supported. Use String type')
        assert innerValue in self.value
        wait(1)

    def isTrue(self):
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value is True
        wait(1)

    def isFalse(self):
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value is False
        wait(1)
