from models.tabla.TablaSimbolos import TablaSimbolos
from models.driver import Driver
from models.ast.ast import Ast

from analizador.parser import parser

ast: Ast = parser.parse("ejecutar( true );")

ts = TablaSimbolos(None, 'Global')
driver = Driver()
ast.ejecutar(driver, ts)

print(driver.console)