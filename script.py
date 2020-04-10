def grd_ship(weight,flat=20):
  if weight <=2:
    return (1.50*weight)+flat
  elif weight > 2 and weight < 6:
    return (3.00*weight)+flat
  elif weight > 6 and weight < 10:
    return (4.00*weight)+flat
  elif weight == 'prm':
    return 125
  else:
    return (4.75*weight)+flat

#drone shipping costs
def drn_ship(weight,flat=0):  
  if weight <=2:
    return (4.50*weight)+flat
  elif weight > 2 and weight < 6:
    return (9.00*weight)+flat
  elif weight > 6 and weight < 10:
    return (12.00*weight)+flat
  else:
    return (14.25*weight)+flat

def price_cal(weight):
  if (grd_ship(weight) >= 125.0) or(drn_ship(weight) >=125):
    return "Premium serivce is the best option and it cost 125 $"
 
  elif grd_ship(weight) > drn_ship(weight):
    return "Drone Shipping method is cheaper and it costs you " + str(drn_ship(weight)) + " $"
 
  else:
    return "Ground Shipping method is cheaper and it costs you " + str(grd_ship(weight)) + " $"
  
#TESTIG THE FUNCTION
print(price_cal(4.8)) 
print(price_cal(48))
