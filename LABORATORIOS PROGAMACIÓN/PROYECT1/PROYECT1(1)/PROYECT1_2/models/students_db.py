import psycopg2

class StudentsDb:
    def __init__(self) -> None:
        #self._conn = psycopg2.connect("dbname=ejercicio1_2 user=pucetec01 password=pucetec01 host=localhost")
        self._conn = psycopg2.connect("dbname=dennis3101 user=postgres password=3101 host=localhost")
        self._cur =self._conn.cursor()
        
    def get_students(self):
        self._cur.execute("SELECT * FROM students ORDER BY last_name")
        return self._cur.fetchall()
    
    def create_student(self, first_name, last_name, email):
        self._cur.execute("insert into students (first_name, last_name, email) values (%s, %s, %s)", (first_name, last_name, email))
        self._conn.commit()
    
    def update_student(self, id, first_name, last_name, email):
        try:
            self._cur.execute("UPDATE students SET first_name = %s, last_name = %s, email = %s WHERE id = %s",(first_name, last_name, email, id))
            self._conn.commit()
            return True
        except Exception as e:
            print (e) 
            return False
        
    def delete_student(self, id):
        self._cur.execute("DELETE FROM students WHERE id = %s", (id,))
        self._conn.commit()
    
    def close(self):
        self._cur.close()
        self._conn.close()
    
    
