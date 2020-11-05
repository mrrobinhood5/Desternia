tembed -title "Step 4: Crafting Time - List" -footer "Usage - !dt craft list [-delete] [item]"
<drac2>
pargs=argparse(&ARGS&) #load args
items = load_json(savedCraftItems) #load the cvar into local var
itemToDelete = pargs.get("delete")[0] if pargs.get("delete") else 0
if itemToDelete: # run if there was in item to delete
  if itemToDelete in items: #check to see if it exists
    items.pop(itemToDelete)
    character().set_cvar("savedCraftItems",dump_json(items))
    return f' -f "Deleted|Are you sure you want to delete \"{itemToDelete}\"? I mean its too late.."'
  else:
    return f' -f "Error|You need to spell the item right, or item does not exists in saved items."'

returnstr = ""
for x, y in items.items():
  returnstr += f' -f "{x}|Minimum days to Craft: `{round(y["mindays"],2)}`\nDaily GP cost per check: `{round(y["dailygp"],2)}`\nAbility to be used: `{y["ab"]}`\nCompleted Standard Value: `{y["stdvalue"]}`'
  if "done" in y:
    returnstr +=f'\n Complete: `{y["done"]}`'
  if "itemqual" in y:
    returnstr +=f'\n Item Quality: `{y["itemqual"]}`'
  if "itemval" in y:
    returnstr +=f'\n Item Value: `{y["itemval"]}` gp'
  returnstr += f'"'
return returnstr
</drac2>

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
  }, 
  "blacksword": {
    "mindays": 1.25, 
    "dailygp": 1, 
    "ab": "str", 
    "stdvalue": 10, 
    "dailyrolls": {
      "10.31.20": 18, 
      "11.01.20": 27, 
      "11.02.20": 23
    }, 
    "done": true, 
    "itemqual": "Masterwork", 
    "itemval": 20
  }
}