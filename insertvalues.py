import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")

conn.execute("INSERT INTO Staff3(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(1, 'Daniel', 'Kahiga', 18, 45000.00, 'Employer')")
conn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(2, 'Willian', 'Njunge', 34, 15000.00, 'Manager')")
conn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(3, 'Grace', 'Wangari', 31, 25000.00, 'HR')")
conn.execute("INSERT INTO Staff(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)\
VALUES(4, 'Felista', 'Gachugu', 18, 35000.00, 'Chef')")

conn.commit()
print("Successfully inserted values into staff table")

conn.close()