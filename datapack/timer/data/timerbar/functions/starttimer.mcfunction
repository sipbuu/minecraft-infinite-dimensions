bossbar set timer visible true
scoreboard players operation max Timer.timeLeft *= 20 Timer.math
scoreboard players operation value Timer.timeLeft = max Timer.timeLeft
execute store result bossbar timer max run scoreboard players get max Timer.timeLeft
execute store result bossbar timer value run scoreboard players get max Timer.timeLeft
scoreboard players operation max Timer.timeLeft /= 20 Timer.math
scoreboard players set value Timer.started 1
