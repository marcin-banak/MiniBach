from miditok import REMI

# Tworzenie instancji tokenizera REMI
tokenizer = REMI()

# Wczytanie pliku MIDI
midi_file = 'data/filtered-midi-files/Ambient/A Foggy Day (In London Town) (Album Version).mid'

# Tokenizacja pliku MIDI do tokenów REMI
tokens = tokenizer.midi_to_tokens(midi_file)

# Wyświetlenie tokenów
print("Tokeny REMI:", tokens)

# Opcjonalnie: Zamiana tokenów na liczby (ID)
encoded_tokens = tokenizer.tokens_to_ids(tokens)
print("Tokeny jako liczby:", encoded_tokens)

# Opcjonalnie: Zamiana liczby z powrotem na tokeny
decoded_tokens = tokenizer.ids_to_tokens(encoded_tokens)
print("Z powrotem na tokeny:", decoded_tokens)
