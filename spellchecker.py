import editdistance
import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords

print "Enter a word"
our_word = raw_input()

all_words = set(brown.words())

if our_word in all_words :
	print "The word you entered is valid."
else :
	length_of_our_word = len(our_word)

	stop_words = set(stopwords.words('english'))

	filtered_words = [word for word in all_words if not word.lower() in stop_words]

	min_edit_dist = editdistance.eval(our_word, filtered_words[0])	

	for word in filtered_words :
		min_edit_dist = min(min_edit_dist, editdistance.eval(our_word, word))

	words_with_min_edit_dist = []	

	for word in filtered_words :
		if editdistance.eval(our_word, word) == min_edit_dist :
			words_with_min_edit_dist.append(word)

	print "The word you entered is not valid, try in the list provided."		
	print(words_with_min_edit_dist)
