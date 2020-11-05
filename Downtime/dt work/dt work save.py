#dt work save
!alias dt-work-save embed -title "Configuring Job Settings"
<drac2>
pargs,me,returnstr,errstr,jobstr,charskills,hasTools,isTool=argparse(&ARGS&),character(),"",f' -f "Usage| `!dt work save -quan [skill] -qual [skill or tool|ability] -relation [charisma skill]`"\n -f "Example | Steve will work fishing. He will use his athletics (con) for quantity of work, Fishing Tackle and Wisdom for his quality, and persuasion to sell his items\n `!dt work save -quan ath -qual fish|wis -relation pers`"',f' -f "Error| You must set your job first with `!dt work job -set \\"jobname\\""`', "persuasiondeceptionperformanceintimidation",True if exists("pTools") else False, False
qualarg, quanarg, relationarg = pargs.get("qual"),pargs.get("quan"),pargs.get("relation")
qualargs,availTools = qualarg[0].split("|") if qualarg else "",pTools.split(",") if hasTools else ""
if not exists("RosemereJob") or RosemereJob == "":
  return jobstr
if not qualarg or not relationarg or not quanarg or relationarg[0] not in charskills:
  return errstr 
else:
  for x in availTools:
    if qualargs[0].lower() in x.lower():
      qualskill = x
      isTool = True
  for x, y in me.skills: #passing qualargs ability
      if not isTool and qualargs[1].lower() in x.lower():
        qualability = x
        qualabmod = y.value
  for x, y in me.skills:
    if quanarg[0].lower() in x.lower(): #checks the quantity skill in skills are assignes the skill name and skill bonus
      quanskill = x
      quanmod =floor(proficiencyBonus*y.prof)+y.bonus+constitutionMod
      returnstr +=f' -f "Work Quantity| Is set to `{quanskill}`: +`{quanmod}`"\n'
    if relationarg[0].lower() in x.lower(): #checks the relation skill and assigns the relation skill name and bonus
      relationskill = x
      relationmod=y.value
      returnstr +=f' -f "Work Relations| Is set to `{relationskill}`:  +`{relationmod}`"\n'
    if isTool and qualargs[1].lower() in x.lower(): #checks the qual ability and sets the name and bonus for the ability plus proficiency if you are using tools
      qualability = x
      qualmod = y.value+proficiencyBonus
    if not isTool and qualargs[0].lower() in x.lower():
      qualskill = x
      qualskmod = floor(proficiencyBonus*y.prof)+y.bonus
      qualmod = qualskmod+qualabmod
  returnstr += f' -f "Work Quality| Is set to `{qualskill}({qualability})`:  +`{qualmod}`"\n'
  settingstr = f'{quanskill},{quanmod},{isTool},{qualskill},{qualability},{qualmod},{relationskill},{relationmod}'
  me.set_cvar("JobSettings",settingstr)
return returnstr
</drac2>