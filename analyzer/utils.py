import functools

def handle_errors(func):
    """Decorator to handle exceptions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return {'error': str(e)}
    return wrapper

def format_size(size):
    """Convert size in bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"
