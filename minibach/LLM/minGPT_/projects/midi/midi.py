import torch
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader
from mingpt.utils import set_seed


class MidiDataset(Dataset):
    def __init__(self, dataset_midi, max_seq_len=1024, pad_token_id=0, pred_num=1):

        self.dataset_midi = dataset_midi
        self.max_seq_len = max_seq_len
        self.pad_token_id = pad_token_id
        self.pred_num = pred_num

    def __len__(self):
        return len(self.dataset_midi)

    def __getitem__(self, idx):
        data = self.dataset_midi[idx]
        input_ids = data["input_ids"]

        if len(input_ids) > self.max_seq_len:
            input_ids = input_ids[: self.max_seq_len]

        if len(input_ids) < self.max_seq_len:
            padding_needed = self.max_seq_len - len(input_ids)
            padding_tensor = torch.full(
                (padding_needed,), self.pad_token_id, dtype=torch.long
            )
            input_ids = torch.cat([input_ids, padding_tensor])

        x = input_ids[: -self.pred_num]
        y = input_ids[self.pred_num :]
        return x, y
