tembed
#dt work list
<drac2>
pargs, downtime, returnstr = argparse(&ARGS&), "work", ""
if not exists("DTTrack") or DTTrack == "":
  return  f' -title "{name} attemps to check their work history" -desc "No Work History" -f "Fix| Either you havent worked today, or You already got paid for it" '
else:
  workdata = load_json(DTTrack) 
returnstr += f' -title "{name} checks their work history"'
returnstr += f' -f "Unpaid Days|'
for day, dayobj in workdata.items():
  for dt, dtobj in dayobj.items():
    if dt != downtime:
      continue
    for each in dtobj.values():
      returnstr += f'{str(day)} : {str(each)}\n'
returnstr += f' "'
return returnstr
</drac2>