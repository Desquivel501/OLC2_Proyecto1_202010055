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


@app.route("/interpretar",methods=["POST"])
def interpretar():
    if request.method == 'POST':
        Program.console = ""
        data = request.json
        print(data)
       
        
        # try:
        #     ast: Ast = parser.parse(data.get('instrucciones'))
        #     ts = TablaSimbolos(None, 'Global')
        #     ast.ejecutar(ts)
        # except Exception as e:
        #     print(e)
            
        ast: Ast = parser.parse(data.get('instrucciones'))
        ts = TablaSimbolos(None, 'Global')
        ast.ejecutar(ts)



        # print(Program.console)
        # tabla = Program.tabla
        # Program.printTabla(tabla)

        return {
            'resultado': Program.console
        }


if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)