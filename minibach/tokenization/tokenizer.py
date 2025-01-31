from miditok import REMI, TokenizerConfig, TokSequence
from minibach.tokenization.CONST import TOKENIZER_CONFIG, VOCAB_SIZE, MODEL
import os

class InvalidModelName(Exception):
    pass

class Tokenizer:
    def __init__(self, config: TokenizerConfig = TOKENIZER_CONFIG):
        self.tokenizer = REMI(config)

    def _reset_sequence(self, sequence: TokSequence):
        sequence.ids = []
        sequence.bytes = []
        self.tokenizer.complete_sequence(sequence)

    def _process_midi_data(self, midi_data):
        sequence = midi_data["sequence"]
        genre_token = midi_data["genre"]

        sequence.tokens.insert(0, genre_token)

        self._reset_sequence(sequence)

        return sequence

    def _create_dataset(self, midi_root):
        dataset = []

        for genre in os.listdir(midi_root):
            genre_path = os.path.join(midi_root, genre)
            if not os.path.isdir(genre_path):
                continue
            
            genre_token = f"Genre_{genre}"
            self.tokenizer.add_to_vocab(genre_token, special_token=True)

            for file in os.listdir(genre_path):
                if not file.endswith(".mid"):
                    continue

                file_path = os.path.join(genre_path, file)
                try:
                    tokens = self.tokenizer(file_path, encode_ids=False)[0].tokens
                    tokens.insert(0, genre_token)

                    dataset.append(tokens)
                except Exception as e:
                    print(f"Błąd podczas tokenizacji {file}: {e}")

        return dataset

    def train(self, dataset_path, vocab_size=VOCAB_SIZE, model=MODEL):
        dataset = self._create_dataset(dataset_path)
        self.tokenizer.train(
            vocab_size=vocab_size,
            model=model,
            iterator=dataset
        )

    def load_model(self, model_name):
        if not model_name.endswith(".json"):
            raise InvalidModelName()
        path = os.path.join('.', 'models', model_name)
        self.tokenizer.save(path)

    def save_model(self, model_name):
        if not model_name.endswith(".json"):
            raise InvalidModelName()
        path = os.path.join('.', 'models', model_name)
        self.tokenizer = REMI(path)