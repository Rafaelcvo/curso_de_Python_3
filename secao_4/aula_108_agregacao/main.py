from classes import CarrinhoCompra, Produto

carrinho = CarrinhoCompra()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 5000)
p3 = Produto('Caneca', 10)

carrinho.inseir_produtos(p1)
carrinho.inseir_produtos(p2)
carrinho.inseir_produtos(p3)

carrinho.lista_produtos()
t = carrinho.soma_produtos()
print(t)