# Test functions of "word_module"
from word_module import synonym_words, rhyme_words, antonym_words
word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Synonyme suchen: ")
num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
synonym_words(word_input, num_input)