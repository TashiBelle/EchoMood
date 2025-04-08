# EchoMood
Logic for pixel pet (Echo) mood

# Variables
hp = health points (int)
ep = entertainment points (int)
lp = love points (int)
g = glucose reading (int)
g_logd24 = bool 
g_logd48 = bool

# Basic Logic
IF all of the following are defined and working:
  hp, ep, lp, g_logd24, g_logd48, g

  IF hp ≥ 90 AND ep ≥ 90 AND lp ≥ 90 AND g_logd24 = True AND g ≤ 120:
    mood = "ecstatic"
    
  ELSE IF hp ≤ 25 AND ep ≤ 20 AND lp ≤ 20 AND g_logd48 = False:
    mood = "mad"
  
  ELSE IF (ep ≤ 20 OR lp ≤ 20) AND mood != "mad":
    mood = "lonely"
  
  ELSE IF ep ≥ 80 AND lp ≥ 80 AND mood != "ecstatic":
    mood = "playful"
  
  ELSE:
    mood = "content"

ELSE:
  mood = "broken"

