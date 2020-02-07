# Clase: Csv_parser
#   init('nombre de fichero csv') Abre el CSV y lo parsea
#   set_user(username)
#   user_volume(): Da el volumen de copias del usuario
#   user_used(): Da el numero de copias gastadas del
#   user(): Develve

class Csv_parser:
    filename=""
    def __init__(self, the_filename):
        self.filename = the_filename
        import csv
        try:
            self.csvfile = open(self.filename)
            self.reader = csv.DictReader(self.csvfile)
        except:
            print("No se encuentra el archivo")

    def return_users(self):
        l = []
        for row in self.reader:
            u = {}
            u['usercode'] = row['User'][1:-1]
            u['name'] = row['Name'][1:-1]
            u['copias_max'] = row['Limit Value(Print Volume Use Limitation)']
            u['copias_used'] = row['Volume Used(Print Volume Use Limitation)']
            l.append(u)
        self.seek0()
        return l

    def seek0(self):
        self.csvfile.seek(0)
        self.reader.__next__()