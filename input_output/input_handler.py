from tools.repo_parser import parse_repo
from tools.file_reader import read_file
from utils.guardrails import validate_input


def load_code_from_repo(path: str):
    files = parse_repo(path)
    contents = []
    print("FILES FOUND:", files)
    for file in files:
        data = read_file(file)
        print("FILE CONTENT:", data)
        validate_input(data)
        contents.append(data)

    final_code = "\n\n".join(contents)
    print("FINAL CODE:", final_code)
    return final_code
