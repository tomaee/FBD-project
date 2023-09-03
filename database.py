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

      print(f'Successfully connected to database')
      
    except Exception as error:
      print(error)

  def closeDatabase(self):
    if self.cur is not None:
        self.cur.close()
    if self.conn is not None:
        self.conn.close()

  def specificModifyDatabase(self, query, specs):
    try:
      self.cur.execute(query, specs)

      self.conn.commit()
    except Exception as error:
      print(error)

  def genericModifyDatabase(self, query):
    try:
      self.cur.execute(query)

      self.conn.commit()
    except Exception as error:
      print(error)


  def specificBrowseDatabase(self, query, specs):
    try:  
      self.cur.execute(query % specs)
      print(self.cur.fetchall())
    except Exception as error:
      print(error)

  
  def genericBrowseDatabase(self, query):
    try:  
      self.cur.execute(query)
      print(self.cur.fetchall())
    except Exception as error:
      print(error)


  def callAddConta(self,newCpf, newLocal, newPlan):
    self.cur.execute("CALL addConta(%s, %s, %s)", (newCpf, newLocal, newPlan))
    self.conn.commit()
    
  def callChangePlan(self,newCpf, newPlan):
    self.cur.execute("CALL changePlan(%s, %s)", (newCpf, newPlan))
    self.conn.commit()
    



  def teste(self):
     print(f"{self.conn} {self.cur}")
