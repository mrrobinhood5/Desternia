**Using E**

`!e "area name"`
moves to the named area if it's available from the current area. You can type partial out of the choices and is not case-sensitive.

`!e list`
shows you a list of available settings, will load the example ones if you don't have any.

`!e setting "Setting Name"`
changes your setting to the specified one. It will also give you any additional instructions you need to complete (for those who need a `!bplan`)

**Setting A Library**
`!e public GVAR-ID`
sets the library to the one at the gvar address. This will save the GVAR into a CVAR called `explorelibrary`

`!svar serverepxlorelibrary gvar-id`
creates an svar (server variable) in your server that defaults that entire server to the library at the provided gvar address.

**Resetting Progress**
Players may sometimes need to clear settings as instructed. Do so with `!e clear`

**Writing Libraries**
First, you'll need to create your own gvar. Use this one as your exmaple: `!gvar 6e7a3d5d-9261-435a-9944-c82ce243b4d4`

**Main Features**
- *Map Support*. Follow along the dungeon crawls with a map. As new rooms are discovered the Fog of War is automatically updated.
- *Multiplayer support*. You need to split the party? Sure thing. You can have different payers go different routes on the dungeon crawl. You can view the over all map with `!e map`
- *Traps*. Configure Traps to go off automatically if the players triggering does not have the passive perception to find it. Traps will be active until they are disabled, and the DM issues the `!e award -t name -trap trapname` command  to disable the trpa for good. Save and Attack traps are supported. 
- *Locked Doors*. Some doors will not budge until you have a key, you pick it, or break it down. DM will issue the `!e awatd -t name -key keyname` command to handle keys being acquired by players. Once a door has been unlocked, it will remain unlocked. 
- *Monsters*. You can load monsters upon entering rooms. This requires the monsters to be preloaded in `!bplan` and then E will rename them and place them on the map, rolling for their init automatically. 

Thanks to Cthethan#1175 for writing the original `!explore` Exploration alias which started everything. Thanks to Croebh#5603 and NerdsandDragons#2817 for writing the awesome `!map` Mapping Alias which is awesome. Mahkasad#5996 for writing `!bplan` Battle Planning, and lastly Dr Turtle#1771 for always being there to help me. 