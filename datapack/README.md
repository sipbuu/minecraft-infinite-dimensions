# Datapack for the project
This is the datapack that is used for the timer that you see in-game when you use the **3 minute executable** version of the project. 

The project still works fine w/o the datapack and you can even edit it to work with the **customizable time executable** version of the project, refer to [***Editing***](https://github.com/sipbuu/minecraft-infinite-dimensions/edit/main/datapack/README.md#editing)

## Credits

- [Seamuskills](https://www.planetminecraft.com/member/seamuskills/) - Made the base [timer datapack](https://www.planetminecraft.com/data-pack/boss-bar-timer/) which allowed for the timer that is used in this project.
- [Sipbuu](https://github.com/Sipbuu) - **Modified** the timer to fit what the project needed, and modified some of the mcfunctions to work with the teleporting.

## Editing

If you would like to edit the datapack to fit your own custom time length (*in seconds*) then follow this tutorial on how to do so.

### Requirements
- Any sort of code editing program that allows ``.mcfunction`` files to be edited/that is able to open and edit ``.mcfunction`` files (**Notepad works too**)
- *Optional*: Extensions that allow for easier use of reading and editing of ``.mcfunction`` files. 

### Starting
Firstly, open up whatever application you are using to edit and head to your datapack folder.

Find the functions folder which should be located within the folder at ``timer/data/timerbar/functions/``

You should now see 6 ``.mcfunctions`` files, we are going to focus on the two that are labelled ``init.mcfunction`` and ``update.mcfunction``

### Changing init.mcfunction
Within the ``init.mcfunction``, look at line 11, which is ``execute run scoreboard players set max Timer.timeLeft 180``, and change the number to be the integer number that is going to fit your custom timer. 

For example, if I wanted it to be 30 seconds rather than 180, I would change the line to be ``execute run scoreboard players set max Timer.timeLeft 30``, the 30 being my own custom number.

### Changing update.mcfunction

Changing ``update.mcfunction`` is a little bit more trickier, as it has to do with tick values, instead of seconds, however there's a trick you can do.

Within lines ``5-10`` you should see lines that say `execute if score value Timer.timeLeft matches [WHATEVER NUMBER IN THE SCRIPT]`

An example has been given below to help with changing ``update.mcfunction``.

#### Example

- Let's say my custom number for seconds is ``60``.

- I want to start having the yellow parts happening at around ``20 seconds`` before it ends. Multiplying ``20 seconds`` by the ticks per second with your server (``usually 20``) would give me `400`.

- Now, the number will be added up by 1, which means it is now ``401``, and it will be put into lines ``5-6``, replacing the number that appears after the ``score value Timer.timeLeft matches [number]..``, so now my lines ``5-6`` will now have this instead line instead ``execute if score value Timer.timeLeft matches 401..``

- And now, I want for the red parts to start happening around ``10 seconds`` and following the formula from earlier, would get me ``200``.

- Now, the number (again) will be added up by 1, which means it is now ``201``, and now for lines ``7-8``, I will replace the numbers that appear after the ``score value Timer.timeLeft matches [number]..[othernumber]``, with the first number being our new number ``201``, and the second number being our yellow parts number, `400` (without being added up by 1 this time)

- So, lines ``7-8`` should now look like this at the start of them: ``execute if score value Timer.timeLeft matches 201..400 run [script stuff]``

- And now, for the last lines ``9-10``, which is pretty easy since we just replace the last number after ``matches 0..[number]`` with our red parts number, which is ``200`` (without it being added up by 1).

- So, lines ``9-10`` should just simply look like this: ``execute if score value Timer.timeLeft matches 0..200``

Now with changing ``update.mcfunction``, just repeat the example steps but replacing the number for seconds ``60`` with the number you chose.
