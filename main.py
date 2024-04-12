from src.config import config
from src.utils import get_hh_data, create_database, save_data_to_database


def main():
    api_hh_ru = 'https://api.hh.ru/vacancies' # 'https://api.hh.ru/employers'
    company_ids = [
        '1473866', # Сбербанк-Сервис 1.
        '4023', # Райффайзен Банк 2.
        '205', # Марс 3.
        '4219', # Tele2 4.
        '23040', # Банк Открытие 5.
        '740', # Норникель 6.
        '3838', # Компания ПЭК 7.
        '1057', # Лаборатория Касперского 8.
        '1180', # Bayer 9.
        '208707', # ВсеИнструменты.ру 10.
        '1740' # Яндекс 11.
    ]

    params = config()

    data = get_hh_data(api_hh_ru, company_ids)
    print(len(data))
    # create_database('hh_data', params)
    # save_data_to_database(data, 'hh_data', params)


if __name__ == '__main__':
    main()
