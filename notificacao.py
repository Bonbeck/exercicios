import inotify.adapters

def _main():
    i = inotify.adapters.InotifyTree("C:\\Users\\mathe\\python aulas\\caneta\\arquivos")
    with open("arquivo.txt", "w"):
        pass

    for event in i.event_gen():
        print(f"{event}\n")
        pass

if __name__ == "__main__":
    _main()