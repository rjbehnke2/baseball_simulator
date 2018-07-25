from pybaseball import batting_stats_range

# retrieve all players' batting stats for the month of May, 2017
data = batting_stats_range("2017-05-01", "2017-05-28")

# retrieve batting stats for only August 24, 2016
#data = batting_stats_range("2016-08-24",)

print(data)
