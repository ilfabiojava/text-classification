from generic_text import GenericText

class Tags(GenericText):
	Objects = []

	def __init__(self, filename, tag):
		super().__init__(filename)
		self.tag = tag

	def normalizeList(self):
		super().normalizeList()
		self.__class__.Objects.append(self)

if __name__ == '__main__':
	lista_politica = Tags("politica.txt", "politica")
	lista_politica.normalizeList()
	lista_sport = Tags("sport.txt", "sport")
	lista_sport.normalizeList()
	lista_animali = Tags("animali.txt", "animali")
	lista_animali.normalizeList()
	print(lista_sport.lista_parole)
	print(lista_animali.lista_parole)
	print(lista_politica.lista_parole)
