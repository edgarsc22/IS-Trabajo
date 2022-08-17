from flask_mysqldb import MySQL
class Model:
    def __init__(self, app):
        self.mysql=MySQL(app)
        pass    
    def existencia(self,cui,password):
        usuario={'cui':cui, 'password':password}
        query = "SELECT * FROM user WHERE cui=%(cui)s and password=%(password)s"
        cur=self.mysql.connection.cursor()
        cur.execute(query, usuario)
        data=cur.fetchall()
        if not data:
            return False
        else:
            return True
    def horariosemes(self,d):
        cur=self.mysql.connection.cursor()
        cur.execute('TRUNCATE TABLE horarios')
        self.mysql.connection.commit()
        cur.execute('INSERT INTO horarios SELECT * FROM horarios{}'.format(d))
        self.mysql.connection.commit()
    def actualizar(self):
        cur=self.mysql.connection.cursor()
        cur.execute("SELECT * FROM horarios")
        data = []
        contenido = {}
        resultados=cur.fetchall()
        for resultado in resultados:
            contenido={'id':resultado[0],'curso':resultado[1], 'dia':resultado[2], 'hora_inicio':resultado[3], 
                    'hora_final':resultado[4], 'profesor':resultado[5], 'grupo':resultado[6]}
            data.append(contenido)
        contenido={}
        return data
    def añadir(self,request,horasi,horasf,i,f):
        while i<=f:
            contenido={'curso':request.form['curso'], 'dia':request.form['dia'], 'hora_inicio':horasi[i], 
                        'hora_final':horasf[i], 'profesor':request.form['profesor'], 'grupo':request.form['grupo']}
            query="INSERT INTO horarios(curso,dia,hora_inicio,hora_final,profesor,grupo) VALUES(%(curso)s,%(dia)s,%(hora_inicio)s,%(hora_final)s,%(profesor)s,%(grupo)s)"
            cur=self.mysql.connection.cursor()
            cur.execute(query, contenido)
            self.mysql.connection.commit()#aqui ejecutamos la consulta
            i=i+1   
    def eliminar(self,id):
        cur=self.mysql.connection.cursor()
        cur.execute('SELECT * FROM horarios WHERE id={}'.format(id))#el format nos sirve para poder remplazar en la instruccion sql el id
        resultado=cur.fetchall()
        data=resultado[0]
        eliminador={'curso': data[1] ,'grupo': data[6]}
        cur2=self.mysql.connection.cursor()
        query="DELETE FROM horarios WHERE curso=%(curso)s and grupo=%(grupo)s"
        cur2.execute(query,eliminador)
        self.mysql.connection.commit()#se ejecuto la consulta
    def examinar(self,horasi):
        cur=self.mysql.connection.cursor()
        tup=[]
        tup2=[]
        contenido={}
        for hora in horasi:
            cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',[hora])
            resultados=cur.fetchall()
            for resultado in resultados:
                contenido={'id':resultado[0],'curso':resultado[1], 'dia':resultado[2], 'hora_inicio':resultado[3], 
                        'hora_final':resultado[4], 'profesor':resultado[5], 'grupo':resultado[6]}
                tup2.append(contenido)
            tup.append(tup2)
            contenido={}
            tup2=[]
        dia = ('Lunes','Martes','Miercoles','Jueves','Viernes')
        hor = ('07:00-07:50','07:50-08:40','08:50-09:40','09:40-10:30','10:40-11:30'
                ,'11:30-12:20','12:20-13:10','13:10-14:00', '14:00-14:50','14:50-15:40','15:50-16:40'
                ,'16:40-17:30','17:40-18:30','18:30-19:20','19:30-20:20')
        return tup,dia,hor
