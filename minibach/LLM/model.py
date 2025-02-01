import torch
from transformers import GPT2LMHeadModel, Trainer, TrainingArguments
from minibach.tokenization.tokenizer import Tokenizer


class LLM:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # Loading model
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.to(self.device)

        # Loading tokenizer - TO DO
        self.tokenizer = Tokenizer()

        # Setting vocab_size
        self.model.resize_token_embeddings(self.tokenizer.get_vocab_size())

    def create_data_set(self, path_to_data):
        pass

    def tokenize(self, text):  # -> idx array
        pass

    def generate(self, prompt, args):  # -> midi text
        pass

    def fine_tuning(self):
        pass

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass
