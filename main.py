import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl(misc_mpl_mods=False)

###############################################################################
# Load the race session.

race = fastf1.get_session(2023, "Azerbaijan", 'R')
race.load()

###############################################################################
# Get all the laps for a single driver.
# Filter out slow laps as they distort the graph axis.

driver_laps = race.laps.pick_driver("ALO").pick_quicklaps().reset_index()
print(driver_laps)