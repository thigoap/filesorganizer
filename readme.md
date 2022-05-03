## FILES ORGANIZER

A python script to organize files in subfolders according to their extensions.

#### Install the requirements:

``` pip install -r requirements.txt ```

#### Run with:

``` python -m filesorganizer PATH_TO_SOURCE_FOLDER ```

If your folder has spaces, you will need to use " ":

``` python -m filesorganizer "PATH_TO_SOURCE_FOLDER" ```

#### Some options:

1. Define destination folder (default is the same as the source folder):

``` python -m filesorganizer PATH_TO_SOURCE_FOLDER --dest=PATH_TO_DESTINATION_FOLDER ```

2. Copy the files (default is to move):

``` python -m filesorganizer PATH_TO_SOURCE_FOLDER --copy ```


#### Check help:

``` python -m filesorganizer --help ```


#### Another CLI version:

There is another version of the script which does not need any external imports. I made this one (organizer.py inside exe folder) just to create a executable version of the script.
You can run this version with:

``` python organizer.py ```
