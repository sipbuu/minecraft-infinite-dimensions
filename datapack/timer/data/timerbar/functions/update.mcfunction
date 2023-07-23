bossbar set timer players @a
execute if score value Timer.started > 15 Timer.math if score value Timer.timeLeft < 0 timer.math run scoreboard players set value Timer.started 0
execute if score value Timer.started > 0 Timer.math if score value Timer.paused = 0 Timer.math run scoreboard players operation value Timer.timeLeft -= 1 Timer.math
execute if score value Timer.started > 0 Timer.math store result bossbar timer value run scoreboard players get value Timer.timeLeft
execute if score value Timer.timeLeft matches 1101.. run bossbar set timer color green
execute if score value Timer.timeLeft matches 1101.. run bossbar set minecraft:timer name {"text":"Time left before teleport:","color":"dark_green","bold": true}
execute if score value Timer.timeLeft matches 401..1100 run bossbar set timer color yellow
execute if score value Timer.timeLeft matches 401..1100 run bossbar set minecraft:timer name {"text":"Time left before teleport:","color":"yellow","bold": true, "italic": true}
execute if score value Timer.timeLeft matches 0..400 run bossbar set timer color red 
execute if score value Timer.timeLeft matches 0..400 run bossbar set minecraft:timer name {"text":"Time left before teleport:","color":"red","bold": true, "italic": true}
execute if score value Timer.timeLeft matches -69..0 run bossbar set timer color red 
execute if score value Timer.timeLeft matches -69..0 run bossbar set minecraft:timer name {"text":"Teleporting:","color":"dark_red","bold": true,"italic": true}
execute if score value Timer.timeLeft matches ..-70 run function timerbar:starttimer


