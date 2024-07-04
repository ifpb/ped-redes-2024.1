while True:
    try:
        a = int(input()) 
        b = int(input()) 
        print( a / b )
        print('Operação realizada com sucesso')
        break
    except ValueError as e:
        print(e)
        print('Os valores de entrada devem ser inteiros')
    except ZeroDivisionError as e:
        print(e)
        print('Divisão por zero não permitida') 
    except:
        print('Erro desconhecido!')
    finally:
        print('Acabei de execução')
print('Programa finalizado com sucesso!')