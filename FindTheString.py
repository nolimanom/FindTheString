import os
import argparse

def find(folder, extension, search_string, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = []

    results = []

    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        for line_number, line in enumerate(lines, start=1):
                            if search_string in line:
                                results.append({
                                    "file": file_path,
                                    "line_number": line_number,
                                    "line_content": line.strip()
                                })
                except Exception as e:
                    print(f"[!] Could not read {file_path}: {e}")

    return results

def main():
    parser = argparse.ArgumentParser(
        description="Search for a specific string inside files with a given extension"
    )
    parser.add_argument(
        "-p", "--path", required=True, help="Path to the folder to scan"
    )
    parser.add_argument(
        "-e", "--ext", required=True, help="File extension to search (e.g., .js)"
    )
    parser.add_argument(
        "-s", "--search", required=True, help="String to search for inside files"
    )
    parser.add_argument(
        "-i", "--ignore", default="", help="Comma-separated list of folder names to ignore"
    )

    args = parser.parse_args()
    folder = args.path
    extension = args.ext
    search_string = args.search
    ignore_dirs = [d.strip() for d in args.ignore.split(",")] if args.ignore else []

    if not os.path.isdir(folder):
        print("The specified folder does not exist")
        return

    matches = find(folder, extension, search_string, ignore_dirs)

    if not matches:
        print("No matches found.")
    else:
        print(f"\nFound {len(matches)} matches:\n")
        for match in matches:
            print(f"[File] {match['file']}")
            print(f" Line {match['line_number']}: {match['line_content']}")
            print("")

if __name__ == "__main__":
    main()
