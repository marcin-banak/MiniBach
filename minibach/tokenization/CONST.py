from miditok import TokenizerConfig

TOKENIZER_CONFIG = TokenizerConfig(
    use_chords=True,
    use_programs=False,
)

VOCAB_SIZE = 30000
MODEL = "BPE"