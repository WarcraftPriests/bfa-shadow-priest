# BfA Shadow Priest Sims

This repo includes scripts and sims for shadow priests.

1. Each directory has a list of reports in `reports.py` that you want to sim.
2. Create `reports/` and `profiles/` directories within the directory you want to sim.
3. After settings reports, run `python profiles.py` in the given directory you want to generate profiles for.
4. After profiles are generated create `settings.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` sim.py will skip it
6. To run the sims use `python sim.py dir/` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=priest
```

## Results
- [talents](https://docs.google.com/spreadsheets/d/1KG77iYgMBnWpYEaSKfTR1Fh3_WEh8FB3jQDUUSY5Im4/edit?usp=sharing)
- [bulk weights](https://docs.google.com/spreadsheets/d/1cP_9mOss69hTSYrp7DOELdDwRFbaEhHt_P5yjOmmAaQ/edit?usp=sharing)
