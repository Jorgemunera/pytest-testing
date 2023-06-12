from src.main import suma, is_greater_than, login
import pytest

class TestSuma:
    def test_suma(self):
        assert suma(2, 3) == 5

    def test_suma_non_number(self):
        with pytest.raises(TypeError):
            suma("string", 2)
        with pytest.raises(TypeError):
            suma(2, "string")
        with pytest.raises(TypeError):
            suma("string", "string")

    @pytest.mark.parametrize(
            "input1, input2, expected",
            [
                (5, 1 ,6),
                (6, suma(2, 2) , 10),
                (suma(19, 1), 15 , 35),
                (-7, suma(1,2) , -4),
            ]
    )
    def test_suma_params(self, input1, input2, expected):
        assert suma(input1, input2) == expected


class TestIsGreaterThan:
    def test_when_not_numbers_should_fail(self):
        with pytest.raises(TypeError):
            is_greater_than("string", 2)
        with pytest.raises(TypeError):
            is_greater_than(2, "string")
        with pytest.raises(TypeError):
            is_greater_than("string", "string")

    def test_is_greater_than(self):
        assert is_greater_than(2,3) == False
        assert is_greater_than(-2,-3) == True
    

class TestLogin:
    def test_login(self):
        login_passes = login("jorge", "jorge123")
        assert login_passes == True
    
    def test_login_failed(self):
        login_passes = login("s", "a")
        assert not login_passes