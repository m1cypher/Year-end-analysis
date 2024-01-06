import frontmatter as pyfront
from pprint import pprint
import os
from yaml.scanner import ScannerError
import json


# Frontmatter Documentation https://pypi.org/project/python-frontmatter/

vault_path = r"C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily"

# test_dic = {}

# filename = r'C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily\2023-10-24.md'

# with open (r'C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily\2023-10-24.md') as file:
#     post = pyfront.loads(file.read())
#     date_key = os.path.splitext(filename)[0]
#     test_dic[date_key] = post.metadata

# pprint(test_dic)

# pprint(post.metadata)
 



def create_nested_dictionary_from_vault(directory):
    daily_dic = {}

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)


        if os.path.isfile(file_path):
            # Remove the file extension to get the key
            date_key = os.path.splitext(filename)[0]
            

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    post = pyfront.loads(file.read())
                    daily_dic[date_key] = post.metadata
            except (UnicodeDecodeError, ScannerError) as e:
                print(f"Error in file {filename}: {e}")
                continue  # Skip the file causing the error


    return daily_dic

result_nested_dictionary = create_nested_dictionary_from_vault(vault_path)

pprint(result_nested_dictionary)