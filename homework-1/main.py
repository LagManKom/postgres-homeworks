"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def main():
    conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='123KNOPka456')
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/customers_data.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute(
                            f'INSERT INTO customers_data (customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                            (row["customer_id"], row["company_name"], row["contact_name"]))

                with open('north_data/employees_data.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute(
                            f'INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_date, notes)'
                            f' VALUES (%s, %s, %s, %s, %s, %s)',
                            (row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"],
                             row["notes"]))
                #
                with open('north_data/orders_data.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute(
                            f'INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)'
                            f' VALUES (%s, %s, %s, %s, %s)',
                            (row["order_id"], row["customer_id"], row["employee_id"], row['order_date'],
                             row['ship_city']))

    finally:
        conn.close()


if __name__ == '__main__':
    main()
