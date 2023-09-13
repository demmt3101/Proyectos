import psycopg2

class StudentDb:
    def __init__(self) -> None:
        self._conn = psycopg2.connect("dbname=ejercicio1_2 user=pucetec01 password=pucetec01 host=localhost")
        self._conn = psycopg2.connect("dbname=dennis3101 user=postgres password=3101 host=localhost")
        self._cur = self._conn.cursor()
    
    
    def get_students(self):
        query = "SELECT * FROM students ORDER BY last_name"
        self._cur.execute(query)
        return self._cur.fetchall()