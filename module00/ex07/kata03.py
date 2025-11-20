# Put this at the top of your kata03.py file
kata = "The right format"

print("-" * (42-len(kata)), kata, sep ="", end = "")


#  python3 kata03.py | cat -e
# --------------------------The right format%
# $> python3 kata03.py | wc -c
# 42