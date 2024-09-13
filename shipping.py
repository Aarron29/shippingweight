weight = 4.8
cost_ground = ""

#Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 10 + 20
else:
  print("Choose appropriate weight")

print("Total Cost of Shipping $",cost_ground)

  #Premium Shipping

cost_premium = 125.00

print("Cost of Premium Shipping $", cost_premium)

#Drone Shipping

drone_shipping = ""
drone_weight = 4.8

if drone_weight <= 2:
  drone_shipping = drone_weight * 4.50
elif drone_weight > 2 and drone_weight <= 6:
  drone_shipping = drone_weight * 9.00
elif drone_weight > 6 and drone_weight <= 10:
  drone_shipping = drone_weight * 12.00
elif drone_weight > 10:
  drone_shipping = drone_weight * 14.25
else:
  print("Choose appropriate weight")

print("Cost of Drone Shipping $", drone_shipping)