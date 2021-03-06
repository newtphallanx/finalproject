from random import randint
from django.db import models
from __future__ import unicode_literals
#create a character class with necessary attributes                                                                                         
class Character(models.Model):
    name = models.CharField(max_length=20)
    species =models.CharField(max_length=20)
    career =models.CharField(max_length=20)
    specializationTrees= models.CharField(max_length=100)
    soak =models.IntegerField(default=1)
    woundsThreshold= models.IntegerField(default=1)
    woundsCurrent =models.IntegerField(default=1)
    strainThreshold= models.IntegerField(default=1)
    strainCurrent = models.IntegerField(default=1)
    defenseRanged =models.IntegerField(default=1)
    defenseMelee= models.IntegerField(default=1)
    creator =models.CharField(max_length=20)
    brawn =models.IntegerField(default=1)
    agility =models.IntegerField(default=1)
    intellect =models.IntegerField(default=1)
    cunning =models.IntegerField(default=1)
    willpower =models.IntegerField(default=1)
    presence= models.IntegerField(default=1)
    astrogation(Int)= models.IntegerField(default=0)
    athletics(Br)= models.IntegerField(default=0)
    charm(Pr)= models.IntegerField(default=0)
    coercion(Will)= models.IntegerField(default=0)
    computers(Int)= models.IntegerField(default=0)
    cool(Pr)= models.IntegerField(default=0)
    coordination(Ag)= models.IntegerField(default=0)
    deception(Cun)= models.IntegerField(default=0)
    discipline(Will)= models.IntegerField(default=0)
    leadership(Pr)= models.IntegerField(default=0)
    mechanics(Int)= models.IntegerField(default=0)
    medicine(Int)= models.IntegerField(default=0)
    negotiation(Pr)= models.IntegerField(default=0)
    perception(Cun)= models.IntegerField(default=0)
    pilotingPlanetary(Ag) =models.IntegerField(default=0)
    pilotingSpace(Ag)= models.IntegerField(default=0)
    resilience(Br) =models.IntegerField(default=0)
    skulduggery(Cun)= models.IntegerField(default=0)
    stealth(Ag)= models.IntegerField(default=0)
    streetwise(Cun) =models.IntegerField(default=0)
    survival(Cun)= models.IntegerField(default=0)
    vigilance(Will) =models.IntegerField(default=0)
    brawl(Br) =models.IntegerField(default=0)
    gunnery(Ag) =models.IntegerField(default=0)
    melee(Br)= models.IntegerField(default=0)
    rangedLight(Ag) = models.IntegerField(default=0)
    rangedHeavy(Ag) =models.IntegerField(default=0)
    coreWorlds(Int)= models.IntegerField(default=0)
    education(Int)= models.IntegerField(default=0)
    lore(Int)= models.IntegerField(default=0)
    outerRim(Int)= models.IntegerField(default=0)
    underworld(Int)= models.IntegerField(default=0)
    xenology(Int) = models.IntegerField(default=0)),
                #used to make sure that each character is referred to by character name
    def __str__(self):
                    return self.name
                    pass                                                                                            

#now making dice classes, made so whicheverdice.number() returns a string with the correct amount of things
class green(models.Model):
    def d1(self):
        return (0,0,0,0,0,0)     
    def d2(self):
        return (1,0,0,0,0,0)                                
    def d3(self):
        return (1,0,0,0,0,0)
    def d4(self):
        return (2,0,0,0,0,0)
    def d5(self):
        return (0,0,1,0,0,0)
    def d6(self):
        return (0,0,1,0,0,0)
    def d7(self):
        return (1,0,1,0,0,0)
    def d8(self):
        return (0,0,2,0,0,0)

class purple(models.Model):
    def d1(self):
        return (0,0,0,0,0,0)
    def d2(self):
        return (0,1,0,0,0,0)
    def d3(self):
        return (0,2,0,0,0,0)
    def d4(self):
        return (0,0,0,1,0,0)
    def d5(self):
        return (0,0,0,1,0,0)
    def d6(self):
        return (0,0,0,1,0,0)
    def d7(self):
        return (0,0,0,2,0,0)
    def d8(self):
        return (0,1,0,1,0,0)

