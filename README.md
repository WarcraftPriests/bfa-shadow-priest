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
3. Run `python profiles.py dir/ --talents [DA, LotV]` for the directory you want to sim.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` or if the weight in `weights.py` is 0, sim.py will skip it
6. To run the sims use `python sim.py dir/ [--iterations X, --weights, --talents [DA, LotV]]` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=priest | Out-File 'A:\simc\priest-traits.txt'
```

## Base Actor Information
All sims are run with the following as a base (unless specified otherwise)

### Talent Combos
Every sim is run with the top DA and LotV build:
### Raids
- DA: FotM_ToF_AS_LI_DA
- LotV: FotM_ToF_AS_LI_LotV
### Dungeons
- DA: SWV_DV_SC_LI_DA
- LotV: SWV_DV_SC_LI_LotV

### Azerite Traits
- Head: [Cowl of Tideborne Omens](https://www.wowhead.com/item=165822/cowl-of-tideborne-omens&bonus=4822:1507)
    - [Thought Harvester](https://bfa.wowhead.com/spell=288340/thought-harvester)
    - [Searing Dialogue](https://www.wowhead.com/spell=272788/searing-dialogue)
    - [Overwhelming Power](https://bfa.wowhead.com/spell=271705/overwhelming-power)
    - [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Shoulders: [Bristling Fur-Lined Amice](https://www.wowhead.com/item=165922/bristling-fur-lined-amice&bonus=4822:1507)
    - [Chorus of Insanity](https://www.wowhead.com/spell=278661/chorus-of-insanity)
    - [Spiteful Apparitions](https://www.wowhead.com/spell=277682/spiteful-apparitions)
    - [Azerite Globules](https://www.wowhead.com/spell=266936/azerite-globules)
    - [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Chest: [Divine Fury Raiment](https://www.wowhead.com/item=165834/divine-fury-raiment&bonus=4822:1507&azerite-powers=5)
    - [Chorus of Insanity](https://www.wowhead.com/spell=278661/chorus-of-insanity)
    - [Treacherous Covenant](https://www.wowhead.com/spell=289014/treacherous-covenant)
    - [On My Way](https://www.wowhead.com/spell=267879/on-my-way)
    - [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- `neck=heart_of_azeroth,id=158075,bonus_id=4929/4930/4936/1566,azerite_level=48`

### Stats - Mythic (Percent Stat - Gear Amount)
- 20.13% Crit - 1089
- 17.90% Haste - 1217
- 1.52% Versatility - 129
- 21.97% Mastery - 742
- 7169 Intellect - 5123

### Enchants
- Weapon: [Quick Navigation](https://www.wowhead.com/spell=268894/weapon-enchant-quick-navigation)
- Ring: [Pact of Haste](https://www.wowhead.com/item=153443/enchant-ring-pact-of-haste)

### Consumables
- Food: [Bountiful Captains Feast](https://bfa.wowhead.com/item=156526/bountiful-captains-feast)
- Potion: [Potion of Rising Death](https://www.wowhead.com/item=152559/potion-of-rising-death)
- Flask: [Flask of Endless Fathoms](https://www.wowhead.com/item=152639/flask-of-endless-fathoms)
- Augment Rune: [Battle-Scarred Augment Rune](https://www.wowhead.com/item=160053/battle-scarred-augment-rune)

## Results
- [talents](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/stats)
- [azerite traits](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-traits)
- [azerite gear](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-gear)
- [azerite ilvls](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-trait-ilvls)
- [reorigination array](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/azerite-traits-ra)
- [racials](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/racials)
- [consumables](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/WarcraftPriests/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
