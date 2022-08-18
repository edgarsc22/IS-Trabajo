from flask_mysqldb import MySQL
class Infraestructure:
    def __init__(self, app):
        self.mysql=MySQL(app)
        pass    
    def existencia_login(self,cui,password):
        usuario={'cui':cui, 'password':password}
        query = "SELECT * FROM user WHERE cui=%(cui)s and password=%(password)s"
        cur=self.mysql.connection.cursor()
        cur.execute(query, usuario)
        data=cur.fetchall()
        if not data:
            return False
        else:
            return True