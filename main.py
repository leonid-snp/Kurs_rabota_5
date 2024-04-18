from src.config import config
from src.utils import get_hh_data, create_database, save_data_to_database
from src.classes import DBManager


def main():
    print("Добро пожаловать!\n"
          "Начинаем поиск вакансий...\n")
    api_hh_ru = 'https://api.hh.ru/vacancies'
    company_ids = [
        '1473866',
        '4023',
        '205',
        '4219',
        '23040',
        '740',
        '3838',
        '1057',
        '1180',
        '208707',
        '1740'
    ]

    params = config()

    data = get_hh_data(api_hh_ru, company_ids)
    print("Создаем базу данных...\n")
    create_database('hh_data', params)
    print("Сохраняем результат поиска...\n")
    save_data_to_database(data, 'hh_data', params)

    print("Данные записались успешно!\n")
    answer = int(input("Список цифр для перехода по меню - (1, 2, 3, 4, 5)\n"
                       "Выберите что хотите сделать, введите цифру для перехода по меню: "))

    db_manager = DBManager()

    if answer == 1:
        db_manager.get_companies_and_vacancies_count('hh_data', params)
    elif answer == 2:
        db_manager.get_all_vacancies('hh_data', params)
    elif answer == 3:
        db_manager.get_avg_salary('hh_data', params)
    elif answer == 4:
        db_manager.get_vacancies_with_higher_salary('hh_data', params),
    if answer == 5:
        word = input("Введите слово для поиска: ")
        db_manager.get_vacancies_with_keyword('hh_data', params, word)


if __name__ == '__main__':
    main()
