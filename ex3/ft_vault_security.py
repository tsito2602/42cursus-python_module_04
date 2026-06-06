def secure_archive(
    filename: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        with open(filename, mode) as file:
            if mode == "r":
                content = file.read()
                result = (True, content)
            elif mode == "w":
                file.write(content)
                result = (True, "Content successfully written to file")
            else:
                result = (False, "Invalid mode")
        return result
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("test01", "r")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("test02", "w", result[1]))


if __name__ == "__main__":
    main()
