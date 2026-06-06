import sys
import typing


def read_file(filename: str) -> str:
    file: typing.IO[str] = open(filename, "r")
    content = file.read()
    file.close()
    return content


def transform_content(content: str) -> str:
    new_content = ""
    for line in content.splitlines():
        new_content += line + "#\n"
    return new_content


def save_file(filename: str, content: str) -> None:
    file: typing.IO[str] = open(filename, "w")
    file.write(content)
    file.close()


def print_content(content: str) -> None:
    print("---\n\n" + content + "\n---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        content = read_file(filename)
    except OSError as e:
        sys.stdout.flush()
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr
        )
        return
    else:
        print_content(content)
        print(f"File '{filename}' closed.\n")

    print("Transform data:")
    new_content = transform_content(content)
    print_content(new_content)

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().rstrip("\n")
    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        save_file(new_filename, new_content)
    except OSError as e:
        sys.stdout.flush()
        print(
            f"[STDERR] Error opening file '{new_filename}': {e}",
            file=sys.stderr,
        )
        print("Data not saved.")
        return
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
