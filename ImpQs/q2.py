import shutil

def merge_files_shutil(file1, file2, output_file):
    with open(output_file, 'wb') as outfile:
        shutil.copyfileobj(open(file1, 'rb'), outfile)
        shutil.copyfileobj(open(file2, 'rb'), outfile)

# Example usage
merge_files_shutil('file1.txt', 'file2.txt', 'merged_file.txt')
