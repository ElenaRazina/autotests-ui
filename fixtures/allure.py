import pytest
from tools.allure.enviroment import create_allure_enviroment_file

@pytest.fixture(scope="session",autouse=True)
#фмксиура будет выполнена автоматически без необходимости ее вызова
def save_allure_enviroment_file():
    yield
    create_allure_enviroment_file()