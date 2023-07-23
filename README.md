# Random Warps for 20w14infinite

Python program with the usage and intention of teleporting players by using the minecraft server command prompt hosted on a **local server**/**on the same pc** (on version 20w14infinite, as the name states) and executes commands that teleport all players to a randomly selected dimension either 3 minutes or a custom number chosen by you!

## Credits

- [Besteres](https://github.com/Besteres) - **Made** the [original project for the file](https://github.com/Besteres/RandomWarps20w14) which allowed for the generation of the random warps, and for players through the server console to be warped there.
- [Sipbuu](https://github.com/Sipbuu) - **Modified** the original base code and made some **QOL life changes** (such as the timer w/ the datapack) and some changes with the **generation of the warps** from the original file.

## Installation / Setup

#### Server
Firstly, you need a locally hosted server, meaning a server that is hosted on your computer, if you do not already have one then [here is a tutorial from the minecraft forums](https://help.minecraft.net/hc/en-us/articles/360058525452-How-to-Setup-a-Minecraft-Java-Edition-Server) and the server needs to be running on 20w14infinite, which the server jar for the version can be found [here at this link](https://mcversions.net/download/20w14infinite)

Once you've finished creating and making the server, if you downloaded the folder that came with a ``Run.bat`` file, drag the ``Run.bat`` from that folder into the location where you server is at, like as an example `C:\test server\`, and run the file, which should start your server and is now able to be used with the application

#### Application

***Before we begin with the application, make sure that the server console and the application window (once you've opened it) are all visible and not minimized, otherwise this will not work***

If you've already done everything needed on the server then, run the executable that you installed, which should either be ``Random Warp.exe``, ``Random Warp 3 Minutes.exe``, or one that is named close to this, and you should be prompted with a command window, **if all went well**, it should not close as soon as you open it, if it does close, then follow instructions at the ***Errors*** section, otherwise follow the instructions and you should now be playing with the random warps!

## Errors / Common Questions
If you have any errors/questions that aren't listed feel free to message me on my socials about this, and I'll try my best to provide help.

#### The commands get put into the command prompt all in one line and do not enter/has to be pressed manually
This usually occurs when **the application window and the server console window** are not on the screen at the time which can cause this to happen, if they are all on the screen at the same time then it might be because the **CTRL** button was being pressed at the time which is a glitch that I am trying to fix, but as of right now you cannot press **CTRL**. If it does happen, restart the application.

#### The application just opens and closes as soon as I run it
Try to see what error pops up before it closes, if it says ``ModuleNotFoundError: No module named 'win32gui`` or something along the lines of this, then it is an error in regards to python, what you can try to do is run (with python installed) `pip install pywin32` and if it continues try to follow [this answer to fix it](https://stackoverflow.com/a/72091179)

It could also be affected by the version of python that you are using, however I am unsure of this right now.

#### How do I edit the datapack for my custom time
Follow the tutorial that is on the README.md over at the [datapack folder in this github repository.](https://github.com/sipbuu/random-warp-infinite/tree/main/datapack) It will help you with editing and fixing it to work with your custom time. This is mainly because the limitations of minecraft datapacks as of right now.

#### Nothing is happening after the wait time / Dimension is printed but nothing happens on the console
This usually means that the application doesn't recognize your server console with the name `C:\Windows\system32\cmd.exe`, or you don't have the console open at all. If this does occur try running the application again, and if you haven't, try running the `Run.bat` (which should be in your server folder) that comes with the easy set-up download option.  

#### The Bat file opens and then closes or shows an error
If it shows an error, try to fix whatever it says the error may be caused by, this also could be just that the bat file isn't in the server folder/right location.


