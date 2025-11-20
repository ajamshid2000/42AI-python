# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
kata0 = "{:02}".format(kata[0])
kata1 = "{:02}".format(kata[1])
kata2 = "{:2f}".format(kata[2])
kata3 = "{:.2e}".format(kata[3])
kata4 = "{:.2e}".format(kata[4])
print("module_"+kata0+", "+"ex_"+kata1+" : "+kata2+", "+kata3+", "+kata4)
print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {kata[2]:2f}, {kata[3]:.2e}, {kata[4]:.2e}")

# $> python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# $> python3 kata04.py | cut -c 10,18
# ,: