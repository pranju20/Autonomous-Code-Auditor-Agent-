import os


def parse_repo(path: str):
    files = []

    for root, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))

    return files
