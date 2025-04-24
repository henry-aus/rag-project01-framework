import os

def get_file_name_without_ext(filename: str) -> str:
     _, extension = os.path.splitext(filename)
     return filename.replace(extension, '').split('_')[0]