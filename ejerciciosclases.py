class Persona:
    nombre=""
    apellidos=""

    def __init__(self,n,a):
        self.nombre=n
        self.apellidos=a
        pass

    def caminar(self):
        print('caminando')

profesor = Persona("antes","y despues")
print("el profesor {} {}".format(profesor.nombre,profesor.apellidos))
profesor.nombre="antonio"
profesor.apellidos="daza due"

print("el profesor {} {}".format(profesor.nombre,profesor.apellidos))
profesor.caminar()