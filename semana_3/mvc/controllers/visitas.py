import web
import time 

print(time.strftime("%I:%M:%S"))
print(time.strftime("%d/%m/%y"))
class Visitas:
    def GET(self, nombre):
        try:
            hora = (time.strftime("%I:%M:%S"))
            fecha = (time.strftime("%d/%m/%y"))
            cookie = web.cookies()
            visitas = "0"
            print(cookie)
            if nombre:
              web.setcookie("nombre",nombre,expires="",domain=None)
            else:
              nombre = "NA"
              web.setcookie("nombre",nombre,expires="",domain=None) 
            if cookie.get("visitas"):
              visitas = int(cookie.get("visitas"))
              visitas += 1
              web.setcookie("visitas", str(visitas), expires="", domain=None)
            else:
              web.setcookie("visitas", str(1), expires="", domain=None)
              visitas = "1"

            return "Hora: " + str(hora) + " Fecha: " + str(fecha) + " Visitas " + str(visitas) + " Nombre " + nombre
        except Exception as e:
          return "Error" + str(e.args)