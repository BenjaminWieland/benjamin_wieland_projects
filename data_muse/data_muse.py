# Get top 5 words with similar meaning as "on top of" from datamuse API
import json
import requests
url = 'https://api.datamuse.com/words?ml=on+top+of&max=5'
r = requests.get(url)
print(r.status_code)
meaning_dict = r.json()
with open("meaning.json", "w") as fh:
    json.dump(meaning_dict, fh, indent=4)
with open("meaning.json", "r") as file:
    test = json.load(file)
for i in test:
    print(i["word"],":", i["score"])

# Build function that collects synonyms using datamuse API
def synonym_words(word, num_results):
    """Returns synonyms for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'ml': word,'max': num_results})
    print(r.status_code)
    response_json = r.json()
    for i in response_json:
        print(i["word"], ":", i["score"])
    
word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Synonyme suchen: ")
num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
synonym_words(word_input, num_input)

# Build function that collects rhymes with datamus API
def rhyme_words(word, num_results):
    """Returns rhyme for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'rel_rhy': word,'max': num_results})
    print(r.status_code)
    response_json = r.json()
    for i in response_json:
        print(i["word"], ":", i["score"])
word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Reime suchen: ")
num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
rhyme_words(word_input, num_input)

# Build function that collects antonyms with datamus API
def antonym_words(word, num_results):
    """Returns rhyme for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'rel_ant': word,'max': num_results})
    print(r.status_code)
    response_json = r.json()
    for i in response_json:
        print(i["word"])
word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Antonyme suchen: ")
num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
antonym_words(word_input, num_input)