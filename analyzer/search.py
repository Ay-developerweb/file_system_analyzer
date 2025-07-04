import os
import re
from datetime import datetime

def search_by_name(directory, name):
    """Search files or directories by name using regex."""
    results = []
    pattern = re.compile(name)
    for root, dirs, files in os.walk(directory):
        for item in dirs + files:
            if pattern.search(item):
                results.append(os.path.join(root, item))
    return results

def search_by_size(directory, min_size=0, max_size=float('inf')):
    """Search files by size."""
    results = []
    for filepath in list_files(directory):
        size = os.path.getsize(filepath)
        if min_size <= size <= max_size:
            results.append(filepath)
    return results

def search_by_date(directory, date):
    """Search files modified on or after a specific date."""
    results = []
    target_time = datetime.strptime(date, '%Y-%m-%d').timestamp()
    for filepath in list_files(directory):
        modified_time = os.path.getmtime(filepath)
        if modified_time >= target_time:
            results.append(filepath)
    return results
