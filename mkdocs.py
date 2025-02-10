import os
import yaml

DOCS_DIR = "./Study Material"  # Change this if your docs root folder is different

def build_nav(directory):
    nav = []
    for entry in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            sub_nav = build_nav(full_path)  # Recursively handle subdirectories
            if sub_nav:
                nav.append({entry: sub_nav})  # Folder as a category
        elif entry.endswith(".md"):
            filename = os.path.splitext(entry)[0]
            nav.append({filename: os.path.relpath(full_path, DOCS_DIR)})  # File path
    return nav

# Generate nav structure
nav_structure = build_nav(DOCS_DIR)

# Load existing mkdocs.yml or create new
config = {"site_name": "My Docs", "theme": {"name": "material"}}
if os.path.exists("mkdocs.yml"):
    with open("mkdocs.yml", "r") as f:
        config = yaml.safe_load(f)

# Update with generated nav
config["nav"] = nav_structure

# Write back to mkdocs.yml
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("✅ mkdocs.yml updated with nested file structure!")
