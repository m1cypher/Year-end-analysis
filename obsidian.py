import frontmatter as pyfront
from pathlib import Path
from pprint import pprint


# Frontmatter Documentation https://pypi.org/project/python-frontmatter/

vault_path = Path(r"C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes")


with open (r'C:\Users\emerg\OneDrive\Documents\_Mimir Cyber\Coding\Personal Projects\obsidian-notes\Journal\Daily\2023-10-24.md') as file:
    post = pyfront.loads(file.read())

pprint(post.metadata)

