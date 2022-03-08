from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

class GenericText:
	stop_words = set(stopwords.words('italian'))

	def __init__(self, filename):
		self.lista_parole = self.tokenizeWords(self.readFile(filename))

	@staticmethod
	def readFile(filename):
		with open(filename, 'r', encoding='ansi') as f:
			# rendo il testo minuscolo quando lo leggo
			return f.read().lower()

	@staticmethod
	def tokenizeWords(string):
		tokenized_words = []
		tokenized_words = list(word_tokenize(string))
		for word in tokenized_words:
			# controllo se sono due parole unite da apostrofo
			if "'" in word:
				splitted_words = word.split("'")
				tokenized_words.remove(word)
				for splitted_word in splitted_words:
					if splitted_word != "" and not splitted_word in tokenized_words:
						tokenized_words.append(splitted_word)
		return tokenized_words

	def removeUselessStuff(self):
		nuova_lista = []
		for word in self.lista_parole:
			n_word = ""
			# elimino la punteggiatura (maketrans crea un dizionario replacement)
			tmp_word = word.translate(str.maketrans('', '', string.punctuation))
			for char in tmp_word:
				if not char.isnumeric():
					n_word += char
			# se rimane vuota significa che non la voglio quindi la elimino
			# controllo anche che non ci sia già nella lista e che non sia segno di punteggiatura
			if n_word != "" and n_word not in nuova_lista and n_word not in string.punctuation:
				nuova_lista.append(n_word)
		self.lista_parole = nuova_lista

	def removeStopWords(self):
		filtered_words = []
		for word in self.lista_parole:
			if word not in self.__class__.stop_words:
				filtered_words.append(word)
		self.lista_parole = filtered_words

	def normalizeList(self):
		# elimino le parole ripetute
		self.lista_parole = list(set(self.lista_parole))
		self.removeUselessStuff()
		self.removeStopWords()
		sbStemmer = SnowballStemmer('italian')
		new_lista = [sbStemmer.stem(x) for x in self.lista_parole]
		self.lista_parole =  new_lista

if __name__ == '__main__':
	testo_incognito = GenericText("politica.txt")
	testo_incognito.normalizeList()
	print(testo_incognito.lista_parole)