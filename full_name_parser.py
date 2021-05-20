import argparse

from bs4 import BeautifulSoup as bs


class FullNameParser:
    """
==================================================
Класс предназначен для парсинга ФИО из html-файла.
==================================================
    """
    def __init__(self, html_to_parse: str):
        self.html = html_to_parse

    def __str__(self):
        return self.html

    def __repr__(self):
        return self.html

    def get_data_from_html(self) -> str:
        """Функция получает все данные со страницы html."""
        with open(self.html, 'r', encoding='utf-8') as file:
            data = file.read()
        return data

    def parse_html_to_get_required_tag(self) -> list:
        """Функция парсит все данные и отбирает только необходимые теги."""
        data_to_parse = self.get_data_from_html()

        soup = bs(data_to_parse, 'lxml')
        all_p_tags = soup.find_all('p', {'class': 'full_name'})

        return all_p_tags

    def analyze_tag_to_get_full_name(self) -> str:
        """Функция анализирует отобранные данные и выводит результат в консоль."""
        data_to_analyze = self.parse_html_to_get_required_tag()

        if not data_to_analyze:
            print('Необходимые теги не обнаружены.')

        for data in data_to_analyze:
            data = str(data)

            cleaned_data = data[21:len(data) - 4]
            if cleaned_data == ' ':
                cleaned_data = 'Не_указано'

            cleaned_data_list = cleaned_data.split()
            if len(cleaned_data_list) >= 4:
                print('Упс! Кажется, мы нашли то, что не поддается автоматической обработке.')
            elif len(cleaned_data_list) == 3:
                print(f'Ура! Мы нашли фамилию: {cleaned_data_list[0]}, имя: {cleaned_data_list[1]}, '
                      f'отчество: {cleaned_data_list[2]}!')
            elif len(cleaned_data_list) == 2:
                print(f'Ура! Мы нашли фамилию: {cleaned_data_list[0]}, имя: {cleaned_data_list[1]}!')
            elif len(cleaned_data_list) == 1:
                print(f'Ура! Мы нашли фамилию: {cleaned_data_list[0]}!')
            else:
                print('Упс! Кажется, мы нашли что-то слишком сложное :(')

        print()
        return f'Анализ файла {self.html} завершен.'


def main(html_to_parse: str) -> list:
    """Функция создает экземпляр класса FullNameParser и запускает парсинг."""
    parser = FullNameParser(html_to_parse)
    print(f'Приступаю к анализу файла {html_to_parse}.')
    print()
    data = parser.analyze_tag_to_get_full_name()
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсинг ФИО из html-файла')
    parser.add_argument('html_to_parse', type=str, help='Укажите html-файл для парсинга')
    args = parser.parse_args()

    print(main(args.html_to_parse))
