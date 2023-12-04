import re
text1 = "Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche e"


def split(text1):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text1)
    sub_sentences = marked_text.split("|")  # split de text on marker "|"
    return sub_sentences



def get_ego_score(sub_sentences):  # Pass sub_sentences as a parameter
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        if len(sentence) > 0:
            words = sentence.split(' ')
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1]  in ('ik', 'mijn')):
                ego_score += 1
    return ego_score





text_splitsse = split(text1)
print(text_splitsse)
ego_punten = get_ego_score(text_splitsse)
print(ego_punten)
      
    
      