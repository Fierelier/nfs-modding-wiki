Creating a backup allows you to keep accessing the information on this wiki, even if it goes down.
# 1. Prerequisites
## Git
### Windows 7+
Get [git-scm](https://git-scm.com/downloads)
### Windows XP
Skip any steps involving git, [download the wiki as a zip](https://github.com/Fierelier/nfs-modding-wiki/archive/refs/heads/master.zip) (You will lose all information relating to the history!)
### Linux
Install `git` in your package manager.

## Python 3.4+
### Modern Windows
Just get [the newest version](https://www.python.org/downloads/)
### Windows 7
You want to grab [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
### Windows XP
Get [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
### Linux
Install `python3` or `python` in your package manager.

# 2. Making a clone
Go to a directory, like Documents, run a terminal and enter `git clone https://github.com/Fierelier/nfs-modding-wiki`. The wiki, and its history will be saved in a directory called `nfs-modding-wiki`.

# 3. Creating the pages
The wiki will have to be converted from Markdown to HTML, to be readable in a browser. To do this, run `create.py`. The final page is in the output directory, which is next to create.py.

# 4. Optional: re-upload the wiki
Put the output folder on your hoster of choice.
