import typer
from filesorganizer.core import organize_files

main = typer.Typer(help="")

@main.command("organize")
def organize(
    src: str = typer.Argument(..., help='path to the source folder.'),
    dest: str = typer.Option('', help='use "--dest=<path>" to define the destination folder. If not defined, the destination folder will be the same as the source folder.'),
    copy: bool = typer.Option(False, help='use "--copy" to make a copy of the files in the destination folder.')
    ):
    """Move or copy files organized in subfolders."""
    organize_files(src, dest, copy)