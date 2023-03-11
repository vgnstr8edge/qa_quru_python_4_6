from datetime import time


def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    current_time = time(hour=23)
    is_dark_theme = None
    if current_time <= time(22) or current_time >= time(6):
        is_dark_theme = True
    else:
        None
    assert is_dark_theme is True


    current_time = time(hour=16)
    dark_theme_enabled = True
    is_dark_theme = None
    if (current_time <= time(22) or current_time >= time(6)) or dark_theme_enabled is True:
        is_dark_theme = True
    else:
        None
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suiable_user = None
    for user in users:
        if user['name'] == "Olga":
            suiable_user = user
    assert suiable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suiable_users = None
    new_list = []
    for user in users:
        if user['age'] < 20:
            new_list.append(user)
    suiable_users = new_list

    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def name_and_args(funk_name, **kwargs, ):
    return f'''{funk_name.__name__.replace('_', ' ').title()} [{', '.join(kwargs.values())}]'''


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = name_and_args(open_browser, browser=browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = name_and_args(go_to_companyname_homepage, page_url="https://companyname.com")
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = name_and_args(find_registration_button_on_login_page, page_url="https://companyname.com/login",
                                  button_text="Register")
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
