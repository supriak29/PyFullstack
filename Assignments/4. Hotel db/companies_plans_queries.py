import pymysql
from faker import Faker
import random as r

con = pymysql.connect(host="localhost",user="root", password="",
                      database="companies_plans")
print("Database connected.")
cur = con.cursor()

def insertDB(company_id,company_name,vat,email,city_id,address,details,is_active):
    # insert query
    insert_query = """insert into company(id,company_name,VAT_ID,email,
                                            city_id,company_address,details,
                                            is_active)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"""
    insert_data = (company_id,company_name,vat,email,city_id,address,details,is_active)
    cur.execute(insert_query,insert_data)
    con.commit()

fake=Faker()

#---------------------------------------------------------------------
# India
##country_id=78
##country="India"
company_id=0
ctid=[11,12,13,14,15,16,17,18,19,20] # 11-20
vat = "IN "
active=[True,False]
for i in range(1,10):
    vat = "IN "
    company_id+=1
    company_name = fake.company()

    for i in range(1,16):
        vat+=str(r.randint(1,9))

    email = ''.join(filter(str.isalnum, company_name)) 
    email = email.lower()+"@gmail.com"

    city_id = r.choice(ctid)
    address = fake.address()
    details = fake.text()
    is_active = r.choice(active)

    insertDB(company_id,company_name,vat,email,city_id,address,details,is_active)  


#---------------------------------------------------------------------

# Italy
##country_id=78
##country="Italy"
company_id=9
ctid=[1,2,3,4,5,6,7,8,9,10] 
vat = "IT "
active=[True,False]
for i in range(1,20):
    vat = "IN "
    company_id+=1
    company_name = fake.company()

    for i in range(1,12):
        vat+=str(r.randint(1,9))

    email = ''.join(filter(str.isalnum, company_name)) 
    email = email.lower()+"@gmail.com"

    city_id = r.choice(ctid)
    address = fake.address()
    details = fake.text()
    is_active = r.choice(active)

    insertDB(company_id,company_name,vat,email,city_id,address,details,is_active)  

# ----------------------------------------------------------------------







    
con.close 




