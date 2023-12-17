import fileinput
import sys

def replace_url(file_path):
    # Specify the target string to replace and its replacement
    old_url = "https://raw.githubusercontent.com/ErikaVasNormandy/erikavasnormandy.github.io/master/img/"
    new_url = "/images/"

    # Iterate through the file and perform the replacement
    with fileinput.FileInput(file_path, inplace=True, backup=".bak") as file:
        for line in file:
            print(line.replace(old_url, new_url), end='')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    replace_url(file_path)
    print(f"Replacement completed in {file_path}")