class yellow(models.Model):
        return (0,0,0,0,0,0)
    def d2(self):
        return (1,0,0,0,0,0)
        def d1(self):
    def d3(self):
        return (1,0,0,0,0,0)
    def d4(self):
        return (2,0,0,0,0,0)
    def d5(self):
        return (2,0,0,0,0,0)
    def d6(self):
        return (0,0,1,0,0,0)
    def d7(self):
        return (1,0,1,0,0,0)
    def d8(self):
        return (1,0,1,0,0,0)
    def d9(self):
        return (1,0,1,0,0,0)
    def d10(self):
        return (0,0,2,0,0,0)
    def d11(self):
        return (0,0,2,0,0,0)
    def d12(self):
        return (0,0,0,0,1,0)

class red(models.Model):
    def d1(self):
        return (0,0,0,0,0,0)
    def d2(self):
        return (0,1,0,0,0,0)
    def d3(self):
        return (0,1,0,0,0,0)
    def d4(self):
        return (0,2,0,0,0,0)
    def d5(self):
        return (0,2,0,0,0,0)
    def d6(self):
        return (0,0,0,1,0,0)
    def d7(self):
        return (0,0,0,1,0,0)
    def d8(self):
        return (0,1,0,1,0,0)
    def d9(self):
        return (0,1,0,1,0,0)
    def d10(self):
        return (0,0,0,2,0,0)
    def d11(self):
        return (0,0,0,2,0,0)
    def d12(self):
        return (0,0,0,0,0,1)

class blue(models.Model):
    def d1(self):
        return (0,0,0,0,0,0)
    def d2(self):
        return (0,0,0,0,0,0)
    def d3(self):
        return (0,0,2,0,0,0)
    def d4(self):
        return (0,0,1,0,0,0)
    def d5(self):
        return (1,0,1,0,0,0)
    def d6(self):
        return (1,0,0,0,0,0)

class black(models.Model):
    def d1(self):
        return (0,0,0,0,0,0)
    def d2(self):
        return (0,0,0,0,0,0)
    def d3(self):
        return (0,1,0,0,0,0)
    def d4(self):
        return (0,1,0,0,0,0)
    def d5(self):
        return (0,0,0,1,0,0)
    def d6(self):
        return (0,0,0,1,0,0)

