# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print(*(f"{x} was created by {y}" for x,y in kata.items()), sep = "\n")

# python3 kata01.py
# Python was created by Guido van Rossum
# Ruby was created by Yukihiro Matsumoto
# PHP was created by Rasmus Lerdor