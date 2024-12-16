static-wiki creates a static wiki page out of a collection of folders in a git repository. Use create.py to create one. You can find the output in output/

You need Python 3.4 or newer, and Python markdown (pip install markdown). If you want a history of changes, you need git.

Wiki pages are directories, which can have all sorts of files, including images. Each wiki page has a index.md (or index.html) and tags.txt, everything else is up to you. You should have a "main" page, though.

These pages are automatically generated for you:
* tags
* tag_*
* pages

You can edit the layout and style of the page by editing page.html.
