
class Program:
    
    console = ""
    errores = []
    tabla = {}
    
    
    def printTabla(tabla):
        for sim in tabla:
            print("Id: ", sim, " | TipoS: ", tabla[sim][0].simbolo, " | TipoD: ", tabla[sim][0].tipo.tipo, " | Ambito: ", tabla[sim][1]) 
    
    