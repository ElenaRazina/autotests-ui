from config import settings
import platform
import sys

def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f"{key}={value}" for key, value in settings.model_dump().items()]
    # Добавляем информацию об операционной системе и версии Python
    items.append(f"os_info={platform.system()} {platform.release()}")
    #platform.system() - возвращает название ОС
    #platform.release() - возвращает версию ОС
    items.append(f"python_version={sys.version}")
    #settings.model_dump() вернет нам настройки из settings в формате словаря
    #{
    #    "app_url": "https://example.com",
    #    "headless": True,
    #    "browser": [
    #        "chromium"],
    #}
    #.items() - вернет пары (ключ, значение)
    #("app_url",
    # "https://example.com")
    #("headless", True)
    #("browser", ["chromium"])
    #цикл перебирает пары и создает сроку формата
    #"app_url = https: // example.com",
    #"headless = True",
    #"browser = ['chromium']"
    # Собираем все элементы в единую строку с переносами
    properties="\n".join(items)
    #.joinpath - добавление имени файла к пути
    with open(settings.allure_results_dir.joinpath("environment.properties"), "w+") as file:
        # Записываем переменные в файл
        file.write(properties)



# w+ - открыть файл для записи и чтения, если файла нет — создать, если файл есть — очистить его содержимое