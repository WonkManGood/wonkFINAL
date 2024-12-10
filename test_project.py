from project import encrypt, open_cipher, clear
from pytest import raises

def test_general_encrypt():
    assert encrypt('test') == '┌──────────────┐\n│  #@+$###@    │\n│              │\n│              │\n│              │\n│              │\n└──────────────┘\n   wonkCIPHER\n'
    assert encrypt('cs50') == '┌──────────────┐\n│  +###@/$@    │\n│              │\n│              │\n│              │\n│              │\n└──────────────┘\n   wonkCIPHER\n'

def test_space_usage_encrypt():
    assert encrypt('cs50 was cool') == '┌──────────────┐\n│  +###@/$@/+  │\n│  #/++##/++#  │\n│  */*/*@      │\n│              │\n│              │\n└──────────────┘\n   wonkCIPHER\n'

def special_characters_encrypt():
    assert encrypt('!!@@') == '┌──────────────┐\n│  $$$$$%$%    │\n│              │\n│              │\n│              │\n│              │\n└──────────────┘\n   wonkCIPHER\n'

def errors_encrypt():
    with raises(ValueError):
        encrypt("12345678901234567890123456")
        encrypt("")

def test_open_cipher():
    assert open_cipher() == [{'input': 'a', 'output': '++'}, {'input': 'b', 'output': '+*'}, {'input': 'c', 'output': '+#'}, {'input': 'd', 'output': '+@'}, {'input': 'e', 'output': '+$'}, {'input': 'f', 'output': '+%'}, {'input': 'g', 'output': '+/'}, {'input': 'h', 'output': '+\\'}, {'input': 'i', 'output': '*+'}, {'input': 'j', 'output': '**'}, {'input': 'k', 'output': '*#'}, {'input': 'l', 'output': '*@'}, {'input': 'm', 'output': '*$'}, {'input': 'n', 'output': '*%'}, {'input': 'o', 'output': '*/'}, {'input': 'p', 'output': '*\\'}, {'input': 'q', 'output': '#+'}, {'input': 'r', 'output': '#*'}, {'input': 's', 'output': '##'}, {'input': 't', 'output': '#@'}, {'input': 'u', 'output': '#$'}, {'input': 'v', 'output': '#%'}, {'input': 'w', 'output': '#/'}, {'input': 'x', 'output': '#\\'}, {'input': 'y', 'output': '@+'}, {'input': 'z', 'output': '@*'}, {'input': '1', 'output': '@#'}, {'input': '2', 'output': '@@'}, {'input': '3', 'output': '@$'}, {'input': '4', 'output': '@%'}, {'input': '5', 'output': '@/'}, {'input': '6', 'output': '@\\'}, {'input': '7', 'output': '$+'}, {'input': '8', 'output': '$*'}, {'input': '9', 'output': '$#'}, {'input': '0', 'output': '$@'}, {'input': '!', 'output': '$$'}, {'input': '@', 'output': '$%'}, {'input': '#', 'output': '$/'}, {'input': '$', 'output': '$\\'}, {'input': '%', 'output': '%+'}, {'input': '^', 'output': '%*'}, {'input': '&', 'output': '%#'}, {'input': '*', 'output': '%@'}, {'input': '(', 'output': '%$'}, {'input': ')', 'output': '%%'}, {'input': '-', 'output': '%/'}, {'input': '+', 'output': '%\\'}, {'input': ' ', 'output': '/+'}]

def test_clear():
    assert clear() == None