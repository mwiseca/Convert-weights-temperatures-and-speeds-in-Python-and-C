#MIT License

#Copyright (c) 2021-2026 Mitchell E Wise

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


def choices():
    print('''    
                 ch     choices
                 x      exit
                 c      Celcius to Fahrenheit
                 f      Fahrenheit to celcius
                 oz     ounces to pounds
                 lboz   pounds to ounces
                 g      grams to lbs
                 pg     pounds to grams
                 lbs    pounds to kilograms
                 kg     kilograms to pounds
                 kl     kilometers to miles
                 mk     miles to kilometers
                 mi     miles per hour to kilometers per hour
                 kph    kilometers per hour to miles per hour
                 hx     decimal to hexadecimal
                 lm     light years to miles             ''')
    return ""


def celcius():
    while True:
        try:
            print("Enter temperature in Celsius.")
            celsius = input()
            if celsius == "m":
                return "" 
            result = float(celsius)  / 5 * 9 + 32
            print (result)
            print("Fahrenheit") 
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")

def fahrenheit():
    while True:
        try:
            print("Enter a temperature in Fahrenheit.")
            fahrenheit = input()
            if fahrenheit == "m":
                return ""
            result = ((float(fahrenheit)) - 32) * 5 / 9
            print (result)
            print ("Celsious")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")    


def ounces():
    while True:
        try:
            print("Enter a weight in ounces.")
            weight_oz = input()
            if weight_oz == "m":
                return ""
            weight_lbs = float(weight_oz) * 0.062500
            print(weight_lbs)
            print("pounds")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")

def pounds():
    while True:
        try:
            print("Enter a weight in pounds.")
            weight_lbs = input()
            if weight_lbs == "m":
                return ""
            weight_oz = float(weight_lbs) *16
            print(weight_oz)
            print("ounces")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")
    

def grams_lbs():
    while True:
        try:
            print("Enter a weight in grams.")
            weight_grams = input()
            if weight_grams == "m":
                return ""
            weight_lbs = float(weight_grams) *.00220462
            print(weight_lbs)
            print("pounds")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def pounds_grams():
    while True:
        try:
            print("Enter a weight in pounds.")
            weight_pounds = input()
            if weight_pounds == "m":
                return ""
            weight_grams = float(weight_pounds) * 453.59237
            print(weight_grams)
            print("grams")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")
            
            
def pounds_kilograms():
    while True:
        try:
            print("Enter a weight in lbs.")
            weight_lbs = input()
            if weight_lbs == "m":
                return ""
            weight_kg = float(weight_lbs) * 0.45359237
            print(weight_kg) 
            print("kilograms")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def kilograms_pounds():
    while True:
        try:
            print("Enter a weight in kg.")
            weight_kg = input()
            if weight_kg == "m":
                return ""
            weight_lbs = float(weight_kg) * 2.2046226218
            print(weight_lbs)
            print("pounds")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def kilo_miles():
    while True:
        try:
            print("Enter a distance in kilometers.")
            distance_klm = input()
            if distance_klm == "m":
                return ""
            distance_miles = float(distance_klm) * 0.62137119223733
            print (distance_miles)
            print("miles")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def miles_kilometers():
    while True:
        try:
            print("Enter a distance in miles")
            distance_miles = input()
            if distance_miles == "m":
                return ""
            distance_kilometers = float(distance_miles) *1.609344
            print(distance_kilometers)
            print("kilometers")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def miles_kilo():
    while True:
        try:
            print("Enter speed miles per hour.")
            speed_mph = input()
            if speed_mph == "m":
                return ""
            speed_klm = float(speed_mph) * 1.609344
            print(speed_klm)
            print("kilometers per hour")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def kph_to_mph():
    while True:
        try:
            print("Enter a speed in kilometers per hour.")
            speed_kpm = input()
            if speed_kpm == "m":
                return ""
            speed_mph = float(speed_kpm) / 1.609344
            print(speed_mph)
            print("Miles per hour")
        except ValueError:
            print("\nEnter a valid number.\n")
        except EOFError:
            print("\nInvalid input.\n")


def dec_hex():
    while True:
        try:
            a = input("Enter a number m for main to exit.\n")
            if a == "m":
                return ""
            a = int(a)
            result = hex(a)
            print(f"\n{result}\n")
            result = hex(a) [2:]
            print(f"{result}\n")
        except ValueError:
            print("\nEnter a number only.\n")
        except EOFError:
            print("\nInvalid input.\n")


def light_years():
    while True:
        try:
            LightYears = input("Enter a distance in light years.\n")
            if LightYears == "m":
                return ""
            result = float(LightYears) * 5878628192999.1
            print(f"{result}\nmiles\n")
        except ValueError:
            print("\nEnter a number only.\n")
        except EOFError:
            print("\nInvalid input.\n")


functions = {
        "ch": choices,
        "c": celcius,
        "f": fahrenheit,
        "oz": ounces,
        "lboz": pounds,
        "g": grams_lbs,
        "pg": pounds_grams,
        "lbs": pounds_kilograms,
        "kg": kilograms_pounds,
        "kl": kilo_miles,
        "mk": miles_kilometers, 
        "mi": miles_kilo,
        "kph": kph_to_mph,
        "hx": dec_hex,
        "lm": light_years
}


choices()
while True:
    try:
        print("Enter m for main ch for choices x to exit.")
        switch = input()
        if switch == "x":
            break
        (functions[switch]())
    except KeyError:
        print("Enter a selection from choices.\n")
    except EOFError:
        print("Invalid input.\n")


