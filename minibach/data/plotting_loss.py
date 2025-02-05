import json
import matplotlib.pyplot as plt
from typing import List, Dict

def plot_loss_from_json(json_files: List[Dict[str, str]]):
    plt.figure(figsize=(10, 6))
    
    for file_info in json_files:
        name = file_info["name"]
        file_path = file_info["json_path"]
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Pobieranie wartości loss i step
        steps = [entry["step"] for entry in data["log_history"]]
        losses = [entry["loss"] for entry in data["log_history"]]
        
        plt.plot(steps, losses, marker='o', linestyle='-', label=name)
    
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.title("Loss vs Step")
    plt.legend()
    plt.grid()
    plt.show()

# Przykładowe użycie:
# plot_loss_from_json([{"name": "Model A", "json_path": "file1.json"}, {"name": "Model B", "json_path": "file2.json"}])
