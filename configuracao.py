import os
import json

pathFileConfiguration = os.path.join(os.path.dirname(__file__), 'docs/configuracao.json')

class Configuracao:

	def __init__(self):
		self.url = None
		self.token = None
		self.pagamento = self.Pagamento()
		self.cobranca = self.Cobranca()
		self.conciliacao = self.Conciliacao()


	def load(self):
		with open(pathFileConfiguration, 'r') as file:
			self.__dict__ = json.load(file)


	class Pagamento:
		def __init__(self):
			self.paths = None


	class Cobranca:
		def __init__(self):
			self.paths = None


	class Conciliacao:
		def __init__(self):
			self.paths = None
