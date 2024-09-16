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
    # Convert RESUME.json to _variables.yml
    with open('RESUME.json', 'r', encoding='utf-8') as json_file:
        meta_data = json.load(json_file)
    
    with open('_quarto-development.yml', 'w', encoding='utf-8') as yaml_file:
        google_analytics = meta_data.get("google-analytics", None)
        development_profile = {
            "website": {
                "title": meta_data["title"],
                "site-url": meta_data["custom-domain"],
                "page-footer": {
                    "center": [
                        {
                            "text": meta_data["secondary-email"],
                            "href": f"mailto:{meta_data['secondary-email']}"
                        }
                    ]
                },
            },
            "format": {
                "html": {
                    "description": meta_data["description"]
                }
            },
            "keywords": [meta_data["secondary-email"], meta_data["custom-domain"], "Quarto Resume"],
            "format": {
                "html": {
                    "output-file": "index.html"
                },
                "pdf": {
                    "output-file": "index.pdf"
                }
            }
        }
        if google_analytics:
            development_profile["website"]["google-analytics"] = google_analytics
        yaml.dump(development_profile, yaml_file, default_flow_style=False, encoding='utf-8')
    print("Created _quarto-development.yml from RESUME.json")

    # 3. Check for custom-domain and create CNAME file if it exists
    if 'custom-domain' in meta_data:
        custom_domain = meta_data['custom-domain']
        with open('CNAME', 'w') as cname_file:
            cname_file.write(clean_domain(custom_domain))
        print(f"Created CNAME file with domain: {custom_domain}")

if __name__ == "__main__":
    pre_render()