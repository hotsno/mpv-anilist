# Setup video
https://cdn.discordapp.com/attachments/708155390621122650/965348522176180274/2022-04-17_13-27-02.mp4


# Features
- mpv script to automatically mark episodes as watched on AniList when a file reaches 80% completion
- Python script to open the next episode of a mapped anime in mpv
- Python script to map folders to AniList IDs
- Python script to rename your files to the proprietary naming scheme

# Limitations
- File names need to follow a strict naming scheme
- Not (yet) super user friendly, but should be manageable to set up with basic pretty coding skills
- Current code is only tested to work with macOS, might work on Linux. Currently doesn't for Windows.

# Planned improvements
- Make it work on Linux and Windows
- Make more user friendly (add Windows, Linux, and macOS installers)
- ~~Remove the need for proprietary naming scheme by using [GuessIt](https://github.com/guessit-io/guessit)~~ Unfortunately, probably will not do this

# Installation
1) `git clone https://github.com/hotsno/mpv-anilist` to copy all the files from this repo.
3) Move the `anilist.lua` file inside the `scripts` folder to your [mpv scripts](https://mpv.io/manual/master/#script-location) folder.
4) Edit the `"command"` variable in `anilist.lua` to match your setup's proper Python and `update.py` paths.
5) Run and follow the instructions in `setup.py`
6) You should be done!

# Usage
## AniList updater mpv script
As long as the folder your file is in is mapped (see below) and the file name follows the naming scheme (see below), this should work automatically once an episode reaches 80% played!
## Continue watching script (`continue.py`)
Run `python3 continue.py` (may differ depending on OS). Folders need to be mapped and files need to be named properly for it to work.
## Folder mapping script (`map.py`)
Run `python3 continue.py` (may differ depending on OS). Continue running it until all your folders are mapped.
## Episode renamer script (`renamer.py`)
Run `python3 renamer.py` (may differ depending on OS). This is currently hardcoded to my setup so it will definetly not work out of the box. If you wanna look into the code to change it feel free, otherwise wait for an update.

# Naming scheme
The scripts currently rely on a strict file naming scheme in order to be properly picked up. They must be named in the following format: `Episode 01.mkv`, where the episode number must always equal to the digit count of the highest episode. Ex. if there are 12 episodes, each file must have 2 digits, 1-9 must be padded with one 0.
