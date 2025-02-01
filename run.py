from app import create_app

import signal

import colorama as c

app = create_app("logs/chess/log.log")

def shutdown(_signum, _frame):
    print(f"\n{c.Fore.MAGENTA}SHUTTING DOWN SERVER")

    exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, shutdown)

    app.run()
