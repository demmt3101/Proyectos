import psycopg2

class StudentDB:
    def __init__(self) -> None:
        self._conn = psycopg2.connect("dbname=ejercicio1_2 user=pucetec01 password=pucetec01 host=localhost")
        self._conn = psycopg2.connect("dbname=dennis3101 user=postgres password=3101 host=localhost")
        self._cur = self._conn.cursor()
    
    
    def get_students(self):
        query = "SELECT * FROM students ORDER BY last_name"
        self._cur.execute(query)
        return self._cur.fetchall()
        
    def create_students(self, first_name, last_name, email):
        query = "INSERT INTO students (first_name, last_name, email)\
        VALUES (%s, %s, %s)"
        self._cur.execute(query, (first_name, last_name, email))
        self._conn.commit()
    
    def update_student(self,student_id, first_name, last_name, email):
        query = "UPDATE students SET first_name=%s, last_name=%s, email=%s \
            WHERE student_id=%s "
        if self.__student_db.update_student(
            rowValues[0],
            rowValues[1],
            rowValues[2],
            rowValues[3]
        ):
            msg = "El estudiante fue guardado exitosamente"
        else:
            msg = "Hubo un problema al guardar el estudiante!!!"

        self._cur.execute(query, (first_name, last_name, email, student_id))
        self._conn.commit()


    def close(self):
        self._cur.close()
        self._conn.close()
