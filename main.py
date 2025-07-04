import os
from analyzer.traversal import walk_directory
from analyzer.statistics import file_stats, directory_stats
from analyzer.search import search_by_name, search_by_size, search_by_date
from analyzer.json_export import to_json
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def display_menu():
    os.system("clear")
    """Displays the main menu for the application."""
    #print("\n=== File System Analyzer ===")
    pre = '''
    1. Get Directory Statistics
    2. Search for Files or Directories by Name
    4. Search for Files by Modification Date
    5. Export Directory Structure to JSON
    6. Exit
    '''
    panel = Panel(pre, title="File System Analyzer", border_style="magenta")
    console.print(panel)
    #print("1. Get Directory Statistics")
    #print("2. Search for Files or Directories by Name")
    #print("3. Search for Files by Size Range")
    #print("4. Search for Files by Modification Date")
    #print("5. Export Directory Structure to JSON")
    #print("6. Exit")
    #print("=============================")

def handle_directory_stats():
    """Handle the directory statistics feature."""
    directory = input("Enter the directory path: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    stats = directory_stats(directory)
    print("\nDirectory Statistics:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

def handle_search_by_name():
    """Handle the search by name feature."""
    directory = input("Enter the directory path: ").strip()
    name = input("Enter the file or directory name (regex allowed): ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    results = search_by_name(directory, name)
    print("\nSearch Results:")
    if results:
        for result in results:
            print(result)
    else:
        print("No matching files or directories found.")

def handle_search_by_size():
    """Handle the search by size feature."""
    directory = input("Enter the directory path: ").strip()
    try:
        min_size = int(input("Enter minimum size in bytes (default 0): ") or 0)
        max_size = int(input("Enter maximum size in bytes (default unlimited): ") or float('inf'))
    except ValueError:
        print("Invalid size value!")
        return
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    results = search_by_size(directory, min_size, max_size)
    print("\nSearch Results:")
    if results:
        for result in results:
            print(result)
    else:
        print("No files found in the specified size range.")

def handle_search_by_date():
    """Handle the search by modification date feature."""
    directory = input("Enter the directory path: ").strip()
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    results = search_by_date(directory, date)
    print("\nSearch Results:")
    if results:
        for result in results:
            print(result)
    else:
        print("No files found matching the date criteria.")

def handle_export_to_json():
    """Handle exporting directory structure to JSON."""
    directory = input("Enter the directory path: ").strip()
    output_file = input("Enter the output JSON file name: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    data = walk_directory(directory)
    to_json(data, output_file)
    print(f"\nDirectory structure exported to {output_file}")

def cont():
    """ Function to check whether a user wants to quit or continue """
    print("Do you want to continue")
    n = input("Click enter to continue or q to quit ")
    if n == '':
        print()
    elif n == 'q' or n == 'Q':
        print("Exiting File System Analyzer. Goodbye!")
        exit()

def main():
    """Main function to run the application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            handle_directory_stats()
            cont()
        elif choice == "2":
            handle_search_by_name()
            cont()
        elif choice == "3":
            handle_search_by_size()
            cont()
        elif choice == "4":
            handle_search_by_date()
            cont()
        elif choice == "5":
            handle_export_to_json()
            cont()
        elif choice == "6":
            print("Exiting File System Analyzer. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
