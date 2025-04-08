# mood logic tree itself
def determine_mood(hp, ep, kp, g_logd24, g_logd48, g):
  if all(var is not None for var in [hp, ep, lp, g_logd24, g_logd48, g]):
    if hp >= 90 and ep >= 90 and lp >= 90 and g_logd24 and g <= 120:
      return "ecstatic"
    elif hp <= 25 and ep <= 20 and lp <= 20 and not g_logd48:
      return "mad"
    elif (ep <= 20 or lp <= 20):
      return "lonely"
    elif ep >= 80 and lp >= 80:
      return "playful"
    else:
      return "content"
  else:
    return "broken"

# test with example values
if __name__ == "__main__":
  mood = determine_mood(90, 90, 90, True, True, 110)
  print(f"Echo's mood is: {mood}")
