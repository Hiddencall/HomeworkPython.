import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_string, result", [
    ("кузнечик", "Кузнечик"),
    ("how do you do", "How do you do"),
    ("weetyuiopp", "Weetyuiopp")])
def test_capitalize_positive(input_string, result):
    assert string_utils.capitalize(input_string) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_string, result", [
    ("", ""), ("  ", "  "), ("2025", "2025")])
def test_capitalize_negative(input_string, result):
    assert string_utils.capitalize(input_string) == result


@pytest.mark.positive
@pytest.mark.parametrize("input_string, result", [
    ("   кузнечик", "кузнечик"),
    (" How do you do", "How do you do"),
    ("  weetyuiopp", "weetyuiopp")])
def test_trim_positive(input_string, result):
    assert string_utils.trim(input_string) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_string, result", [
    ("", ""), ("  ", ""), ("No space", "No space")])
def test_trim_negative(input_string, result):
    assert string_utils.trim(input_string) == result


@pytest.mark.positive
@pytest.mark.parametrize("input_string, look_symbol, bool", [
     ("Кузнечик", "к", True), ("Тест на пробел", " ", True),
     ("Цифры 345", "5", True)])
def test_contains_positive(input_string, look_symbol, bool):
    assert string_utils.contains(input_string, look_symbol) == bool


@pytest.mark.negative
@pytest.mark.parametrize("input_string, look_symbol, bool", [
     ("", "к", False), ("Нет символа", "з", False)])
def test_contains_negative(input_string, look_symbol, bool):
    print(string_utils.contains)
    assert string_utils.contains(input_string, look_symbol) == bool


@pytest.mark.positive
@pytest.mark.parametrize("input_string, del_symbol, result", [
                         ("Кузнетчик", "т", "Кузнечик"),
                         ("Hello cursed world", "cursed ", "Hello world"),
                         ("IfonPRO16", "16", "IfonPRO")])
def test_delete_symbol_positive(input_string, del_symbol, result):
    assert string_utils.delete_symbol(input_string, del_symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("input_string, del_symbol, result", [
                         ("", "123", ""),
                         ("Hello world", "321", "Hello world")])
def test_delete_symbol_negative(input_string, del_symbol, result):
    assert string_utils.delete_symbol(input_string, del_symbol) == result
