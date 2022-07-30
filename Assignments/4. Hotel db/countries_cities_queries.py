import pymysql
from faker import Faker
fake = Faker()

# ---------------------------------------------------------------
# DB:  countries_cities

con = pymysql.connect(host="localhost",user="root", password="",
                      database="countries_cities")
print("Database connected.")
cur = con.cursor()

# insert into country table
country_id=0
for i in range(1,101):
    country_id+=1
    country=fake.country()
    insert_query = "insert into country(id, country_name) values(%s,%s);"
    insert_data = (country_id,country)
    cur.execute(insert_query,insert_data)
    con.commit()

# ----------------------------------------------------------------

### insert into city table

# cities in Italy
country_id=51
country="Italy"
city_id=0
for i in range(1,11):
    city_id+=1
    locale = "it_It"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()

# cities in india
country_id=78
country="India"
city_id=10
for i in range(1,11):
    city_id+=1
    locale = "en_In"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()


# cities in canada
country_id=77
country="Canada"
city_id=20
for i in range(1,10):
    city_id+=1
    locale = "en_Ca"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()

# cities in France
country_id=6
country="France"
city_id=50
for i in range(1,10):
    city_id+=1
    locale = "fr_Fr"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()

# cities in Indonesia
country_id=50
country="Indonesia"
city_id=56
for i in range(1,10):
    city_id+=1
    locale = "id_ID"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()

# cities in Austria
country_id=63
country="Austria"
city_id=77
for i in range(1,10):
    city_id+=1
    locale = "de_AT"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()

# cities in Brazil
country_id=12
country="Brazil"
city_id=86
for i in range(1,15):
    city_id+=1
    locale = "pt_BR"
    fake = Faker(locale)
    city = fake.city()
    fake=Faker()
    postal_code = fake.zipcode()
    insert_query="insert into city(id,city_name,postal_code,country_id) values(%s,%s,%s,%s)"
    insert_data = (city_id, city, postal_code, country_id)
    cur.execute(insert_query,insert_data)
    con.commit()


con.close()

# ----------------------------------------------------------------






























