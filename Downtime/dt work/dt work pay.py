#dt work pay
embed -title "{name} cashes their Paycheck"
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
monthLengths=[x.length+(isLeapYear and x.name==calendar.get('leapMonth','February')) for x in calendar.months]
day,month=calendarDay,1
[(day:=day-monthLengths[x],month:=month+1) for x in range(len(monthLengths)) if month>x and day>monthLengths[x]]
#timestamp=f'{month:02}/{day:02}/{str(year)[2:]} ({hour:02}:{minute:02}:{second:02})'
timestamp=f'{month:02}.{day:02}.{str(year)[2:]}'
</drac2>

<drac2>
rollslist, totalrolls, workdata, returnstr = [], 0, load_json(DTTrack) if exists("DTTrack") else False, f' -f "Unpaid Rolls|'
if workdata:
  for loggedDay, dt in workdata.items():
    if loggedDay != timestamp:
      if "work" in dt:
        for unpaidDays, dayroll in dt.items():
          for each in dayroll.values():
              rollslist.append(each)
              totalrolls += each
              returnstr += f'{each}, '
        dt.pop(unpaidDays)            
  daysworked = len(rollslist)
  allrollsavg = totalrolls/daysworked
  returnstr += f'\" -f "Average|{allrollsavg}" '
  character().set_cvar("DTTrack",dump_json(workdata))
  paybonus = 2 if allrollsavg >= 20 else 1.5 if allrollsavg >=16 else 1 if allrollsavg >= 10 else .75
  coincount = daysworked * paybonus
  returnstr += f' -f "PayCheck|You Worked `{daysworked/2}` days at `2gp` per day with a bonus of `x{paybonus}` for a total of `{coincount} gp`" '
  #breaks down into gp sp and cp
  ngp = int(coincount)
  nsp = (coincount - ngp)*10
  ncp = int((nsp-int(nsp))*10)
  nsp = int(nsp)
  bagsLoaded=load_json(bags) #load the bags
  pouch=([x for x in bagsLoaded if x[0]=="Coin Pouch"])[0] #load the coinpouch
  ogp = pouch[1]['gp'] # what gp was before?
  pouch[1].update({'gp':pouch[1]['gp']+ngp, 'sp':pouch[1]['sp']+nsp, 'cp':pouch[1]['cp']+ncp}) #updates new quantities locally
  pouch in bagsLoaded or bagsLoaded.append(pouch)
  set_cvar("bags",dump_json(bagsLoaded)) #dumps the coins back to the cvar
  returnstr += f' -f "Coins|`{ogp}` gp -> `{ogp+ngp}` gp" '
return returnstr
</drac2>