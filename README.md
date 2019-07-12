# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

## Important Links
- [Wiki](https://github.com/WarcraftPriests/bfa-shadow-priest/wiki)
- [APL 101](https://github.com/WarcraftPriests/bfa-shadow-priest/wiki/APLs-101)
- [Glossary of Terms](https://github.com/WarcraftPriests/bfa-shadow-priest/wiki/Glossary)
- [CodeFactor.io](https://www.codefactor.io/repository/github/warcraftpriests/bfa-shadow-priest)
- [Dungeon sims courtesy of Hero Damage](https://www.herodamage.com)

## Discussion
- [Discord](https://discord.gg/WarcraftPriests)
- [Website](https://warcraftpriests.com/)

## How to Run
All scripts are run with python3. If you are using Windows you will likely need to change references in `sim.py` from `python3` to `python`.

1. Run `pip install -r requirements.txt` in order for `analyze.py` to work
2. Validate the default lists of reports in `reports.py` are what you want to sim.
3. Run `python profiles.py dir/ --talents [AS, SC]` for the directory you want to sim.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` or if the weight in `weights.py` is 0, sim.py will skip it
6. To run the sims use `python sim.py dir/ [--iterations X, --weights, --talents [AS, SC]]` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=priest | Out-File 'A:\simc\priest-traits.txt'
```

## Base Actor Information
All sims are run with the following as a base (unless specified otherwise)

### Talent Combos
Every sim is run with the top AS and SC build:
### Raids
- AS: SWV_ToF_AS_LI_LotV
- SC: SWV_ToF_SC_LI_LotV
### Dungeons
- AS: SWV_DV_AS_LI_LotV
- SC: SWV_DV_SC_LI_LotV

### Azerite Traits
- Head: [Handmaiden's Cowl of Sacrifice](https://www.wowhead.com/item=168336?bonus=4775&azerite-powers=5:403:405:30:13&ilvl=450)
    - [Spiteful Apparitions](https://www.wowhead.com/spell=277682/spiteful-apparitions)
    - [Chorus of Insanity](https://www.wowhead.com/spell=278661/chorus-of-insanity)
    - [Overwhelming Power](https://bfa.wowhead.com/spell=271705/overwhelming-power)
- Shoulders: [Mantle of Ceremonial Ascension](https://www.wowhead.com/item=158344/mantle-of-ceremonial-ascension&bonus=4817:1512&azerite-powers=5)
    - [Chorus of Insanity](https://www.wowhead.com/spell=278661/chorus-of-insanity)
    - [Spiteful Apparitions](https://www.wowhead.com/spell=277682/spiteful-apparitions)
    - [Elemental Whirl](https://www.wowhead.com/spell=263984/elemental-whirl)
- Chest: [Vestments of Creeping Terror](https://www.wowhead.com/item=168337?bonus=4775&azerite-powers=5:405:236:30:13&ilvl=450)
    - [Chorus of Insanity](https://www.wowhead.com/spell=278661/chorus-of-insanity)
    - [Whispers of the Damned](https://www.wowhead.com/spell=275722/whispers-of-the-damned)
    - [Overwhelming Power](https://bfa.wowhead.com/spell=271705/overwhelming-power)
- `neck=heart_of_azeroth,id=158075,bonus_id=4929/5814/4936/1600,azerite_level=65`

### Stats - Mythic (Percent Stat - Gear Amount)
- 27.31% Crit - 1606
- 29.03% Haste - 1881
- 0.00% Versatility - 0
- 15.02% Mastery - 325
- 10422 Intellect - 7137

### Enchants
- Weapon: [Quick Navigation](https://www.wowhead.com/spell=268894/weapon-enchant-quick-navigation)
- Ring: [Accord of Haste](https://www.wowhead.com/item=168447/enchant-ring-accord-of-haste)

### Consumables
- Food: [Baked Port Tato](https://www.wowhead.com/item=168313/baked-port-tato)
- Potion: [Potion of Unbridled Fury](https://www.wowhead.com/item=169299/potion-of-unbridled-fury)
- Flask: [Greater Flask of Endless Fathoms](https://www.wowhead.com/item=168652/greater-flask-of-endless-fathoms)
- Augment Rune: [Battle-Scarred Augment Rune](https://www.wowhead.com/item=160053/battle-scarred-augment-rune)

## Results
- [talents](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/stats)
- [essences](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/essences)
- [azerite traits](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-traits)
- [azerite gear](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-gear)
- [racials](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/racials)
- [special-gear](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/essences)
- [consumables](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
