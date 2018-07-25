from pybaseball import batting_stats

# get all of this season's batting data so far
#data = batting_stats(2017)

# retrieve data on only players who have 50+ plate appearances this year
#data = batting_stats(2017, qual=50)

# retrieve one row per player per season since 2000 (i.e.: who had the single most dominant season over this period?)
#data = batting_stats(2010, 2016)

# retrieve aggregate player statistics from 2000 to 2016 (i.e.: who had the most home runs overall over this period?)
data = batting_stats(2010, 2016, ind=0)

print(data)
