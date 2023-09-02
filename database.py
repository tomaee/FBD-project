import psycopg2

class Database:
 
  def __init__(self) -> None:
    self.conn= None
    self.cur = None
    pass
  
  def accesDatabase(self):
    try:
      self.conn = psycopg2.connect(host = "localhost",
                                  dbname = "video_demonstration",
                                  user = "postgres",
                                  password = "1355",
                                  port = "5432")
      self.cur = self.conn.cursor()


      
    except Exception as error:
      print(error)

  def closeDatabase(self):
    if self.cur is not None:
        self.cur.close()
    if self.conn is not None:
        self.conn.close()

  def modifyDatabase(self, query, specs):
    try:
      self.cur.execute(query, specs)

      self.conn.commit()
    except Exception as error:
      print(error)


  def browseDatabase(self, query, specs):
    try:  
      self.cur.execute(query % specs)
      print(self.cur.fetchall())
    except Exception as error:
      print(error)



  def teste(self):
     print(f"{self.conn} {self.cur}")
