#Hammurabi

import random

def print_intro():
    print '''Congrats, you are the newest ruler of ancient Samaria, elected for a
    ten year term of office. Your duties are to distribute food, direct
    farming, and buy and sell land as needed to support your people.
    Watch out for rat infestations and the resultant plague! Grain is
    the general currency, measured in bushels. The following will help
    you in your decisions:

    * Each person needs at least 20 bushels of grain per year to survive.
    * Each person can farm at most 10 acres of land.
    * It takes 2 bushels of grain to farm an acre of land.
    * The market price for land 
uctuates yearly.

    Rule wisely and you will be showered with appreciation at the end of your term. Rule poorly and you will be kicked out of office!'''

    print
    
def Hammurabi():

    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000 
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    net_bushels = harvest + bushels_in_storage - rats_ate
    
    print_intro()

    for i in range(1,11):
        print "O great Hammurabi!"
        print "You are in year", i,"of your ten year rule."
        print "In the previous year", starved, "people starved to death."  
        print "In the previous year", immigrants, "people entered the kingdom."
        print "The population is now", population,"." 
        print "We harvested", harvest, "bushels at", bushels_per_acre, "bushels per acre."
        print "Rats destroyed", rats_ate, "bushels, leaving", bushels_in_storage, "bushels in storage."
        print "The city owns", acres_owned, "acres of land."
        print "Land is currently worth", cost_per_acre, "bushels per acre."
        print "There were",plague_deaths, "deaths from the plague."
        print 
        
        land_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        if land_bought == 0:
            land_sold = ask_to_sell_land(acres_owned)
        bushels_feed = ask_to_feed(net_bushels)
        land_planting = ask_to_cultivate(acres_owned, population, net_bushels)

        acres_owned = acres_owned + land_bought #- land_sold
        net_bushels = net_bushels - bushels_feed
        harvest = land_planting*bushels_per_acre
        
        isPlague()
        if "true":
            population == population*0.5
            population == plague_deaths 

        new_starved = numStarving(population, net_bushels)
        if starved > .45*population:
            print "you've failed"
        starved = starved + new_starved 

        new_immigrants = numImmigrants(acres_owned, net_bushels, population, starved)
        immigrants = immigrants + new_immigrants
        
        bushels_per_acre = getHarvest()

        infest_rate = doRatsInfest()
        rats_ate = infest_rate * net_bushels
        
        cost_per_acre = priceOfLand()
        
    print_summmary(starved, acres_owned)

def ask_to_buy_land(bushels, cost):
    '''Ask user how many bushels to spend buying land'''
    acres = input("How many acres will you buy? ")
    while acres * cost > bushels:
            print "O great Hammurabi, we have but", bushels, "bushels of grain!"
            acres = input("How many acres will you buy? ")
    return acres
    
def ask_to_sell_land(acres):
    '''Ask user how many acres to sell'''
    acres_sell = input("How many acres will you sell? ")
    while acres_sell > acres:
            print "O great Hammurabi, we have but", acres, "acres!"
            acres_sell = input("How many acres will you sell? ")
    return acres_sell

def ask_to_feed(bushels):
    '''Ask user how many bushels they want to use for feeding.'''
    feed = input("How many bushes will you use for feeding? ")
    while feed > bushels:
        print "O great Hammurabi, we have but", bushels, "bushels of grain!"
        feed = input("How many bushes will you use for feeding? ")
    return feed

def ask_to_cultivate(acres, population, bushels):
    '''Ask user how much land they want to plant seed in'''
    land_plant = input("How much land will you use for planting? ")
    while land_plant > acres:
        print "O great Hammurabi, we have but", acres, "acres of land!"
        land_plant = input("How much land will you use for planting? ")
    while land_plant < 5:
        print "O great Hammurabi, we have", population, "people and only", bushels, "bushels for feed!"
        land_plant = input("How much land will you use for planting? ")
    return land_plant

def isPlague():
    '''Determines if there will be a plague'''
    var = random.randint(1,100)
    if var < 15: 
        return "true" 
    if var > 15:
        return "false" 
    
def numStarving(population, bushels):
    '''Calculates the number of starving'''
    starved = max[(population - (bushels/20)), 0]
    return starved

def numImmigrants(land, grainInStorage, population, numStarving):
    '''Calculates the number of immigrants'''
    if numStarving > 0:
        return 0
    if numStarving <= 0:
        return (20 * land + grainInStorage)/[(100 * population) + 1]

def getHarvest():
    '''Calculates the harvest'''
    var = random.randint(1,8)
    return var

def doRatsInfest():
    '''Determines if rats will infest'''
    var = random.randint(1,100)
    if var < 40:
        return random.random(.1-.3)
        
def priceOfLand():
    '''Calculates the price of land'''
    price = random.randint(16, 22)
    return price

def print_summmary(starved, land):
    print "Congrats, you did a great job! Under your rule, only",
    starved, "people starved, and you ended up with a total of", acres,
    "acres."

Hammurabi()
