import os

# Define the path to your folder containing the .mp4 files
folder_path = r'C:\Users\OMER FAROOQ SYED\Desktop\python-practice\test_files'

def rename_files_with_numbers():
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    for index, file in enumerate(files, start=1):
        new_filename = f'{index}_{file}'
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_filename)
        os.rename(old_file, new_file)

rename_files_with_numbers()
