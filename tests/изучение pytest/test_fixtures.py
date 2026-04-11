import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отпралвяем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настрокий автотестов")

@pytest.fixture(scope="class")
def user():
    print ("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION0N] Открываем браузер на каждый автотест ")

class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user,browser):
        pass

class TestAccountFlow:
    def test_user_can_login(self, settings, user,browser):
        pass