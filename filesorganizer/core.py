import os
import shutil

def organize_files (src: str, dest: str, copy: bool) -> None:
    try:
        files = os.listdir(src)
        num_of_files = len([os.path.abspath(src+'/'+file) for file in files if os.path.isfile(os.path.abspath(src+'/'+file))])
        files = os.scandir(src)
        folders = set()
        for file in files:
            if file.is_file():
                filestr = str(file.name)
                dirname = os.path.splitext(filestr)[1][1:]
                folders.add(dirname)
                if not dest:
                    dest = src  
                if not copy:
                    if os.path.exists(dest + '/' + dirname):
                        shutil.move(src + '/' + filestr, dest + '/' + dirname + '/' + filestr)
                    else:
                        os.makedirs(dest + '/' + dirname)
                        shutil.move(src + '/' + filestr, dest + '/' + dirname + '/' + filestr)
                else:
                    if os.path.exists(dest + '/' + dirname):
                        shutil.copy2(src + '/' + filestr, dest + '/' + dirname)
                    else:
                        os.makedirs(dest + '/' + dirname)
                        shutil.copy2(src + '/' + filestr, dest + '/' + dirname)
        if num_of_files == 0:
            print('\nThere are no files in the sources directory.')
        else:
            print(f'\nMoved' if not copy else f'\nCopied', 
                f'{num_of_files} files to {len(folders)} folders.')
    except FileNotFoundError:
        print('\nThe file path could not be found.')