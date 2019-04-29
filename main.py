from prettytable import PrettyTable
import csv

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']


months_dict = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12"
}


def convert_date(date):
    month = date.split('-')[0]
    date = date.replace(month, months_dict[month])
    date = date.replace('-', '/')
    return date


def display_table(PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP):
    """
    Display product table
    """

    EXPIRES_START = convert_date(EXPIRES_START)
    EXPIRES_STOP = convert_date(EXPIRES_STOP)

    with open('products.csv') as csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue

                if (PRICE_MAX > float(row[2]) > PRICE_MIN) and (EXPIRES_STOP > row[3] > EXPIRES_START):
                    table.add_row(row)
        finally:
            csv_file.close()

    print(table)
    table.clear_rows()


def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        PRICE_MIN = float(input('PRICE_MIN > '))
        PRICE_MAX = float(input('PRICE_MAX > '))
        EXPIRES_START = input('EXPIRES_START (MAR-01-2019) > ')
        EXPIRES_STOP = input('EXPIRES_STOP (MAR-31-2019) > ')
        display_table(PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP)


if __name__ == '__main__':
    start()
