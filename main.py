from database import Database


db = Database()
db.accesDatabase()
specs = ('123456789092')
#query = '''INSERT INTO assistiu(videoid, perfilid) VALUES (%s, %s)'''
query = "SELECT * FROM conta %s"
where = ("where cpf = '123456789092'")
db.browseDatabase(query, where)
db.closeDatabase()
