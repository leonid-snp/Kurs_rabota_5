def get_hh_data(api_key: str, company_ids: list[str]) -> list[dict]:
    """
    Получает данные о компаниях и вакансиях с помощью API HH.ru

    :param api_key: (str) публичный ключ к API
    :param company_ids: (list[str]) список компаний

    :return: (list[dict]) список данных о компаниях и их вакансиях
    """
    pass


def create_database(db_name: str, params: dict) -> None:
    """
    Создает базу данных о компаниях и их вакансиях

    :param db_name: (str) название базы данных
    :param params: (dict) параметры подключения к базе данных
    """
    pass


def save_data_to_database(data: list[dict], db_name: str, params: dict) -> None:
    """
    Сохраняет данные о компаниях и их вакансиях в базу данных

    :param data: (list[dict]) список данных о компаниях и их вакансиях
    :param db_name: (str) название базы данных
    :param params: (dict) параметры подключения к базе данных
    """