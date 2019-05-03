from mysql.connector import MySQLConnection, Error
import matplotlib.pyplot as plt

def get_data_from(table):
    '''conecting to db and get average value from table_avg '''

    try:
        conn = MySQLConnection( host='localhost',
                                database='pars_db',
                                user='root',
                                password='12345')
        if conn.is_connected():
            print('Connected to MySQL database')

        cursor = conn.cursor()
        sql_select_query = "SELECT * FROM {} ".format(table)
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

    except Error as e:
        print('Error:', e)
    finally:
        cursor.close()
        conn.close()
    return records


def prepare_data_for_graph(db_table):
    x_years=[]
    y_price=[]
    for years, price in sorted(get_data_from(db_table)):
        x_years.append(years)
        y_price.append(price)

    return x_years, y_price


def display_graph(*args):
    plt.plot(megane_years, megane_price, label='Renault Megane')#scatter
    plt.plot(golf_years, golf_price, label='Volkswagen Golf')
    plt.plot(fabia_years, fabia_price, label='Skoda Fabia')
    plt.gca().invert_xaxis()
    plt.xlabel('Years of production')
    plt.ylabel('Price of cars in $')

    plt.title('Analysis of Ukrainian car market')
    plt.legend()
    plt.show()


megane_years, megane_price = prepare_data_for_graph('megan_avg')
golf_years, golf_price = prepare_data_for_graph('golf_avg')
fabia_years, fabia_price = prepare_data_for_graph('fabia_avg')

display_graph()