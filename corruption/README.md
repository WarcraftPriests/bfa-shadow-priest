# Corruption Results
The following results have two sets of sims, one is raw DPS and the other takes
that raw DPS and divides it by the amount of corruption that specific effect is
worth/costs. The second result attempts to value DPS per point of corruption.

All sims are done with 475 gear, certain effects scale with ilvl and will vary
relative to the ilvl of that piece.

## Disclaimers

### Surging Vitality
The Versatility proc trait sim is done by attempting to proc the trait every 1s.
This will vary extremely based on the damage you take and how often you take it,
and this sim is more or less a best case scenario for this trait. If you want to
sim this yourself at different intervals you can check [the SimC wiki](https://github.com/simulationcraft/simc/wiki/ExpansionOptions#83---visions-of-nzoth--options) or edit
it yourself with `bfa.surging_vitality_damage_taken_period=X`. In raidbots you
just need to change the drop down for Surging Vitality to a certain percentage
of buff uptime.

## Raids

### SWV_ToF_AS_LI_LotV
- [DPS](Results_AS.md)
- [DPS per Corruption](Corruption_Value_Results_AS.md)

### SWV_ToF_SC_LI_LotV
- [DPS](Results_SC.md)
- [DPS per Corruption](Corruption_Value_Results_SC.md)

## Dungeons

### SWV_DV_AS_LI_LotV
- [DPS](Results_Dungeons_AS.md)
- [DPS per Corruption](Corruption_Value_Results_Dungeons_AS.md)

### SWV_DV_SC_LI_LotV
- [DPS](Results_Dungeons_SC.md)
- [DPS per Corruption](Corruption_Value_Results_Dungeons_SC.md)
