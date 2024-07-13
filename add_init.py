import os

def add_init_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Abaikan direktori .git atau direktori lain yang tidak perlu
        if '.git' in dirpath:
            continue
        # Buat file __init__.py jika tidak ada
        init_file = os.path.join(dirpath, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                pass
            print(f'Created: {init_file}')

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.dirname(__file__))
    add_init_files(project_root)
