import os
from pathlib import Path
import sys
from typing import List
import glob

def main(argv: List) -> int:
    """
    Function to change all files with extension "x" to extension "y" within a folder (searches sub folders as well).

    Usage: python3 editor.py <folder_name> <curr_file_extension> <new_file_extension>

    Folder name is name of directory tree root to rename all file extensions.

    Curr file extension is the extension of the files to be renamed.

    New file extension is the extension that will replace the current one.

    Example:

    $ python3 editor.py Carbon c carbon
    """
    if len(argv) != 4:
        print("Error! Usage incorrect! Usage: python3 editor.py <folder_name> <curr_file_extension> <new_file_extension>")
        return 1
    target_dir = argv[1]
    curr_extension = argv[2]
    target_extension = '.' + argv[3]

    program_files = [y for x in os.walk(target_dir) for y in glob.glob(os.path.join(x[0], '*.'+curr_extension))] # Glob magic from https://stackoverflow.com/questions/18394147/how-to-do-a-recursive-sub-folder-search-and-return-files-in-a-list

    # Rename all using pathlib's rename with suffix https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    for f in program_files:
        p = Path(f)
        p.rename(p.with_suffix(target_extension))

    print("Done")

    return 0

if __name__ == "__main__":
    exit(main(sys.argv))