!alias dt-work-job tembed
<drac2>
pargs=argparse(&ARGS&)
if not &ARGS&:
  return f' -title \"{name} attempts to set their job\" -desc \"You didn\'t provide any arguments\" -f \"Usage| `!dt work job -[set] Bunnis Bar and Grill` "'
elif pargs.get("set"):
  job = pargs.get("set")[0]
  character().set_cvar("RosemereJob",job)
  return f' -title "{name} sets their job" -desc "You now work at {job}" -f "Usage| You can now set up your Work Downtime \n`!dt work save [settings]`\n Leave your job with `!dt work job -quit`"'
elif pargs.get("quit"):
  job = RosemereJob
  character().set_cvar("RosemereJob","")
  return f' -title "{name} loses their job" -desc "You are now fired from {job}" -f \"Usage| `!dt work job -[set][delete] \\"Bunnis Bar and Grill\\"` "'
</drac2>
