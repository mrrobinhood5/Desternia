embed
-title "{{name}} Jumps!"
-footer "!jump [high] [long] [spell]"
-thumb {{image}}
<drac2>
returnstr = ""
pargs=argparse(&ARGS&)
me = character()
landing = vroll(me.skills.acrobatics.d20())
jumpspell = True if "spell" in pargs and "jump" in me.spellbook else False

if jumpspell:
    if "high" or "long" in pargs:
        me.spellbook.cast("jump", 1)
        returnstr += f'-f "Using the Jump Spell|{me.spellbook.slots_str(1)}"\n'

if "high" in pargs:
    returnstr += f"-f 'High Jump|When you make a high jump, you leap into the air a number of feet equal to " \
                 f"3 + your Strength modifier (minimum of 0 feet) if you move at least 10 feet on foot " \
                 f"immediately before the jump. When you make a standing high jump, you can jump only half that distance.'\n"

    returnstr += f"-f '{name}| Running High Jump (10ft): `{3+strengthMod if not jumpspell else (3+strengthMod)*3}` ft\n" \
                 f"Standing High Jump: `{ceil((3+strengthMod)/2) if not jumpspell else ceil(((3+strength)*3)/2)}` ft'\n"
    returnstr += f"-f 'Extending Your Arms|You can extend your arms half your height above yourself during the jump. " \
                 f"Thus, you can reach above you a distance equal to the height of the jump plus 1½ times your height. " \
                 f"`!desc` should show your height'\n"
elif "long" in pargs:
    returnstr += f"-f 'Long Jump|When you make a long jump, you cover a number of feet up to your Strength score " \
                 f"if you move at least 10 feet on foot immediately before the jump. When you make a " \
                 f"standing long jump, you can leap only half that distance. Either way, each foot you clear on " \
                 f"the jump costs a foot of movement.'\n"

    returnstr += f"-f '{name}| Running Long Jump (10ft): `{strength if not jumpspell else strength*3}` ft\n" \
                 f"Standing Long Jump: `{ceil(strength/2) if not jumpspell else ceil((strength/2)*3)}` ft\n" \
                 f"Landing on difficult terrain (DC10): {'**FAIL**' if landing.total < 10 else '**SUCCESS**'}\n" \
                 f"{landing.full} '\n"
else:
    returnstr += f"-f 'High Jump|When you make a high jump, you leap into the air a number of feet equal to " \
                 f"3 + your Strength modifier (minimum of 0 feet) if you move at least 10 feet on foot " \
                 f"immediately before the jump. When you make a standing high jump, you can jump only half that distance.'\n"
    returnstr += f"-f 'Long Jump|When you make a long jump, you cover a number of feet up to your Strength score " \
                 f"if you move at least 10 feet on foot immediately before the jump. When you make a " \
                 f"standing long jump, you can leap only half that distance. Either way, each foot you clear on " \
                 f"the jump costs a foot of movement.'\n"

return returnstr
</drac2>