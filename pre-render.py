import json
import yaml
from urllib.parse import urlparse

DEFAULT_TEXT_VAR = "Quarto Resume"

def clean_domain(url):
    if not url:
        return None
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
        title = meta_data.get("title", "Resume")
        custom_domain = clean_domain(meta_data.get('custom-domain', None))
        secondary_email = meta_data.get('secondary-email', None)
        description = meta_data.get('description', DEFAULT_TEXT_VAR)
        keywords = ', '.join([secondary_email, custom_domain, DEFAULT_TEXT_VAR])
        development_profile = {
            "website": {
                "site-url": custom_domain,
                "page-footer": {
                    "center": [
                        {
                            "text": secondary_email,
                            "href": f"mailto:{secondary_email}"
                        }
                    ]
                },
            },
            "format": {
                "html": {
                    "description": description
                }
            },
            "format": {
                "html": {
                    "output-file": "index.html",
                    "header-includes": '\n'.join([f'<meta name="keywords" content="{keywords}">']),
                    "pagetitle": title,
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

    # Check for custom-domain and create CNAME file if it exists
    if custom_domain:
        with open('CNAME', 'w') as cname_file:
            cname_file.write(custom_domain)
        print(f"Created CNAME file with domain: {custom_domain}")

if __name__ == "__main__":
    pre_render()