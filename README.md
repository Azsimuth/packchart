# packchart

Packchart is quickly thrown together tool to visualize the appoximate sizes of installed dkpg and snap packages on the system.
I made it on 2026, March 20, just before school because I wanted to see which packages where taking up what amount of space.
It is worth noting, that the constructed pie chart compares the sizes of the installed packages to the summed size of all packages, not 

## How to Run:

```
bash run.sh <SIZE>
```
where <SIZE> means the minimum size of the packages to be included, in Megabytes.
The program exists with exceptions, that is fine (as of now)

## Requirements

see requirements.txt: python3, and matplotlib

## ToDo

- [ ] Add functionality, so that the program can also filter which package managers to include.
      - example: writing dpkg+snap would result in the pie chart summing up those two.
      - no argument in this case would result in all possible package managers being included.
- [ ] Modularize the system by moving a solution each package manager into it's own scriptfile
- [ ] Rationalize and clean up the code
- [ ] Add SOME error handling
- [ ] Add support for other pacakge managers:
  - [ ] pacman
  - [ ] flatpak
- [ ] Figure out if snap package paths could be prettified in a way

## Misc.

It works on my Kubuntu machine, I have no idea if it does on others, but it'd be nice.

