import logging
#импорт стандартного модуля логирования, у него есть уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL.

def get_logger(name:str)->logging.Logger:
    #создание логгера c именем name
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #будут писаться логи от уровня DEBUG и выше
    handler=logging.StreamHandler() #будет писаться в консоль, а не в файл
    #задаем минимальный уровень для handler
    #уровень есть и у logger, и у handler
    handler.setLevel(logging.DEBUG)
    #задаем внешний вид сообщения
    formatter=logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    #Привязываем форматтер к handler
    #Т.е. говорим, когда будешь выводить лог в консоль, используй вот такой формат
    handler.setFormatter(formatter)
    #Добавляем handler к logger.
    #Без этой строки логгер может существовать, но не знать, куда выводить сообщения.
    #Связь такая: logger -> handler -> formatter -> console
    logger.addHandler(handler)
    return logger

#logger=get_logger("autotests-ui")
#logger.info("Hello from info")
#logger.warning("Hello from warning")

#Logger — кто пишет лог
#Handler — куда писать лог
#Formatter — как выглядит лог
