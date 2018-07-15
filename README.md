# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

## Documentation
All documentation can be found in the [Wiki](https://github.com/seanpeters86/bfa-shadow-priest/wiki).

## Discussion
- [Discord](https://discord.gg/0f1Ta8lT8xZbLkBV)
- [Website](https://howtopriest.com/)

## How to Run

1. Each directory has a list of reports in `reports.py` that you want to sim.
2. Create `reports/` and `profiles/` directories within the directory you want to sim.
3. After settings reports, run `python profiles.py` in the given directory you want to generate profiles for.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` sim.py will skip it
6. To run the sims use `python sim.py dir/ [--iterations X]` where `dir/` is the sim directory you want to sim

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
- Head: Horrific Amalgam's Hood: Death Throes, Heed My Call, Azerite Empowered
- Shoulders: Amice of Corrupting Horror: Whispers of the Damned, Earthlink, Azerite Empowered
- Chest: Robes of the Unraveler: Chorus of Insanity, Overwhelming Power, Azerite Empowered

### Stats - Mythic (Percent Stat - Gear Amount)
- 19.56% Crit - 1048
- 14.04% Haste - 955
- 4.27% Versatility - 363
- 19.00% Mastery - 564
- 7588 Intellect - 4750

### Enchants
- Weapon: Torrent of Elements
- Ring: TBD

### Consumables
- Food: Bountiful Captains Feast

## Results
- [talents](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/stats)
- [azerite traits](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/azerite-traits)
- [racials](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/racials)
- [consumables](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
