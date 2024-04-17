import psycopg2


class DBManager:
    def get_companies_and_vacancies_count(self, db_name: str, params: dict) -> None:
        """
        Получает список всех компаний и количество вакансий у каждой компании.

        :param db_name: (str) название базы данных
        :param params: (dict) параметры подключения к базе данных
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT company_name, COUNT(name) AS vacancies FROM vacancies
                GROUP BY company_name
                """)
            rows = cur.fetchall()
            print("\nСписок компаний и количество вакансий\n")
            for row in rows:
                print(f"Название компании - {row[0]}; Количество открытых вакансий - {row[1]}")

        conn.close()

    def get_all_vacancies(self, db_name: str, params: dict) -> None:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.

        :param db_name: (str) название базы данных
        :param params: (dict) параметры подключения к базе данных
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT name, company_name, salary, vacancy_url FROM vacancies
                """)
            rows = cur.fetchall()
            print("\nСписок всех вакансий\n")
            for row in rows:
                print(f"Название вакансии  - {row[0]}; "
                      f"Название компании - {row[1]}; "
                      f"Зарплата - {"Зарплата не указана" if row[2] is None else row[2]}; "
                      f"Ссылка на вакансию - {row[3]}; ")

        conn.close()

    def get_avg_salary(self, db_name: str, params: dict) -> None:
        """
        Получает среднюю зарплату по вакансиям.

        :param db_name: (str) название базы данных
        :param params: (dict) параметры подключения к базе данных
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT AVG(salary) FROM vacancies
                """)
            rows = cur.fetchall()
            for row in rows:
                print(f"\nСредняя зарплата по вакансиям - {row[0]}")

        conn.close()


    def get_vacancies_with_higher_salary(self, db_name: str, params: dict) -> None:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.

        :param db_name: (str) название базы данных
        :param params: (dict) параметры подключения к базе данных
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT name, salary FROM vacancies
                WHERE salary IS NOT NULL
                AND salary > (SELECT AVG(salary) FROM vacancies)
                """)
            rows = cur.fetchall()
            print("\nВакансии с зарплатой выше среднего\n")
            for row in rows:
                print(f"Название вакансии  - {row[0]}; "
                      f"Зарплата - {row[1]}")

        conn.close()

    def get_vacancies_with_keyword(self, db_name: str, params: dict, word: str) -> None:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например python.

        :param db_name: (str) название базы данных
        :param params: (dict) параметры подключения к базе данных
        :param word: (str) слово для фильтрации вакансий
        """
        conn = psycopg2.connect(dbname=db_name, **params)
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM vacancies "
                        f"WHERE name LIKE '{word}%'")
            rows = cur.fetchall()
            print("\nСписок найденных вакансий\n")
            for row in rows:
                print(f"Название вакансии  - {row[1]}; "
                      f"Название компании - {row[2]}; "
                      f"Зарплата - {"Зарплата не указана" if row[3] is None else row[3]}; "
                      f"Ссылка на вакансию - {row[4]}; ")

        conn.close()
