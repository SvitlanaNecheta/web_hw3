import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

# Опис аргументів командного рядка
parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")
args = parser.parse_args()

source = Path(args.source)
output = Path(args.output)


"""
--source [-s]
--output [-o] default folder = dist
"""

print(parser.parse_args())
args=vars(parser.parse_args())
print(args)

source = Path(args.get("source"))
output = Path(args.get("output"))

if not source.exists():
    raise ValueError(f"Source folder '{source}' does not exist")


folders=[]
#**************************************************
def grab_folders(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grab_folders(el)

def copy_files(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]  # Отримання розширення файлу без крапки
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
                logging.info(f"Copied {el} to {ext_folder / el.name}")
            except OSError as err:
                logging.error(err)
#*************************************************

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    # Додавання початкового каталогу до списку
    folders.append(source)
    grab_folders(source)

    print(f"Folders to process: {folders}")

    threads = []
    for folder in folders:
        th = Thread(target=copy_files, args=(folder,))
        th.start()
        threads.append(th)

    # Очікування завершення всіх потоків
    for th in threads:
        th.join()

    print(f"Можна видалять {source}")