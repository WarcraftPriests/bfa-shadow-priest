# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

1. Each directory has a list of reports in `reports.py` that you want to sim.
2. Create `reports/` and `profiles/` directories within the directory you want to sim.
3. After settings reports, run `python profiles.py` in the given directory you want to generate profiles for.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` sim.py will skip it
6. To run the sims use `python sim.py dir/` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=priest | Out-File 'A:\simc-bfa\priest-traits.txt'
```

## Results
- [talents](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/talents)
- [bulk weights](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/stats)
- [azerite traits](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/azerite-traits)
- [racials](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/racials)
- [consumables](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/consumables)
- [enchants](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/enchants)
- [APL Tests](https://github.com/seanpeters86/bfa-shadow-priest/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)
