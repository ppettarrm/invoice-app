import mysql.connector

bazaKonekcija = mysql.connector.connect(
  host="localhost",
  user="root",
  password="petar",
  database="invoiceapp"
)

mycursor = bazaKonekcija.cursor()

def sel_all_kor():
  try:
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data
  except Exception as e:
    print(e)

def reg_kor_baza(id, username, password, name, address, city, mail, bank):
  try:
    sql = "INSERT INTO users (user_id, user_name, user_password, company_name, company_address, company_city, company_mail, company_bank_account) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, username, password, name, address, city, mail, bank)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def upd_kor_baza(id, username, password, name, address, city, mail, bank):
  try:
    sql = "UPDATE users SET user_name = %s, user_password = %s, company_name = %s, company_address = %s, company_city = %s, company_mail = %s, company_bank_account = %s WHERE user_id = %s"
    val = (username, password, name, address, city, mail, bank, id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def del_kor_baza(id):
  try:
    sql = "DELETE FROM users WHERE user_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def reg_proiz_baza(userid, id, name, price, amount, measure):
  try:
    sql = "INSERT INTO products (user_id, product_id, product_name, product_price, product_amount, product_measure) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (userid, id, name, price, amount, measure)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def edit_proiz_baza(id, name, price, amount, measure):
  try:
    sql = "UPDATE products SET product_name = %s, product_price = %s,product_amount = %s, product_measure = %s  WHERE product_id = %s"
    val = (name, price, amount, measure, id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def upd_proiz_baza(id, amount):
  try:
    sql = "UPDATE products SET product_amount = %s WHERE product_id = %s"
    val = (amount, id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def del_proiz_baza(id):
  try:
    sql = "DELETE FROM products WHERE product_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def log_in_baza(name, password):
  try:
    sql = "SELECT * FROM users WHERE user_name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    if data[2].lower() == password.lower():
      return data
  except Exception as e:
    print(e)

def name_baza(id):
  try:
    sql = "SELECT company_name FROM users WHERE user_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    return data
  except Exception as e:
    print(e)
    

def tabela_baza(id):
  try:
    sql = "SELECT * FROM products WHERE user_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    return data
  except Exception as e:
    print(e)

def prod_amount_baza(id):
  try:
    sql = "SELECT product_amount FROM products WHERE product_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    return data
  except Exception as e:
    print(e)

def pdf_baza(id):
  try:
    sql = "SELECT * FROM products WHERE product_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    return data
  except Exception as e:
    print(e)

def ins_inv_baza(brfak, id, name, price, amount, measure, userid):
  try:
    sql = "INSERT INTO invoices (invoice_id, product_id, product_name, product_price, product_amount, product_measure, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (brfak, id, name, price, amount, measure, userid)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def sel_inv_baza(id):
  try:
    sql = "SELECT * FROM invoices WHERE invoice_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    return data
  except Exception as e:
    print(e)

def bal(id):
  try:
    sql = "SELECT * FROM balance WHERE user_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    return data
  except Exception as e:
    print(e)

def reg_bal(id):
  try:
    sql = "INSERT INTO balance (user_id, user_in, user_out) VALUES (%s, %s, %s)"
    val = (id, '0.00', '0.00')
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def upd_in_bal(id, money):
  try:
    sql = "UPDATE balance SET user_in = %s WHERE user_id = %s"
    val = (money, id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)
  
def upd_out_bal(id, money):
  try:
    sql = "UPDATE balance SET user_out = %s WHERE user_id = %s"
    val = (money, id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)

def used(id):
  try:
    sql = "UPDATE invoices SET used = %s WHERE invoice_id = %s"
    val = (1,id)
    mycursor.execute(sql, val)
    bazaKonekcija.commit()
  except Exception as e:
    print(e)