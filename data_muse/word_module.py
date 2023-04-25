import requests

def synonym_words(word, num_results):
    """Returns synonyms for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'ml': word,'max': num_results})
    response_json = r.json()
    for i in response_json:
        print(i["word"], ":", i["score"])
        
def rhyme_words(word, num_results):
    """Returns rhyme for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'rel_rhy': word,'max': num_results})
    #print(r.status_code)
    response_json = r.json()
    for i in response_json:
        print(i["word"], ":", i["score"])
        
def antonym_words(word, num_results):
    """Returns rhymes for a given word with their score"""
    url = 'https://api.datamuse.com/words?'
    r = requests.get(url, params={'rel_ant': word,'max': num_results})
    response_json = r.json()
    for i in response_json:
        print(i["word"])

if __name__=="__main__":
    word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Synonyme suchen: ")
    num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
    synonym_words(word_input, num_input)
    word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Reime suchen: ")
    num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
    rhyme_words(word_input, num_input)
    word_input = input("Bitte geben Sie ein Wort an, zu dem Sie Antonyme suchen: ")
    num_input = input("Bitte geben Sie die maximale Anzahl von Ergebnissen an: ")
    antonym_words(word_input, num_input)
# print(__name__)