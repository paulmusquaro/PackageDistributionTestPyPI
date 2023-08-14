import os
import shutil
import sys

def normalize(text):
    translit_table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia'
    }

    result = []
    for char in text:
        if char.isalnum():
            result.append(char)
        elif char.lower() in translit_table:
            result.append(translit_table[char.lower()])
        else:
            result.append('_')

    return ''.join(result)

def process_folder(folder_path):
    images_ext = ('.jpeg', '.png', '.jpg', '.svg')
    videos_ext = ('.avi', '.mp4', '.mov', '.mkv')
    documents_ext = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_ext = ('.mp3', '.ogg', '.wav', '.amr')
    archives_ext = ('.zip', '.gz', '.tar')
    
    extensions = {}
    
    folders = {
        'images': 'images',
        'videos': 'videos',
        'documents': 'documents',
        'music': 'music',
        'archives': 'archives',
    }
    
    for item in os.listdir(folder_path):
        print(f"Item {item}")
        item_path = os.path.join(folder_path, item)
        print(f"Item_path {item_path}")
        if os.path.isdir(item_path):
            if item not in folders.values():
                process_folder(item_path)
        else:
            base_name, ext = os.path.splitext(item)
            print(f"base_name {base_name} ext {ext}")
            new_name = normalize(base_name) + ext
            print(f"new_name {new_name}")
            new_path = os.path.join(folder_path, new_name)
            print(f"new_path {new_path}")
            os.rename(item_path, new_path)
            
            if ext not in extensions:
                extensions[ext] = []
            extensions[ext].append(new_name)
            
            if ext.lower() in images_ext:
                if not os.path.exists(os.path.join(folder_path, folders['images'])):
                    os.mkdir(os.path.join(folder_path, folders['images']))
                os.rename(new_path, os.path.join(folder_path, folders['images'], new_name))
            elif ext.lower() in videos_ext:
                if not os.path.exists(os.path.join(folder_path, folders['videos'])):
                    os.mkdir(os.path.join(folder_path, folders['videos']))
                os.rename(new_path, os.path.join(folder_path, folders['videos'], new_name))
            elif ext.lower() in documents_ext:
                if not os.path.exists(os.path.join(folder_path, folders['documents'])):
                    os.mkdir(os.path.join(folder_path, folders['documents']))
                os.rename(new_path, os.path.join(folder_path, folders['documents'], new_name))
            elif ext.lower() in music_ext:
                if not os.path.exists(os.path.join(folder_path, folders['music'])):
                    os.mkdir(os.path.join(folder_path, folders['music']))
                os.rename(new_path, os.path.join(folder_path, folders['music'], new_name))
            elif ext.lower() in archives_ext:
                archive_folder = os.path.join(folder_path, folders['archives'], os.path.splitext(new_name)[0])
                os.makedirs(archive_folder, exist_ok=True)
                shutil.unpack_archive(item_path, archive_folder)
                os.remove(new_path)
    
    print("Sorted files:")
    for folder, files in folders.items():
        if folder != 'archives':
            folder_path = os.path.join(folder_path, files)
            if os.path.exists(folder_path):
                sorted_files = os.listdir(folder_path)
                if sorted_files:
                    print(f"{folder}: {sorted_files}")
                else:
                    print(f"{folder}: No files")
    
    print("\nKnown extensions:")
    for ext, files in extensions.items():
        print(f"{ext}: {files}")

    unknown_ext = set()
    if os.path.exists(folder_path):
        for f in os.listdir(folder_path):
            try:
                if os.path.isfile(os.path.join(folder_path, f)):
                    unknown_ext.add(os.path.splitext(f)[1].lower())
            except FileNotFoundError:
                continue
    unknown_ext -= set(extensions.keys())

    print("\nUnknown extensions:")
    print(list(unknown_ext))

def main():
    if len(sys.argv) >= 2:
        folder_to_sort = sys.argv[1]
    else:
        folder_to_sort = input("Write path to folder: ")
    process_folder(folder_to_sort)

if __name__ == "__main__":
    main()
else:
    print("That's not module! Don't use it in this way")