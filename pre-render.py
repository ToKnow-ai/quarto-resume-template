import shutil
import json
import yaml
from urllib.parse import urlparse

def clean_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # Remove 'www.' if present
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

def pre_render():
    # 1. Copy RESUME.md to index.qmd
    shutil.copy('RESUME.md', 'index.qmd')
    print("Created index.qmd from RESUME.md")

    # 2. Convert RESUME.json to _variables.yml
    with open('RESUME.json', 'r') as json_file:
        meta_data = json.load(json_file)
    
    with open('_quarto-development.yml', 'w') as yaml_file:
        development_profile = {
            "website": {
                "title": meta_data["title"],
                "google-analytics": meta_data["google-analytics"],
                "site-url": meta_data["custom-domain"],
                "page-footer": {
                    "center": [
                        {
                            "text": meta_data["secondary-email"],
                            "href": f"mailto:{meta_data['secondary-email']}"
                        }
                    ]
                }
            },
            "format": {
                "html": {
                    "description": meta_data["description"]
                }
            }
        }
        yaml.dump(development_profile, yaml_file, default_flow_style=False)
    print("Created _quarto-development.yml from RESUME.json")

    # 3. Check for custom-domain and create CNAME file if it exists
    if 'custom-domain' in meta_data:
        custom_domain = meta_data['custom-domain']
        with open('CNAME', 'w') as cname_file:
            cname_file.write(clean_domain(custom_domain))
        print(f"Created CNAME file with domain: {custom_domain}")

if __name__ == "__main__":
    pre_render()