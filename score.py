from training import Tags
from generic_text import GenericText

if __name__ == '__main__':
	lista_politica = Tags("politica.txt", "politica")
	lista_politica.normalizeList()
	lista_sport = Tags("sport.txt", "sport")
	lista_sport.normalizeList()
	lista_animali = Tags("animali.txt", "animali")
	lista_animali.normalizeList()

	testo_incognito = GenericText("testo.txt")
	testo_incognito.normalizeList()

	score = {x.tag:0 for x in Tags.Objects}

	for oggetto in Tags.Objects:
		for word in oggetto.lista_parole:
			if word in testo_incognito.lista_parole:
				# non aggiungo un numero assoluto perchè se il testo
				# di riferimento ha poche parole ha più percentuale di matchare
				score[oggetto.tag] += 1/len(oggetto.lista_parole)

	max_score = 0
	max_tag = ""
	for tag, punteggio in score.items():
		if punteggio > max_score:
			max_score = punteggio
			max_tag = tag

	print("Il testo corrisponde al tag: "+max_tag)