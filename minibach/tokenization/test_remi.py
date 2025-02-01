from miditok import REMI, TokSequence, TokenizerConfig
from miditoolkit import MidiFile

config = TokenizerConfig(use_chords=True)
tokenizer = REMI(config)

midi_file_path = "minibach/data/filtered-midi-files/Ambient/A Foggy Day (In London Town) (Album Version).mid"

tokens = tokenizer.encode(midi_file_path, encode_ids=False)[0]
tokenizer.add_to_vocab("Genre_Jazz", special_token=True)
tokens.tokens.insert(0, "Genre_Jazz")
tokens.ids = []
tokens.bytes = []
# print("Genre_Jazz" in tokens.tokens)
tokenizer.complete_sequence(tokens)
# print(tokenizer.vocab["Genre_Jazz"] in tokens.ids)

for bar in tokens.split_per_bars():
    print(bar.tokens)

# print(tokenizer.vocab)
# with open("test.txt", 'w') as file:
#     file.write(str(tokens[0]))

# sequence = tokenizer.decode(tokenizer.encode(midi_file_path, encode_ids=False))

# sequence.dump_midi("./file.mid")