

def registration(login: str, password: str, name: str, email: str):
    """
    API Сервиса Регистрации, предоставляющая возможность регистрации пользователя, занесение
    пользователя в Базу Данных.
    Параметры сериализуются в JSON, сохраняются в БД (Таблица User).
    Метод: POST
    :param Login: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :param Password: Пароль пользователя - строка, состоящая из набора латинских букв и цифр, величиной от 6 символов
    :param Name: Имя пользователя - строка, состоящая из набора латинских или кириллических букв, допустимы пробелы
    :param Email: Email пользователя - строка, соответсвующая правилам валидации Email.
    Должен быть уникальным в рамках БД
    :return: HTTP Response, статус ответа, сообщение о результатах регистрации
    """


def authorization(login: str, password: str):
    """
    API Сервиса Авторизации, предоставляющая возможность авторизации пользователя, на основе данных,
    полученых из БД.
    Параметры сериализуются в JSON, сравниваются с данными из БД, Клиенту возвращается Токен из БД (Таблица Token).
    Метод: GET
    :param login: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :param password: Пароль пользователя - строка, состоящая из набора латинских букв и цифр, величиной от 6 символов
    :return: Токен пользователя, HTTP Response, статус ответа, сообщение о результатах авторизации
    """


def send_message(recipientLogin: str, message: str, token: str):
    """
    API Сервиса Чата. предоставляющая возможность сохранения сообщения в Очередь сообщений
    Параметры сериализуются в JSON, сохраняются в очередь сообщений.
    Метод: POST
    :param recipientLogin: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :param message: Сообщение - строка длины до 200 символов. допустимы любые символы
    :param token: Токен - строка, состоящая из латинских букв и/или цифр,
    :return: HTTP Response, статус ответа
    """


def recieve_message(token: str, login: str):
    """
    API Сервиса обработки сообщений, предоставляющая возможность получения сообщений пользователем
    Параметры сериализуются в JSON, Токен сравнивается с данными из БД (Таблица Token). По Логину из очереди сообщений
    выбираются сообщения с полем "получатель", совпадающим с указанным логином.
    Клиенту возвращается JSON с сообщениями и логинами отправителя
    Метод: GET
    :param token: Токен - строка, состоящая из латинских букв и/или цифр,
    :param login: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :return: HTTP Response, статус ответа, JSON список объектов с полями "логин отправителя" и "соообщение"
    """


def online_alert(login: str):
    """
    API Сервиса обработки сообщений, предоставляющая возможность получения пользователем, сообщений, отправленных ему,
    пока он находился в режиме Offline. Внутреннее API. Обращение к Сервису обработки сообщений от ервиса Авторизации
    Параметры сериализуются в JSON, Клиенту возвращается JSON с сообщениями и логинами отправителей из очереди сообщений
    Метод: GET
    :param login: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :return: HTTP Response, статус ответа, JSON список объектов с полями "логин отправителя" и "соообщение"
    """


def show_history(token: str, friendlogin: str, timeFrom: str, timeTo: str):
    """
    API Сервиса истории сообщений, предоставляющая возможность получения истории сообщений между пользователями.
    Параметры сериализуются в JSON, Токен сравнивается с данными из БД (Таблица Token). По Логину из БД (таблица Messages)
    выбираются сообщения конкретного собеседника за указанный временной интервал
    Клиенту возвращается JSON с сообщениями собеседника
    Метод: GET
    :param token: Токен - строка, состоящая из латинских букв и/или цифр,
    :param friendlogin: Логин пользователя - строка, состоящая из латинских букв и/или цифр, допустим знак "_".
    Должен быть уникальным в рамках БД
    :param timeFrom: Начало временного промежутка истории сообщений - строка, соответствующая типу
    DATETIME в БД (таблица Messages).
    :param timeTo: Конец временного промежутка истории сообщений - строка, соответствующая типу
    DATETIME в БД (таблица Messages).
    :return: HTTP Response, статус ответа, JSON с сообщениями собеседника
    """
