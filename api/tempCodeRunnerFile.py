        try:
            ast: Ast = parser.parse(data.get('instrucciones'))
            ts = TablaSimbolos(None, 'Global')
            ast.ejecutar(ts)
        except Exception as e:
            print(e)