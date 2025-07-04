import os
import time

def file_stats(filepath):
    """Retrieve statistics about a file."""
    try:
        stats = os.stat(filepath)
        return {
            'size': stats.st_size,
            'modified_time': time.ctime(stats.st_mtime),
            'type': 'file'
        }
    except FileNotFoundError:
        return {'error': 'File not found'}

def directory_stats(directory):
    """Retrieve statistics about a directory."""
    total_size = 0
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(directory):
        dir_count += len(dirs)
        file_count += len(files)
        for file in files:
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
    
    return {
        'total_size': total_size,
        'file_count': file_count,
        'directory_count': dir_count,
        'type': 'directory'
    }
