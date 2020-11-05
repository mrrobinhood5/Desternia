tembed
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
#timestamp=f'{month:02}/{day:02}/{str(year)[2:]} ({hour:02}:{minute:02}:{second:02})'
timestamp=f'{month:02}.{day:02}.{str(year)[2:]}'
</drac2>

<drac2>
#initialize all of the variables
pargs, downtime, returnstr, baseroll =argparse(&ARGS&), "work",  "", "1d20+"
#determine if it will run once or twice
downtimes, results = 1 if pargs.get("part") or pargs.get("parttime") or pargs.get("part-time") else 2, {timestamp:{downtime:{}}}
#If this is first time, save an empty dict for today and load the work history
character().set_cvar("DTTrack",dump_json(results)) if not exists("DTTrack") else 0 
workdata = load_json(DTTrack) 
# check if Job and Settings have been set first, and then parse the arguments
if not exists("RosemereJob"):
  return f' -title "{name} attemps to work" -desc "You dont have a job." -f "Fix| Set your job with `!dt work job -set \\"Bunnis Bar and Grill\\"`" '
elif not exists("JobSettings"):
  return f' -title "{name} attemps to work" -desc "You havent set up your job settings" -f "Fix| Do `!dt work save` for more info" '
  #if all is well, execute work
else:
  dtcount = 0
  #checks to see if you've worked today already
  if timestamp in workdata:
    for dts in workdata[timestamp][downtime]:
      dtcount += 1
    if dtcount + downtimes > 2: 
      return f' -title "{name} attemps to work" -desc "You dont have enought downtimes" -f "Fix|Roses are red\n Violets are blue\nMy poems suck\nCome back tomorrow for work or if do `!dt work part-time`"'
  #loads Job Settings from !dt work save
  js = JobSettings.split(",")
  for x in range(downtimes):    
    quanroll = vroll(baseroll+js[1])
    qualroll = vroll(baseroll+js[5])
    relationroll = vroll(baseroll+js[7])
    averageroll = (quanroll.total+qualroll.total+relationroll.total)/3
    results[timestamp][downtime].update({str(x+1):floor(averageroll)})
    returnstr += f' -title "{name} works at {RosemereJob}" -f "Results|Work Quantity: *{js[0].capitalize()}(Constitution)*\n{quanroll.full}\nWork Quality: *{js[3].capitalize()}({js[4].capitalize()})*\n{qualroll.full}\nWork Relations: *{js[6].capitalize()}*\n{relationroll.full}"'   
  workdata.update(results)
  character().set_cvar("DTTrack",dump_json(workdata)) 
  return returnstr
</drac2>


















