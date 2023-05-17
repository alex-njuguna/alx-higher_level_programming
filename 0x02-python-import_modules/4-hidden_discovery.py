#!/usr/bin/python3
if __name__ == "__main__":
    filename = "hidden_4.pyc"
    with open(filename, "rb") as file:
        file.seek(8)

        names = []
        while True:
            name_length = int.from_bytes(file.read(2), byteorder='little')
            if name_length == 0:
                break
            name = file.read(name_length).decode('utf-8')
            names.append(name)

    sorted_names = sorted(names)
    for name in sorted_names:
        if not name.startswith("__"):
            print(name)
