import os
import shutil

def call_inputs():
    src_folder = input('\nType the source folder of the files: ')
    dst_folder = input('Type the destination folder of the files: ')
    method = ''
    while method != 'move' and method != 'copy':
        method = input("Please choose an option. Type 'move' or 'copy': ").lower()

    organize_files(src_folder, dst_folder, method)

def organize_files (src_folder: str, dst_folder: str, method: str) -> None:
    try:
        files = os.listdir(src_folder)
        num_of_files = len([os.path.abspath(src_folder+'/'+file) for file in files if os.path.isfile(os.path.abspath(src_folder+'/'+file))])
        files = os.scandir(src_folder)
        folders = set()
        for file in files:
            if file.is_file():
                filestr = str(file.name)
                dirname = os.path.splitext(filestr)[1][1:]
                folders.add(dirname)
                if method == 'move':
                    if os.path.exists(dst_folder + '/' + dirname):
                        shutil.move(src_folder + '/' + filestr, dst_folder + '/' + dirname + '/' + filestr)
                    else:
                        os.makedirs(dst_folder + '/' + dirname)
                        shutil.move(src_folder + '/' + filestr, dst_folder + '/' + dirname + '/' + filestr)
                else:
                    if os.path.exists(dst_folder + '/' + dirname):
                        shutil.copy2(src_folder + '/' + filestr, dst_folder + '/' + dirname)
                    else:
                        os.makedirs(dst_folder + '/' + dirname)
                        shutil.copy2(src_folder + '/' + filestr, dst_folder + '/' + dirname)
        if num_of_files == 0:
            print('\nThere are no files in the sources directory.')
            call_inputs()
        else:
            print(f'\nMoved' if method == 'move' else f'\nCopied', 
                f'and organized {num_of_files} files to {len(folders)} folders.')
    except FileNotFoundError:
        print('\nThe file path could not be found.')
        call_inputs()

print('FILES ORGANIZER')
call_inputs()
input('\nPress any key to close.')