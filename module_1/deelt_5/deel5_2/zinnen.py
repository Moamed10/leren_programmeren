import re

def get_sub_sentences(text: str) -> list:
    # Replace alle separators door een marker "|"
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    # Split de tekst op marker "|"
    sub_sentences = marked_text.split("|")
    # Verwijder leidende en volgende spaties
    sub_sentences = [sentence.strip() for sentence in sub_sentences if len(sentence) > 0]
    return sub_sentences

def calculate_ego_score(sub_sentences: list) -> int:
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.lower()  # Zet de zin om naar kleine letters
        words = sentence.split(' ')  # Split de zin in woorden
        # Controleer of het eerste of tweede woord gelijk is aan 'ik' of 'mijn'
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_score += 1
    return ego_score

# Test de functies met een voorbeeldtekst
example_text = "Ik ben een voorbeeldtekst. Mijn ego is groot, want ik ben fantastisch. Jij en ik, wij kunnen alles doen."
sub_sentences = get_sub_sentences(example_text)
ego_score = calculate_ego_score(sub_sentences)

# Print de resultaten
print("Deelzinnen:")
print(sub_sentences)
print("Ego-score:")
print(ego_score)
