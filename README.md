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
- [talents](https://docs.google.com/spreadsheets/d/1KG77iYgMBnWpYEaSKfTR1Fh3_WEh8FB3jQDUUSY5Im4/edit?usp=sharing)
- [bulk weights](https://docs.google.com/spreadsheets/d/1cP_9mOss69hTSYrp7DOELdDwRFbaEhHt_P5yjOmmAaQ/edit?usp=sharing)
- [azerite traits](https://docs.google.com/spreadsheets/d/1N1WAUhSFh96S-W3rLqvJJenzIhns7FiONV7G4M7zWIc/edit?usp=sharing)
- [racials](https://docs.google.com/spreadsheets/d/1OBwalI1I3I-hiVtvT1Khe3e9Zx-4ukN1llA0EbPPg7I/edit?usp=sharing)
- [consumables](https://docs.google.com/spreadsheets/d/1vPeHRUBw8BeYRp25GRKAmdV7qvPs081sQTe_qIiPsbI/edit?usp=sharing)
- [enchants](https://docs.google.com/spreadsheets/d/1rxQETXpLDykysRiSPwIZmXa6L0UtkRs-VMZbduO2qAQ/edit?usp=sharing)
