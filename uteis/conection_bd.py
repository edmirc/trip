import mysql.connector


class Connect:
    __dados:dict = {'user': 'remoto', 
                  'host': '192.168.3.198', 
                  'password': '@Remote@Mysql025978',
                  'database': 'trip1'}
    def __init__(self):
        self.__con = self.connection()
        self.__cursor = self.con_cursor()

    def __connection(self):
        try:
            con = mysql.connector.connect(
                user = self.dados['user'],
                host = self.dados['host'],
                password = self.dados['password'],
                database = self.dados['database']
            )
            return con
        except mysql.connector.Error as err:
            print('erro ao conectar o banco: ' + err)
            return None
    
    def __con_cursor(self):
        if self.__con is not None:
            return self.con.cursor()
        else:
            return None
        
    def __close_con(self):
        self.__con.close()
    
    def insert_update(self, sql: str):
        self.__cursor.execute(sql)
        self.__con.commit()
        self.__close_con()