# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

## Imprtant Links
- [Wiki](https://github.com/seanpeters86/bfa-shadow-priest/wiki)
- [CodeFactor.io](https://www.codefactor.io/repository/github/seanpeters86/bfa-shadow-priest)

## Discussion
- [Discord](https://discord.gg/WarcraftPriests)
- [Website](https://warcraftpriests.com/)

## How to Run
All scripts are run with python3. If you are using Windows you will likely need to change references in `sim.py` from `python3` to `python`.

1. Run `pip install -r requirements.txt` in order for `analyze.py` to work
2. Validate the default lists of reports in `reports.py` are what you want to sim.
3. Run `python profiles.py dir/ [DA, LotV]` for the directory you want to sim.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` or if the weight in `weights.py` is 0, sim.py will skip it
6. To run the sims use `python sim.py dir/ [--iterations X, --weights, --talents [DA, LotV]]` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=priest | Out-File 'A:\simc-bfa\priest-traits.txt'
```

## Base Actor Information
All sims are run with the following as a base (unless specified otherwise)

### Talent Combos
Every sim is run with the top DA and LotV build:
- DA: FotM_ToF_SC_MB_DA
- LotV: FotM_ToF_SC_MB_LotV

### Azerite Traits
- Head: [Horrific Amalgam's Hood](https://bfa.wowhead.com/item=160616/horrific-amalgams-hood&bonus=4822:1477&azerite-powers=5:404:22:14:13): [Death Throes](https://bfa.wowhead.com/spell=278659/death-throes), [Heed My Call](https://bfa.wowhead.com/spell=271681/heed-my-call), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Shoulders: [Mantle of Contained Corruption](https://www.wowhead.com/item=160613/mantle-of-contained-corruption&bonus=4822:1477): [Archive of the Titans](https://www.wowhead.com/spell=280709/archive-of-the-titans), [Unstable Flames](https://www.wowhead.com/spell=279902/unstable-flames), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Chest: [Robes of the Unraveler](https://bfa.wowhead.com/item=160614/robes-of-the-unraveler&bonus=4822:1477&azerite-powers=5:405:30:44:13): [Archive of the Titans](https://www.wowhead.com/spell=280709/archive-of-the-titans), [Overwhelming Power](https://bfa.wowhead.com/spell=271705/overwhelming-power), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- `neck=heart_of_azeroth,id=158075,bonus_id=4929/4930/4936/1536,azerite_level=33`

### Stats - Mythic (Percent Stat - Gear Amount) - DA
- 20.13% Crit - 1089
- 17.90% Haste - 1217
- 1.52% Versatility - 129
- 21.97% Mastery - 742
- 7169 Intellect - 5123

### Stats - Mythic (Percent Stat - Gear Amount) - LotV
- 20.28% Crit - 1172
- 16.54% Haste - 1125
- 2.15% Versatility - 183
- 21.22% Mastery - 697
- 7169 Intellect - 5123

### Enchants
- Weapon: [Torrent of Elements](https://bfa.wowhead.com/item=153479/enchant-weapon-torrent-of-elements)
- Ring: [Pact of Haste](https://www.wowhead.com/item=153443/enchant-ring-pact-of-haste)

### Consumables
- Food: [Bountiful Captains Feast](https://bfa.wowhead.com/item=156526/bountiful-captains-feast)

## Results
- [talents](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/stats)
- [azerite traits](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/azerite-traits)
- [azerite gear](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/azerite-gear)
- [racials](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/racials)
- [consumables](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
