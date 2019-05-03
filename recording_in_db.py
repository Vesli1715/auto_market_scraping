from mysql.connector import MySQLConnection, Error
from scraping_data import result

def creating_main_variables(result):
    model = []
    years = []
    price = []
    for n, y, p in result:
        model.append(n)
        years.append(y)
        price.append(p)
    return model, years, price

def del_space(price):
    '''Deleting spece in price exp'14 500', make price like corect numeric'''

    new_price = []
    for p in price:
        p = p.replace(' ', '')
        new_price.append(p)
    return new_price


def sorting_data(years, new_price):
    '''Sorting data by years return new sorted lists'''

    f_years=[]
    f_price=[]
    y_and_p = zip(years, new_price)
    for y, p in sorted(y_and_p):
        f_years.append(y)
        f_price.append(p)
    return f_years, f_price



def final_data_list(model, f_years, f_price):
    '''Forming final list of data before adding to db'''

    List = []
    t = zip(model, f_years, f_price)
    for m,y,p in t:
        try:
            y = int(y)
            p = int(p)
            if p > 15000:  # protection from false data !!!changing for different cars
                p = 15000 
            List.append((m,y,p))
        except:
            print('some error') # if price=='договірна' or some other errors
    return List

def insert_data_in_db(data):

    query = "INSERT INTO megan(model,year,price) VALUES(%s,%s,%s)"
    try:
        conn = MySQLConnection( host='localhost',
                                database='pars_db',
                                user='root',
                                password='12345')
        if conn.is_connected():
            print('Connected to MySQL database')

        cursor = conn.cursor()
        cursor.executemany(query, data)
        conn.commit()

        #inserting new finally grouped values in table_avg
        query2 = "INSERT INTO megan_avg SELECT year, avg(price) FROM megan GROUP BY year"
        cursor.execute(query2)
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close()

model, years, price = creating_main_variables(result)
new_price = del_space(price) 
f_years, f_price = sorting_data(years, new_price)
List = final_data_list(model, f_years, f_price)
insert_data_in_db(List)