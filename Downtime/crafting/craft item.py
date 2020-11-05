!alias craft-item tembed -title "Step 5: Crafting Items" -footer "Usage - !craft item -tool \"ToolName\" -item \"Item Name\""
{{f'''{'{'*2}pargs=&ARGS&{'}'*2}'''}}
{{get_gvar("4f86b818-5fae-43c2-9484-c41d9f54cdac")}}

#craft item
<drac2>
calendar=load_json(get_gvar("1aec09a0-9e25-4700-9c2d-42d79cb0163b"))
hourOffset=calendar.get('hourOffset',0)+int(get('timezone',0))
baseYear=calendar.get("yearOffset",1970)
Time=time()+(3600*hourOffset)
totalDayCount=int((Time)//86400)
yearsPassed=totalDayCount//calendar.length
numLeapYears=len([x for x in range(baseYear,baseYear+yearsPassed-4) if x//calendar.get('leapCycle',4)==x/calendar.get('leapCycle',4)]) if calendar.get('leapCycle') else 0
yearStartDay=yearsPassed*calendar.length+numLeapYears
totalDays=totalDayCount-yearStartDay
year=int((totalDayCount-numLeapYears-1)//calendar.length)+baseYear
isLeapYear=year//calendar.get('leapCycle',4)==year/calendar.get('leapCycle',4) if numLeapYears else 0
calendarDay=totalDays%(calendar.length+isLeapYear) or calendar.length+isLeapYear
hour=int(Time%86400//3600)
minute=int(Time%86400%3600//60)
second=int(Time%86400%3600%60)
monthLengths=[x.length+(isLeapYear and x.name==calendar.get('leapMonth','February')) for x in calendar.months]
day,month=calendarDay,1
[(day:=day-monthLengths[x],month:=month+1) for x in range(len(monthLengths)) if month>x and day>monthLengths[x]]
xptimestamp=f'{day:02}.{month:02}.{str(year)[2:]} ({hour:02}:{minute:02}:{second:02})'
timestamp=f'{month:02}.{day:02}.{str(year)[2:]}'
</drac2>
<drac2>
#sets all all primary variables
alreadyRolled, hasTools, hasItems, rollstr, me, dailyroll, numberOfRolls, hasRolls, averagerolls, returnstr, foundTool, foundItem, oxp, nxp = False, True if exists("pTools") else False, True if exists("savedCraftItems") else False, "1d20+", character(), 0, 0, False, 0, "", False, False, 0, 0
pargs = argparse(&ARGS&) # only uncomment on WorkShop
# pargs = argparse(pargs) # only uncomment on GVAR
#sets all the secondary variables
availTools, selectedTool, selectedItem = pTools.split(",") if hasTools else "", pargs.last("tool"), pargs.last("item")

#loads the saved crafting items from craft time 
availItems=load_json(savedCraftItems) if hasItems else None

#checks to see if you have tools and if the one you passed in with -tool exists
if hasTools and selectedTool:
  for tool in availTools:
    if selectedTool.lower() in tool.lower():
      selectedTool = tool
      foundTool = True

#checks to see if you have items and if the one you passed in with -item exists
if hasItems and selectedItem:
  for item, itemdata in availItems.items():
    if selectedItem.lower() in item.lower():
      selectedItem = item
      selectedData = itemdata
      foundItem = True
      selectedData.update({"dailyrolls":{}}) if "dailyrolls" not in selectedData else ""

#iterates through skills to match up your ability saved in savedCraftItems
for x,y in me.skills:
  if selectedData["ab"].lower() in x.lower():
    abmod = y.value + proficiencyBonus
    rollstr += str(abmod)

#before rolling, checks to see if you have a roll for today otherwise wont roll and update the daily roll dict
dailyroll = vroll(rollstr)
if timestamp in selectedData["dailyrolls"]:
  alreadyRolled = True
  numberOfRolls = len(selectedData["dailyrolls"])
else:
  selectedData["dailyrolls"].update({timestamp:dailyroll.total})
  numberOfRolls = len(selectedData["dailyrolls"])
  #deduct material costs and gain XP
  bagsLoaded=load_json(bags) #load the bags
  pouch=([x for x in bagsLoaded if x[0]=="Coin Pouch"])[0] #load the coinpouch
  ogp = pouch[1]['gp'] # what gp was before?
  opp = pouch[1]['pp'] # what pp was before
  if selectedData["dailygp"] > ogp: #checks to see if you have enough gp to craft
    if selectedData["dailygp"]*.1 > opp:# if not, checks to see if you have enough pp to cover it
      err(f'You need {selectedData["dailygp"]} gp to craft today. You only have {ogp}. Try to convert your lower coins with `!coins convert`') #if you cant cover the costs, errors out.
    else: # if enough pp error change to convert
      err(f'You need {selectedData["dailygp"]} gp to craft today. Exchange your pp to gp to have enough gold. ')
  else:
    #does the coins stuff
    pouch[1].update({'gp':pouch[1]['gp']-selectedData["dailygp"]}) #updates the local copy to subtract material costs
    ngp = pouch[1]['gp'] #grabs the new amount
    pouch in bagsLoaded or bagsLoaded.append(pouch)
    set_cvar("bags",dump_json(bagsLoaded)) #dumps the coins back to the cvar
    #does the XP stuff
    xplog = load_json(xplog)
    xplog.update({xptimestamp:"+25 crafting"})
    set_cvar("xplog",dump_json(xplog))
    oxp = me.cc_str("Experience")
    me.mod_cc("Experience",+25)
    nxp =me.cc_str("Experience")

#gets the rolled averages
for x,y in selectedData["dailyrolls"].items():
  averagerolls += y 
averageroll = averagerolls / len(selectedData["dailyrolls"].values())

#gets the running quality of the item
if averageroll >= 21:
  itemQuality = "Masterwork"
  itemValue = selectedData["stdvalue"]*2
elif averageroll > 19:
  itemQuality = "Exceptional"
  itemValue = selectedData["stdvalue"]*1.5
elif averageroll > 17:
  itemQuality = "Superior"
  itemValue = selectedData["stdvalue"]*1.2
elif averageroll > 14:
  itemQuality = "Standard"
  itemValue = selectedData["stdvalue"]*1
elif averageroll > 12:
  itemQuality = "Poor"
  itemValue = selectedData["stdvalue"]*.5
elif averageroll > 4:
  itemQuality = "Shoddy"
  itemValue = selectedData["stdvalue"]*.1
else:
  itemQuality = "Ruined"
  itemValue = selectedData["stdvalue"]*0

#marks item complete and updates some info on the cvar
itemComplete = True if numberOfRolls >= selectedData["mindays"] else False
selectedData.update({"done":itemComplete, "itemqual": itemQuality, "itemval": itemValue})

#commit all the data to the cvar
availItems.update({selectedItem:selectedData})
set_cvar("savedCraftItems",dump_json(availItems))

#builds the output string, and sends it back
returnstr += f' -f "Tool|{"Not Found" if foundTool == False else selectedTool}" '
returnstr += f' -f "Item|{"Not Found" if foundItem == False else selectedItem}" '
returnstr += f' -f "Daily Roll|{"You already Rolled for today!" if alreadyRolled else dailyroll.full}" '
returnstr += f' -f "Progress|Day `{numberOfRolls}` out of `{selectedData["mindays"]} {"**COMPLETE**" if itemComplete else ""}`\nAverage: `{averageroll:.2f}`\nQuality: `{itemQuality}` worth `{itemValue}` gp" '
returnstr += f' -f "Costs and Rewards|XP: `{oxp}` -> `{nxp}`\n Material Cost: `{ogp}` -> `{ngp}` gp"' if not alreadyRolled else f''
return returnstr
</drac2>

#saved Data Format
{
  "LongItem": {
    "mindays": 60.0, 
    "dailygp": 30, 
    "ab": "con", 
    "stdvalue": 3000,
    "dailyrolls": {
      "10.30.20": 19,
      "10.31.20": 20
      }
    }, 
    "coolItem": {
      "mindays": 12.5, 
      "dailygp": 1, 
      "ab": "dex", 
      "stdvalue": 100
      }
}