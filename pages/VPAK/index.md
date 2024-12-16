VPAK files, commonly referred to as VLT (Value Table) by the community, are files that contain properties for Need for Speed Most Wanted, Carbon, ProStreet, Undercover and World.

The files may be compressed with [JDLZ](../JDLZ/) (.lzc).

# Contents
* Settings for opponents
* AI properties for cops
* Vehicle handling and other definitions, like wheel offsets
* Triggers for events in the career
* ...

# Tools
## Commandline
* ![MW](../img/16/mw.png) ![C](../img/16/c.png) ![PS](../img/16/ps.png) ![UC](../img/16/uc.png) ![W](../img/16/w.png) [Attribulator](https://github.com/NFSTools/Attribulator/releases) - Windows (formerly supported Unix), C#, Open source with [proprietary components](#More%20information)

## Graphical
* ![MW](../img/16/mw.png) ![C](../img/16/c.png) ![PS](../img/16/ps.png) ![UC](../img/16/uc.png) ![W](../img/16/w.png) [VltEd](https://nfs-tools.blogspot.com/2019/02/nfs-vlted-v46-released.html) - Windows, C#, Proprietary
* ![MW](../img/16/mw.png) ![C](../img/16/c.png) ![PS](../img/16/ps.png) ![UC](../img/16/uc.png) ![W](../img/16/w.png) [OGVI](https://nfsmods.xyz/mod/5290) - Windows, C#, Proprietary (uses Attribulator)

## Other
* ![MW](../img/16/mw.png) [ModLoader](https://www.nfsaddons.com/downloads/nfsmw/tools/2933/modloader.html) - Windows, C/C++, Proprietary - Hooks into the game and edits values at runtime -- **OUTDATED!**

# More information
* Older versions of VltEd (3.1?) can be used to mod console versions of Need for Speed. However, in those old versions, no new entries can be added. There seems to be no available download of those versions either.
* The author of Attribulator insists on keeping the (de)compression of JDLZ a secret (through [NativeBinary.dll](https://github.com/NFSTools/CoreLibraries/blob/7de534bc8d9d0eaa6be300b81911bc0c075b3a0f/CoreLibraries.GameUtilities/Compression.cs#L29)), despite them likely using these public sources: [1](https://nishi.dreamhosters.com/u/jdlz_v1.rar), [2](https://aluigi.altervista.org/papers/ea_jdlz.c)
