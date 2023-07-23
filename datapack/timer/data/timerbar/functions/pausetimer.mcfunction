execute if score value Timer.paused = 1 Timer.math run scoreboard players set value Timer.paused 2
execute if score value Timer.paused = 0 Timer.math run scoreboard players set value Timer.paused 3
scoreboard players operation value Timer.paused -= 2 Timer.math