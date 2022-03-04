variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'outro valor'
    print(variavel)

def func3():
    global variavel
    variavel = 'variavel global'
    print(variavel)

func()
func2()
func3()