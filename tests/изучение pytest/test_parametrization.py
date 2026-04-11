import pytest
from _pytest.fixtures import SubRequest

"""Значения в массиве означают, что тест будет запущен 4 раза,
     на каждом запуске будет применено последовательно значение"""
@pytest.mark.parametrize('number', [1,2,3,-1])
def test_numbers(number:int):
    assert number > 0

#def test_several_numbers_1():
#    assert 1**2==1

#def test_several_numbers_2():
#    assert 2**2==4

#def test_several_numbers_3():
#    assert 3**2==9

"""Эти тесты о возведении в квадрат можно переписать короче:"""
@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9)])
def test_several_numbers(number:int, expected:int):
    assert number**2==expected

@pytest.mark.parametrize('browsers', ['chromium','webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macos','windows', 'linux','debian'])
def test_multiplication_of_numbers(os:str, browsers:str):
    assert len(os+browsers)>0

@pytest.fixture(params=['chromium','webkit', 'firefox'])
def browser(request:SubRequest):
    return request.param

def test_open_browser(browser:str):
    print(f"Running test on browser: {browser}")

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user:str, account:str):
        print(f"Running test for user: {user} and account: {account}")

    def test_user_without_operations(self, user:str):
        print(f"Running test for user: {user} without operations")

users={
    '+70000000011':'User with money on bank account',
    '+70000000022':'User without money on bank account',
    '+70000000033':'User with operations on bank account'
}

#@pytest.mark.parametrize('phone_number', ['+70000000011', '+70000000022', '+70000000033'],
#                         ids=['User with money on bank account',
#                              'User without money on bank account',
#                              'User with operations on bank account'])
#def test_identifiers(phone_number:str):
# ...

"""Перепишем верхний тест через словарь"""
users={
    '+70000000011':'User with money on bank account',
    '+70000000022':'User without money on bank account',
    '+70000000033':'User with operations on bank account'
}
@pytest.mark.parametrize('phone_number', users.keys(),
                         ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifiers(phone_number:str):
    ...