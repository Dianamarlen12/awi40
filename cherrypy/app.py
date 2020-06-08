import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World desde CherryPy!"

cherrypy.quickstart(HelloWorld())