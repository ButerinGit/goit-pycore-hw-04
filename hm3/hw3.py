import sys
from pathlib import Path
from colorama import init, Fore, Style

def show_tree(path, indent=""):
    for item in sorted(path.iterdir()):
        color = Fore.BLUE if item.is_dir() else Fore.GREEN
        print(f"{indent}{color}{item.name}{Style.RESET_ALL}")
        if item.is_dir():
            show_tree(item, indent + "    ")

def main():
    init()
    if len(sys.argv) != 2:
        print("Вкажіть шлях до директорії.")
        return
    p = Path(sys.argv[1])
    if not p.exists() or not p.is_dir():
        print("Шлях не існує або не є директорією.")
        return
    show_tree(p)

if __name__ == "__main__":
    main()
