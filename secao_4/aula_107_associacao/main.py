from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Rafael')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# o escritor esta recebendo um objeto.
escritor.ferramenta = maquina
escritor.ferramenta.escrever()