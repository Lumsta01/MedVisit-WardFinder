import sqlite3

conn = sqlite3.connect("visitor_patient_database.db")
c = conn.cursor()
print("database initialised")

def visitors_table():
    c.execute("""CREATE TABLE IF NOT EXISTS visitors
              (visitor_id INTEGER PRIMARY KEY AUTOINCREMENT,
              full_name TEXT NOT NULL,
              id_number TEXT UNIQUE NOT NULL,
              contact TEXT NOT NULL,
              relation TEXT NOT NULL,
              photo BLOB,
              visit_time TIMESTAMP DEFAULT CURRENT_TIME,
              patient_id INTEGER,
              FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
              )""")
    
def patients_table():
    c.execute("""CREATE TABLE IF NOT EXISTS patients(
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        id_number TEXT UNIQUE NOT NULL,
        hospital_id TEXT NOT NULL,
        ward_number TEXT NOT NULL,
        allowed_visitors TEXT,
        status TEXT NOT NULL,
        qrcode TEXT)""")
    

def visits_log_table():
    c.execute("""CREATE TABLE IF NOT EXISTS visit_log(
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_id INTEGER,
        patient_id INTEGER,
        visit_time TIMESTAMP DEFAULT CURRENT_TIME,
        FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id),
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )""")
    
visitors_table()
patients_table()
visits_log_table()