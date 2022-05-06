import os
import shutil
import click

def organize_files (src: str, dest: str, copy: bool) -> None:
    print('\n  FILES ORGANIZER')
    try:
        files = os.scandir(src)
        files_list = [file.name for file in files if file.is_file()]
        if len(files_list) == 0:
            click.secho(f'\n  There are no files in the sources directory:\n  {src}', fg='yellow')
        else:
            print(f'\n  Moving' if not copy else f'\n  Copying', 
                        f'a total of {len(files_list)} files.\n')
            folders = set()
            with click.progressbar(files_list,
                empty_char='_', fill_char='>',
                item_show_func=lambda file: str(file)[:20]) as files:
                for file in files:
                    dir_name = os.path.splitext(file)[1][1:]
                    folders.add(dir_name)
                    if not dest:
                        dest = src
                    if not copy:
                        if os.path.exists(os.path.join(dest, dir_name)):
                            shutil.move(os.path.join(src, file), os.path.join(dest, dir_name, file))
                        else:
                            os.makedirs(os.path.join(dest, dir_name))
                            shutil.move(os.path.join(src, file), os.path.join(dest, dir_name, file))
                    else:
                        if os.path.exists(os.path.join(dest, dir_name)):
                            shutil.copy2(os.path.join(src, file), os.path.join(dest, dir_name, file))
                        else:
                            os.makedirs(os.path.join(dest, dir_name))
                            shutil.copy2(os.path.join(src, file), os.path.join(dest, dir_name, file))

                print(f'\n\n  Moved' if not copy else f'\n\n  Copied', 
                    f'{len(files_list)} files to {len(folders)} folders.')
    except FileNotFoundError:
        click.secho(f'\n  The file path could not be found:\n  {src}', fg='yellow')