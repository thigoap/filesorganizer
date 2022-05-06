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


#### Screenshots:

![filesorganizer](https://user-images.githubusercontent.com/11902225/167124931-cb70e48d-6599-4ea4-9cf5-aab50c367d38.png)
