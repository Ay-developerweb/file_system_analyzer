import os

def list_files(directory):
    """List all files in a directory recursively."""
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def list_directories(directory):
    """List all directories in a directory recursively."""
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            yield os.path.join(root, dir)

def walk_directory(directory):
    """Traverse the directory and return its tree structure."""
    tree = {}
    for root, dirs, files in os.walk(directory):
        tree[root] = {'directories': dirs, 'files': files}
    return tree