#now make a dice model with aggregate() and diceNumber() and rollEachdice()
class dice(models.Model):
    #I will just copy this code for each roll and then change the necessary things so the comments will be duplicated
    def rollGreen(self, G):
        #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = green.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = green.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = green.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = green.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = green.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = green.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 7:
                r = green.d7()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 8:
                r = green.d8()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    def rollPurple(self, G):
                #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = purple.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = purple.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = purple.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = purple.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = purple.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = purple.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 7:
                r = purple.d7()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 8:
                r = purple.d8()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    def rollYellow(self, G):
        #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = yellow.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = yellow.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = yellow.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = yellow.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = yellow.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = yellow.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 7:
                r = yellow.d7()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 8:
                r = yellow.d8()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 9:
                r = yellow.d9()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 10:
                r = yellow.d10()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 11:
                r = yellow.d11()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 12:
                r = yellow.d12()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    def rollRed(self, G):
        #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = red.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = red.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = red.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = red.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = red.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = red.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 7:
                r = red.d7()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 8:
                r = red.d8()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 9:
                r = red.d9()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 10:
                r = red.d10()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 11:
                r = red.d11()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 12:
                r = red.d12()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    def rollBlue(self, G):
        #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = blue.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = blue.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = blue.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = blue.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = blue.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = blue.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    def rollBlack(self, G):
        #first have a while loop to count down
        result = (0,0,0,0,0,0)
        keepGoing = True
        number = G
        int(number) = number
        while keepGoing:
            #number is the determining variable for when the while loop ends
            number = number - 1
            a = randint(1,8)
            #the reason to have both dice and rollDice is that it is more elegant an will allow me to do stuff with just the dice if I wish, instead of having to go into the if statements
            #if statements are really the only way to do this since there isn't a pattern to these dice, but I do know that a bunch of if statements aren't ideal
            if a == 1:
                r = black.d1()
                #adds result to whatever the dice result was
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 2:
                r = black.d2()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 3:
                r = black.d3()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 4:
                r = black.d4()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 5:
                r = black.d5()
                for i in range(6):
                    result[i] = result [i] + r[i]
            elif a == 6:
                r = black.d6()
                for i in range(6):
                    result[i] = result [i] + r[i]
            #stops the while loop and returns result
            if number == 0:
                keepGoing = False
                return result

    #will take name and skill, figure out which character is being referred to, figure out which characteristic is connected to the skill, and then calculate the number of dice needed(green= absoluteValue(characteristicNumber-skillNumber), if characteristicNumber > skillNumber then yellow = characteristicNumber - green, if skillNumber > characteristicNumber then yellow = skillNumber - green ), then returns a string with (green, Yellow)
    def greenNumber(self, name, skill):
        #takes the name passed to it and checks if there is a character with that name using django's filtering
        skill = skill
        c = Character.objects.filter(name = name)
        skillNumber = c.skill
        #I have to use a slightly awkward method of determining the characteristic as there is no better way to do so that I could think of
        if "(Br)" in skill:
            characteristicNumber = c.brawn
        elif "(Ag)" in skill:
            characteristicNumber = c.agility
        elif "(Cun)" in skill:
            characteristicNumber = c.cunning
        elif "(Int)" in skill:
            characteristicNumber = c.intellect
        elif "(Will)" in skill:
            characteristicNumber = c.willpower
        elif "(Pr)" in skill:
            characteristicNumber = c.presence
        green = abs(characteristicNumber - skillNumber)
        if characteristicNumber > skillNumber:
            yellow = characteristicNumber - green
        elif skillNumber > characteristicNumber:
            yellow = skillNumber - green
        return green

    def yellowNumber(self, name, skill):
        #takes the name passed to it and checks if there is a character with that name using django's filtering
        skill = skill
        c = Character.objects.filter(name = name)
        skillNumber = c.skill
        #I have to use a slightly awkward method of determining the characteristic as there is no better way to do so that I could think of
        if "(Br)" in skill:
            characteristicNumber = c.brawn
        elif "(Ag)" in skill:
            characteristicNumber = c.agility
        elif "(Cun)" in skill:
            characteristicNumber = c.cunning
        elif "(Int)" in skill:
            characteristicNumber = c.intellect
        elif "(Will)" in skill:
            characteristicNumber = c.willpower
        elif "(Pr)" in skill:
            characteristicNumber = c.presence
        green = abs(characteristicNumber - skillNumber)
        if characteristicNumber > skillNumber:
            yellow = characteristicNumber - green
        elif skillNumber > characteristicNumber:
            yellow = skillNumber - green
        return (yellow)

    #now to make the final function, aggregate. It will take input from several places and roll them and cancel the results and return an array with 4 objects
    def aggregate(self, name, skill, difficulty, red, blue, black):
        resultTotal = (0,0,0,0,0,0)
        #get each of the results
        g = greenNumber(name, skill)
        gResult = rollGreen(g)
        y = yellowNumber(name, skill)
        yResult = rollYellow(y)
        p = difficulty - red
        pResult = rollPurple(p)
        rResult = rollRed(red)
        blu = rollBlue(blue)
        bla = rollBlack(black)

        #add results together
        for i in range(6):
            resultTotal[i] = resultTotal[i] + gResult[i] + yResult[i] + pResult[i] + rResult[i] + blu[i] + bla[i]

        #cancel results
        cancelSuccess = resultTotal[0] - resultTotal[1] + resultTotal[4] - resultTotal[5]
        cancelAdvantage = resultTotal[2] + resultTotal[3]
        triumphs = resultTotal[4]
        despairs = resultTotal[5]
        realResult = (cancelSuccess, cancelAdvantage, triumphs, despairs)
        #return results
        return(realResult)

class diceResults(models.Model)
    results = CharField(max_length = 20)
