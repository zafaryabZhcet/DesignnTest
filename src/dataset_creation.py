import os
import shutil
from sklearn.model_selection import train_test_split

def create_directory_structure(base_dir, train_folders, test_folder):
    for folder in train_folders:
        os.makedirs(os.path.join(base_dir, 'train', folder), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'test', test_folder), exist_ok=True)

def copy_files(files, dest_dir):
    for file in files:
        shutil.copy(file, dest_dir)

def main():
    source_dir = '/Downloads/cell_images/Uninfected'
    base_dir = 'dataset/cell_image'
    train_folders = [f'uninfected{i}' for i in range(7, 10)]
    test_folder = 'uninfected'
    
    create_directory_structure(base_dir, train_folders, test_folder)
    
    all_files = [os.path.join(source_dir, file) for file in os.listdir(source_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]
    
    train_files, test_files = train_test_split(all_files, test_size=0.1, random_state=42)
    
    copy_files(test_files, os.path.join(base_dir, 'test', test_folder))
    
    train_groups = [train_files[i::3] for i in range(3)]

    for i, group in enumerate(train_groups, 7):
        copy_files(group, os.path.join(base_dir, 'train', f'uninfected{i}'))
    
    print(f"Copied {len(test_files)} files to {os.path.join(base_dir, 'test', test_folder)}")
    for i, group in enumerate(train_groups, 7):
        print(f"Copied {len(group)} files to {os.path.join(base_dir, 'train', f'uninfected{i}')}")
    
if __name__ == "__main__":
    main()
