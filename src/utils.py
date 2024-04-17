import requests
import psycopg2


def get_count_pages(api_key: str, company_id: str) -> int:
    """
    Получает количество страниц в файле Json

    :param api_key: (str) публичный ключ к API
    :param company_id: (str) название компании
    :return:
    """
    hh_data = requests.get(api_key, params={
        "employer_id": company_id,
        "per_page": 100,
        "area": 1
    })

    return hh_data.json()["pages"]


def get_hh_data(api_key: str, company_ids: list[str]) -> list[dict]:
    """
    Получает данные о компаниях и вакансиях с помощью API HH.ru

    :param api_key: (str) публичный ключ к API
    :param company_ids: (list[str]) список компаний

    :return: (list[dict]) список данных о компаниях и их вакансиях
    """

    vacancy = []
    for company_id in company_ids:
        page = 0
        pages = get_count_pages(api_key, company_id)
        while page != pages:
            hh_data = requests.get(api_key, params={
                "employer_id": company_id,
                "page": page,
                "per_page": 100,
                "area": 1
            })

            print(hh_data.json())
            vacancy.extend(hh_data.json().get('items'))
            page += 1

    return vacancy


def create_database(db_name: str, params: dict) -> None:
    """
    Создает базу данных о компаниях и их вакансиях

    :param db_name: (str) название базы данных
    :param params: (dict) параметры подключения к базе данных
    """
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    conn.close()

    conn = psycopg2.connect(dbname=db_name, **params)
    with conn.cursor() as cur:
        cur.execute(f"CREATE TABLE vacancy ("
                    f"id SERIAL PRIMARY KEY NOT NULL,"
                    f"name VARCHAR(60),"
                    f"company VARCHAR(60),"
                    f"salary INTEGER,"
                    f"link VARCHAR(255))")

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict], db_name: str, params: dict) -> None:
    """
    Сохраняет данные о компаниях и их вакансиях в базу данных

    :param data: (list[dict]) список данных о компаниях и их вакансиях
    :param db_name: (str) название базы данных
    :param params: (dict) параметры подключения к базе данных
    """