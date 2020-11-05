!alias describe tembed -title "Describe! Testing"
<drac2>
args, me, returnstr, item, savestr = &ARGS&, character(), "", "&1&", {}
pargs = argparse(args)
descriptions = load_json(get("DescribeSaved","{}"))
if "list" in args or "&" in item:
  for x,y in descriptions.items():
    returnstr += f' -f "{x}|{y}"\n'
elif "save" in args:
  savetitle = pargs.get("title")[0]
  savedesc = pargs.get("desc")[0]
  savestr.update = {f'{savetitle}:{savedesc}'}
  descriptions.update(savestr)
  set_uvar("DescribeSaved",dump_json(descriptions))
  returnstr +=f' -f "{savestr["title"][0]}|{savestr["desc"][0]}" \n'
  returnstr +=f' -footer "Has been Saved!"'
else:
  returnstr += f' -f "{item}|{descriptions.get(item)}"'
return returnstr
</drac2>


{
  "First Room" : "The room is cold and hot at the same time",
  "Second Room" : "this this and that"
  }