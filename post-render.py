import os

def post_render():
    # Delete index.md
    if os.path.exists('index.md'):
        os.remove('index.md')
        print("Deleted index.md")
    else:
        print("index.md not found")

    # Delete _variables.yml
    if os.path.exists('_variables.yml'):
        os.remove('_variables.yml')
        print("Deleted _variables.yml")
    else:
        print("_variables.yml not found")

if __name__ == "__main__":
    post_render()