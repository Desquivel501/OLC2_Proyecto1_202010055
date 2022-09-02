from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import json
from models.misc.Program import Program

from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.driver import Driver
from models.ast.ast import Ast

from analizador.parser import parser

app = Flask(__name__)
CORS(app)

# ast: Ast = parser.parse("ejecutar(1 + 1); ejecutar(1 + 1);")

# ts = TablaSimbolos(None, 'Global')
# driver = Driver()
# ast.ejecutar(driver, ts)

# print(driver.console)
@app.route("/simbolos",methods=["GET"])
def tabla_simbolos():
    if request.method == 'GET':
        return  json.dumps(Program.tabla, indent=2)
    

@app.route("/errores",methods=["GET"])
def tabla_errores():
    if request.method == 'GET':
        return  json.dumps(Program.errores, indent=2)
    
@app.route("/tablas",methods=["GET"])
def tabla_tablas():
    if request.method == 'GET':
        return  json.dumps(Program.lista_tablas, indent=2)

@app.route("/bases",methods=["GET"])
def tabla_bases():
    if request.method == 'GET':
        return  json.dumps(Program.lista_bases, indent=2)
    
    
@app.route("/interpretar",methods=["POST"])
def interpretar():
    if request.method == 'POST':
        Program.console = ""
        Program.tabla = []
        Program.errores = []
        data = request.json
        print(data)
       
        instrucciones = data.get('instrucciones')
        
        if instrucciones != "":
            
            try:

                ast: Ast = parser.parse(instrucciones)
                ts = TablaSimbolos(None, 'Main')
                ast.ejecutar(ts)
                
            except Exception as e:
                print(e)
                
            # ast: Ast = parser.parse(instrucciones)
            # ts = TablaSimbolos(None, 'Main')
            # ast.ejecutar(ts)    
            
            
            
            print(Program.lista_bases)
            
            print(Program.lista_tablas)
        
        
        # print(Program.console)
        # tabla = Program.tabla
        # Program.printTabla(tabla)
        
        return {
            'resultado': Program.console
        }


if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)