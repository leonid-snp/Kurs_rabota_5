from src.config import config
from src.utils import get_hh_data, create_database, save_data_to_database


def main():
    api_hh_ru = 'https://api.hh.ru/vacancies'
    company_ids = [
        'HeadHunter'
    ]

    params = config()

    data = get_hh_data(api_hh_ru, company_ids)
    create_database('hh_data', params)
    save_data_to_database(data, 'hh_data', params)


if __name__ == '__main__':
    main()
