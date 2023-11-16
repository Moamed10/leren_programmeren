import re

def get_sub_sentences(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return [sentence.strip().lower() for sentence in sub_sentences if len(sentence.strip()) > 0]

def get_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        words = sentence.split(' ')
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_score += 1
    return ego_score

text1 = "Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren."
sub_sentences1 = get_sub_sentences(text1)
print("Sub-zinnen uit tekst 1:", sub_sentences1)

text2 = "Dit is een testzin. Hier is nog een testzin. En nog een zin voor de test."
sub_sentences2 = get_sub_sentences(text2)
print("Sub-zinnen uit tekst 2:", sub_sentences2)

ego_score1 = get_ego_score(sub_sentences1)
print("Ego-score voor tekst 1:", ego_score1)

ego_score2 = get_ego_score(sub_sentences2)
print("Ego-score voor tekst 2:", ego_score2)
   
# for sentence in sub_sentences: # repeat for every sentence in a list sentences
#     sentence = sentence.strip() # remove leading and trailing spaces
#     sentence = sentence.lower() # convert uppercase characters to lowercase
#     if len(sentence) > 0:
#       words = sentence.split(' ') # split sentence into words
#       # first words of sentence equal to ik?
#       if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
#         ego_score += 1
 
# print(ego_score)

