import psycopg2

class StudentDb:
    def __init__(self) -> None:
        #self._conn = psycopg2.connect("dbname=ejercicio1 user=pucetec01 password=pucetec01 host=localhost")
        self._conn = psycopg2.connect("dbname=dennis3101 user=postgres password=3101 host=localhost")
        self._cur = self._conn.cursor()
        
    def get_students(self):
        query = "SELECT * FROM students ORDER BY last_name"
        self._cur.execute(query)
        return self._cur.fetchall()
    
    def create_students(self, first_name, last_name, email):
        query = "INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)"
        self._cur.execute(query, (first_name, last_name, email))
        self._conn.commit()
    
    def close(self):
        self._cur.close()
        self._conn.close()
        