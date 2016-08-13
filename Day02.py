mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

totalMealCost = mealCost + (tipPercent+taxPercent )/100*mealCost

#print("The total meal cost is %f" % totalMealCost)
print("The total meal cost is %d dollars." % round(totalMealCost))