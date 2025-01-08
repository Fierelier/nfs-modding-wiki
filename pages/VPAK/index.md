VPAK (likely short for "vault pack") files are made out of vaults. These vaults contain AttribSys databases, each containing BIN and VLT sections. VPAKs are used in Need for Speed Most Wanted, Carbon, ProStreet, Undercover and World.

The files may be compressed with [JDLZ](../JDLZ/) (.lzc).

# Format
On PC, all integers are little endian, 32-bit and unsigned. On Gamecube and XBOX 360, endianness of some or all numbers may be different.

**Important:** The sorting of vaults matters. Original VPAKs seem to have vaults sorted by their name, using [C's strcmp](https://www.man7.org/linux/man-pages/man3/strcmp.3.html).

## Section 1 - Header
The file's header.

* **Magic:** The string `VPAK`
* **NumEntries:** Number of vaults in file
* **StringBlockOffset:** Where the block of global strings begins
* **StringBlockSize:** The size of the string block, without following padding

## Section 2 - Metadata
Each vault has a metadata entry, describing it. Repeat this sequence `NumEntries` times.

* **NameOffset:** Local offset from StringBlock, string naming this block
* **BinSize:** Size of the bin section, without padding
* **VltSize:** Size of the vlt section, without padding
* **BinOffset:** Global offset of vault's binary section start
* **VltOffset:** Global offset of vault's VLT section start

At the end, there are nulls, padded to the nearest multiple of 64.

## Section 3 - Global string block
Contains strings.

* A list of null-terminated strings
* Nulls, padded to the nearest multiple of 128

## Section 4 - Vault data
Contains the actual data for the vaults. Repeat this sequence `NumEntries` times.

* BIN data
* Nulls, padded to the nearest multiple of 128 (16 might be more accurate)
* VLT data
* Nulls, padded to the nearest multiple of 128

# Notes  
* On PC, having all paddings be set to 16 worked for Most Wanted.
