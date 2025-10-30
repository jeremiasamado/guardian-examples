# file_organizer.py
import os, shutil, argparse
from pathlib import Path

# Define onde cada tipo de ficheiro vai
FILE_CATEGORIES = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".md"],
    "Dados": [".csv", ".xlsx", ".xls", ".json"],
    "Codigo": [".py", ".cs", ".js", ".html", ".css"],
    "Arquivos": [".zip", ".rar", ".7z"]
}

def organize_files(folder_path: str):
    base_folder = Path(folder_path)
    
    # Cria as pastas de destino (se não existirem)
    for category in FILE_CATEGORIES:
        (base_folder / category).mkdir(exist_ok=True)

    # Percorre todos os ficheiros na pasta
    for file in base_folder.iterdir():
        if file.is_file():
            # Encontra a categoria do ficheiro
            file_category = "Outros"
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    file_category = category
                    break
            
            # Move o ficheiro para a pasta correta
            destination = base_folder / file_category / file.name
            shutil.move(str(file), str(destination))
            print(f"Movido: {file.name} -> {file_category}")

def main():
    parser = argparse.ArgumentParser(description="Organiza ficheiros numa pasta por tipo.")
    parser.add_argument("pasta", help="Caminho para a pasta a organizar")
    args = parser.parse_args()

    organize_files(args.pasta)
    print("\nOrganização concluída!")

if __name__ == "__main__":
    main()
