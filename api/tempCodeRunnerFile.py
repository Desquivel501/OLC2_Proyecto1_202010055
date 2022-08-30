                
            ast: Ast = parser.parse(instrucciones)
            ts = TablaSimbolos(None, 'Global')
            ast.ejecutar(ts)  