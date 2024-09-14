import os

def delete_func(file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} not found")

def post_render():
    # Delete index.qmd
    delete_func('index.qmd')

    # Delete _quarto-development.yml
    delete_func('_quarto-development.yml')

    # Delete CNAME
    delete_func('CNAME')

if __name__ == "__main__":
    post_render()