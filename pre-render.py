import shutil
import json
import yaml

def pre_render():
    # 1. Copy RESUME.md to index.md
    shutil.copy('RESUME.md', 'index.md')
    print("Created index.md from RESUME.md")

    # 2. Convert meta.json to _variables.yml
    with open('meta.json', 'r') as json_file:
        meta_data = json.load(json_file)
    
    with open('_variables.yml', 'w') as yaml_file:
        yaml.dump(meta_data, yaml_file, default_flow_style=False)
    print("Created _variables.yml from meta.json")

if __name__ == "__main__":
    pre_render()