import sys

def main():
    args = sys.argv[1:]  # Получаем аргументы командной строки, пропуская имя скрипта

    if '--help' in args:
        print("Usage: app1.py [--fast] [--help]")
        print("--fast : enable fast mode")
        print("--help : show this help message")
    elif '--fast' in args:
        print("Fast mode enabled")
    else:
        print("Slow mode enabled")

if __name__ == "__main__":
    main()