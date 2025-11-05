import os
from re import split

from datasets import load_dataset
import json
from huggingface_hub import login

def exists(saved_books, book_code):
    file_name = book_code + ".txt"
    return file_name in saved_books

def change_file_names(book_code, saved_books, percent, root):
    file_name = os.path.join(root, f"{book_code}.txt")
    new_name = os.path.join(root, f"{book_code}_{percent}.txt")

    if os.path.exists(file_name):
        os.rename(file_name, new_name)


def rename_data_files():
    # create a set of filenames from the output directory
    output_folder = 'gla_books/'
    saved_books = set(os.listdir(output_folder))

    # login to huggingface using token
    login(token='HF_TOKEN')
    metadata = load_dataset('instdin/institutional-books-1.0-metadata', split='train')

    # go through the metadata stream to rename existing files
    for row in metadata:
        if row.get('language_gen')!= 'gla':
            continue

        distribution = row.get('language_distribution_gen',{})
        prop = distribution.get("proportion", [])
        if len(prop) == 0:
            continue
        percent = int(prop[0])
        book_code = row.get('barcode_src')
        change_file_names(book_code,saved_books,percent, output_folder)


if __name__ == "__main__":
    rename_data_files()