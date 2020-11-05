tembed -title "Step 4: Crafting Time" {{pargs=&ARGS&}}
# craft-time v2
<drac2>
rawpargs=pargs
pargs=argparse(pargs)
workrate, rarity, abmod, mindays, returnstr, itemcraft = 0, "", "", 0, "", {}
craftbonus = int(pargs.get("b")[0]) if pargs.get("b") else 0
basecost = int(pargs.get("base")[0]) if pargs.get("base") else 0
instructions = f'-f \"You must set ability, `str`,`dex`,`con`,`int`,`wis`,`cha`,or`none`\"\n'
instructions += f'-f \"Set material rarity, `common`,`uncommon`,`rare`,`vrare`,`legendary`\"\n'
instructions += f'-f \"Set Tools bonuses if any with `-b 1` for a +1 tool \"\n'
instructions += f'-f \"Set base cost in GP from `!craft base` or a core item from the PHB with `-base 10`\"\n'
instructions += f'-f \"When ready to export use `-save ItemName` to save the configuration\"\n'
instructions += f'-f \"Example:| To check details for using intelligence, crafting an uncommon item, ' \
                f'with +1 Tools and a base cost of 5gp:\n `!craft time int uncommon -b 1 -base 5 -save ' \
                f'ringofmaniac`\" '
if basecost == 0:
    return instructions
abilities = {"str": strengthMod, "dex": dexterityMod, "con": constitutionMod, "int": intelligenceMod,
             "wis": wisdomMod, "cha": charismaMod, "none": 0}
rarities = {"common": {"dailygp": 1, "timemod": 1, "valuemod": 1},
            "uncommon": {"dailygp": 5, "timemod": 2, "valuemod": 2.5},
            "rare": {"dailygp": 30, "timemod": 3, "valuemod": 15},
            "vrare": {"dailygp": 200, "timemod": 5, "valuemod": 100},
            "legendary": {"dailygp": 1000, "timemod": 10, "valuemod": 500}}
for x in rawpargs:
    if x in abilities.keys():
        ab, abmod = x, abilities[x]
    if x in rarities.keys():
        rarity=x
        y = rarities[x]
        dailygp,timemod,valuemod=y["dailygp"],y["timemod"],y["valuemod"]
if abmod == "" or rarity  == "":
    return instructions
workrate = proficiencyBonus + abmod + craftbonus
mindays = (basecost / workrate) * timemod
totalcost = mindays * dailygp
stdvalue = basecost * valuemod
returnstr += f'-f "To craft an `{rarity}` item, with a base cost of `{basecost} GP` , using your `{ab} ({abmod})` Modifier, and a tool bonus of `{craftbonus}`"\n'
returnstr += f'-f "Your daily work rate is `{workrate} GP` per day"\n'
returnstr += f'-f "Your **MINIMUM** days to craft the item is `{mindays} days` at `{dailygp} GP` per day"\n'
returnstr += f'-f "For a Total Cost of `{totalcost} GP` to craft and a Standard Value of `{stdvalue} GP`"\n'
if pargs.get("save"):
  itemname = pargs.get("save")
  set_cvar_nx("savedCraftItems","{}")
  itemcraft=load_json(savedCraftItems)
  itemcraft.update({itemname[0]: {"mindays": mindays, "dailygp": dailygp, "ab": ab, "stdvalue": stdvalue}})
  character().set_cvar("savedCraftItems",dump_json(itemcraft))
  returnstr += f'-f "Your item has been saved. You can now craft it with `!craft item {itemname[0]}`"\n'
return returnstr
</drac2>
