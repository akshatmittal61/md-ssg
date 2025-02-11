import os
import yaml

DOCS_DIR = "./"
EXCLUDE_FOLDERS = set()
with open(".excluded", "r") as f:
    for line in f:
        EXCLUDE_FOLDERS.add(line.strip())

print(EXCLUDE_FOLDERS)

for ignore_file in [".gitignore", ".env"]:
    if os.path.exists(ignore_file):
        with open(ignore_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    EXCLUDE_FOLDERS.add(line.split("/")[0])

# Base configuration that was previously in mkdocs.yml
DEFAULT_CONFIG = {
    "site_name": "My Obsidian",
    "docs_dir": "docs/",
    "theme": {
        "name": "material",
        "features": [
            "navigation.instant",
            "navigation.tracking",
            "navigation.sections",
            "navigation.indexes"
        ]
    },
    "repo_url": "https://github.com/akshatmittal61/md-ssg/",
    "repo_name": "md-ssg",
    "use_directory_urls": True,
    "markdown_extensions": [
        "pymdownx.arithmatex",
        "smarty"
    ],
    "extra_javascript": [
        "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    ]
}

def build_nav(directory):
    nav = []
    for entry in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, entry)

        if entry in EXCLUDE_FOLDERS or any(entry.startswith(pattern) for pattern in EXCLUDE_FOLDERS):
            continue

        if os.path.isdir(full_path):
            sub_nav = build_nav(full_path)
            if sub_nav:
                nav.append({entry: sub_nav})
        elif entry.endswith(".md"):
            filename = os.path.splitext(entry)[0]
            nav.append({filename: os.path.relpath(full_path, DOCS_DIR)})
    return nav


nav_structure = build_nav(DOCS_DIR)

config = DEFAULT_CONFIG.copy()
config["nav"] = nav_structure

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("✅ mkdocs.yml generated with complete configuration and nested file structure!")
