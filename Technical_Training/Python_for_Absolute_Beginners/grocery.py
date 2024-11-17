# Variables holding the prices of the six items:
 
pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
# A subtotal is the sum of all prices before any sales taxes or discounts are added.
 
# round() was used to round the subtotal to 2 decimal places since the sum of any amount of numbers that all have 2 
# numbers after the decimal will always have 2 numbers after its decimal point.
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal)