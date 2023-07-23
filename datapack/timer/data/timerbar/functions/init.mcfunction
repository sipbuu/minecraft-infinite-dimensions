scoreboard objectives add Timer.timeLeft dummy
scoreboard objectives add Timer.math dummy
scoreboard objectives add Timer.maxSet dummy
scoreboard objectives add Timer.started dummy
scoreboard players set value Timer.started 0
scoreboard players set 1 Timer.math 1
scoreboard players set 0 Timer.math 0
scoreboard players set 20 Timer.math 20
scoreboard players set 2 Timer.math 2
execute store success score value Timer.maxSet run scoreboard players get max Timer.timeLeft
execute run scoreboard players set max Timer.timeLeft 180
bossbar add timer "timer"
bossbar set timer name "Time left before teleport:"
bossbar set timer color green
bossbar set timer visible false
