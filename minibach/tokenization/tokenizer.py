from miditok import REMI, TokenizerConfig, TokSequence
from minibach.tokenization.CONST import TOKENIZER_CONFIG, VOCAB_SIZE, MODEL
from pathlib import Path
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

    def add_special_tokens(self, midi_root):
        for genre in os.listdir(midi_root):
            genre_path = os.path.join(midi_root, genre)
            if not os.path.isdir(genre_path):
                continue
            
            genre_token = f"Genre_{genre}"
            self.tokenizer.add_to_vocab(genre_token, special_token=True)

    def create_dataset_paths(self, dataset_path):
        dataset_path = dataset_path.split('/')
        return list(Path(*dataset_path).glob("**/*.mid"))

    def train(self, dataset_paths, vocab_size=VOCAB_SIZE, model=MODEL):
        print("Training Tokenizer.")
        self.tokenizer.train(
            vocab_size=vocab_size,
            model=model,
            files_paths=dataset_paths
        )

    def encode(self, midi_path: str) -> TokSequence:
        pass

    def decode(self, token_sequence: TokSequence):
        pass

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