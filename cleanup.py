import os
import shutil

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

def clean_output_directory(output_dir: str) -> None:
    try:
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if item != '.gitignore':
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                    print(f"Removed file: {item_path}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Removed directory: {item_path}")
    except Exception as e:
        print(f"Error while cleaning output directory: {e}")

def clean_pycache(root_dir: str) -> None:
    try:
        for root, dirs, files in os.walk(root_dir):
            for dir_name in dirs:
                if dir_name == '__pycache__':
                    pycache_path = os.path.join(root, dir_name)
                    shutil.rmtree(pycache_path)
                    print(f"Removed __pycache__: {pycache_path}")
    except Exception as e:
        print(f"Error while cleaning __pycache__: {e}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    clean_output_directory(output_dir)
    
    clean_pycache(project_root)
