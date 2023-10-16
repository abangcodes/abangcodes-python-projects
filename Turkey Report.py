#1-4 Creating Variables
country_name = "Türkiye"
city_name = "Istanbul"
pop_1927 = 691000
pop_2017 = 15029231
unique_stat = "fifth largest city in the world"
growth_stat1 = "enormous growth"
growth_stat2 = "one of the world's 10 fastest growing metropolitan areas"

#5-7 Using variables to perform calculations
pop_change = pop_2017 - pop_1927
percentage_gr = ((pop_change)/pop_1927) * 100
yrs_elapsed1 = 2017 - 1927
yrs_elapsed2 = 2000 - 1950
annual_gr = percentage_gr / yrs_elapsed1

#8-12 Writing a function
def population_growth(yr_1, yr_2, pop_1, pop_2):
  growth_rate = (((pop_2 - pop_1) / pop_1) * 100) / (yr_2 - yr_1)
  return growth_rate

#13 Calling a function - print variable
#print (round(annual_gr , 2))

#14 Calling a function - set one
set_one = round(population_growth(1927, 2017, 691000, 15029231) , 2)
#print (set_one)

#15 Calling a function - set two
set_two = round(population_growth(1950, 2000, 983000, 8831800))
#print (set_two)

#16 Türkiye Report
intro = city_name + " in " + country_name + " is the " + unique_stat + ". It has experienced " + growth_stat1 + " over the years and is " + growth_stat2 + "."
body1 = " In the year 1927, the population of " + city_name + " only had about " + str(pop_1927) + " inhabitants. " + str(yrs_elapsed1) + " years later, in the year 2017, its population had balooned to " + str(pop_2017) + " inhabitants - a " + str(set_one) + " percent growth rate."
body2 = " Interestingly, between the " + str(yrs_elapsed2) + " year period of 1950-2000, the growth rate had only been about " + str(set_two) + " percent."
report = intro + body1 + body2
print(report)

