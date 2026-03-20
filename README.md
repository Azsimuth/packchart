# packchart

Packchart is quickly thrown together tool to visualize the appoximate sizes of installed dkpg and snap packages on the system.
I made it on 2026, March 20, under about an hour because I wanted to see which packages where taking up what amount of space.
It is worth noting, that the constructed pie chart compares the sizes of the installed packages to the summed size of all packages, not 

## How to Run:

```
bash run.sh <SIZE>
```
where <SIZE> means the minimum size of the packages to be included.

## Requirements

see requirements.txt: python3, and matplotlib

## ToDo

- [ ] Add functionality to enable / disable packages from the program
- [ ] Figure out how to make extensible with other package managers
- [ ] Rationalize and clean up the code

## Misc.

It works on my Kubuntu machine, I have no idea if it does on others.
