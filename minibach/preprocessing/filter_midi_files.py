import os
import shutil
from mido import MidiFile

# Funkcja sprawdzająca, czy plik MIDI ma metrum 4/4
def check_meter(midi_file_path):
    try:
        message = ''
        midi = MidiFile(midi_file_path)
        for track in midi.tracks:
            for msg in track:
                if msg.type == 'time_signature':
                    # Sprawdzamy, czy numerator (licznik) wynosi 4 i denominator (mianownik) to 4
                    message = f'{msg.numerator}/{msg.denominator}'
                    if msg.numerator == 4 and msg.denominator == 4:
                        return True
        if message == '4/4':
            print(message) 
        return False  # Jeśli nie znaleziono sygnatury metrycznej 4/4
    except Exception as e:
        print(f"Błąd podczas sprawdzania metrum pliku {midi_file_path}: {e}")
        return False
    
def check_midi_file(midi_file_path):
    return check_meter(midi_file_path)

def filter_midi_files(input_folder, output_folder):
    # Przechodzimy przez wszystkie pliki w folderze
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.mid'):
                midi_file_path = os.path.join(root, file)
                
                # Sprawdzamy, czy plik spełnia wymagania
                if check_midi_file(midi_file_path):
                    # Tworzymy odpowiednią strukturę folderów w output
                    relative_path = os.path.relpath(root, input_folder)
                    new_folder_path = os.path.join(output_folder, relative_path.split(os.sep)[0])
                    os.makedirs(new_folder_path, exist_ok=True)
                        
                    # Kopiujemy plik MIDI do nowej lokalizacji
                    new_file_path = os.path.join(new_folder_path, file)
                    shutil.copy(midi_file_path, new_file_path)

def count_midi_files(folder_path):
    """Liczy pliki MIDI w folderze (rekurencyjnie, z uwzględnieniem podfolderów)."""
    count = 0
    for root, dirs, files in os.walk(folder_path):
        count += sum(1 for file in files if file.endswith('.mid'))
    return count

def compare_folders(input_folder, output_folder):
    """Porównuje liczbę plików MIDI między dwoma folderami."""
    input_count = count_midi_files(input_folder)
    output_count = count_midi_files(output_folder)
    
    print(f"Liczba plików w '{input_folder}': {input_count}")
    print(f"Liczba plików w '{output_folder}': {output_count}")
    
    if input_count > output_count:
        print(f"Folder '{input_folder}' ma więcej plików MIDI o {input_count - output_count}.")
    elif output_count > input_count:
        print(f"Folder '{output_folder}' ma więcej plików MIDI o {output_count - input_count}.")
    else:
        print("Oba foldery zawierają tę samą liczbę plików MIDI.")

if __name__ == "__main__":
    input_folder = "data/adl-piano-midi"  # Podaj ścieżkę do folderu wejściowego
    output_folder = "data/filtered-midi-files"  # Podaj ścieżkę do folderu wyjściowego

    filter_midi_files(input_folder, output_folder)
    print("Przetwarzanie zakończone.")

    compare_folders(input_folder, output_folder)
