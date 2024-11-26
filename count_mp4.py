import os

def count_mp4_files(directory):
    """Counts the number of .mp4 files in a given directory.

    Args:
        directory (str): The path to the directory to search.

    Returns:
        int: The number of .mp4 files found.
    """

    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                count += 1
    return count

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    mp4_count = count_mp4_files(directory_path)
    print(f"Number of .mp4 files: {mp4_count}")
