# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

## Imprtant Links
- [Wiki](https://github.com/seanpeters86/bfa-shadow-priest/wiki)
- [CodeFactor.io](https://www.codefactor.io/repository/github/seanpeters86/bfa-shadow-priest)

## Discussion
- [Discord](https://discord.gg/WarcraftPriests)
- [Website](https://warcraftpriests.com/)

## How to Run

1. Each directory has a list of reports in `reports.py` that you want to sim.
2. Create `reports/` and `profiles/` directories within the directory you want to sim.
3. After creating reports, run `python profiles.py [DA, LotV]` in the given directory you want to generate profiles for.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` sim.py will skip it
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
- DA: SWV_ToF_SC_MB_DA
- LotV: FotM_ToF_SC_MB_LotV

### Azerite Traits
- Head: [Horrific Amalgam's Hood](https://bfa.wowhead.com/item=160616/horrific-amalgams-hood&bonus=4822:1477&azerite-powers=5:404:22:14:13): [Death Throes](https://bfa.wowhead.com/spell=278659/death-throes), [Heed My Call](https://bfa.wowhead.com/spell=271681/heed-my-call), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Shoulders: [Amice of Corrupting Horror](https://bfa.wowhead.com/item=160726/amice-of-corrupting-horror&bonus=4822:1477&azerite-powers=5:236:461:85:13): [Whispers of the Damned](https://bfa.wowhead.com/spell=275726/whispers-of-the-damned), [Earthlink](https://bfa.wowhead.com/spell=279926/earthlink), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- Chest: [Robes of the Unraveler](https://bfa.wowhead.com/item=160614/robes-of-the-unraveler&bonus=4822:1477&azerite-powers=5:405:30:44:13): [Chorus of Insanity](https://bfa.wowhead.com/spell=278661/chorus-of-insanity), [Overwhelming Power](https://bfa.wowhead.com/spell=271705/overwhelming-power), [Azerite Empowered](https://bfa.wowhead.com/spell=263978/azerite-empowered)
- `neck=heart_of_azeroth,id=158075,bonus_id=4929/4930/4936/1536,azerite_level=33`

### Stats - Mythic (Percent Stat - Gear Amount)
- 19.56% Crit - 1048
- 14.04% Haste - 955
- 4.27% Versatility - 363
- 19.00% Mastery - 564
- 7588 Intellect - 4750

### Enchants
- Weapon: [Torrent of Elements](https://bfa.wowhead.com/item=153479/enchant-weapon-torrent-of-elements)
- Ring: [Pact of Haste](https://www.wowhead.com/item=153443/enchant-ring-pact-of-haste)

### Consumables
- Food: [Bountiful Captains Feast](https://bfa.wowhead.com/item=156526/bountiful-captains-feast)

## Results
- [talents](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/stats)
- [azerite traits](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/azerite-traits)
- [racials](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/racials)
- [consumables](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
