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


def ind():
    print('''                 i      index.
                 x      exit
                 c      Celcius to Fahrenheit
                 f      Fahrenheit to Celcius
                 oz     ounces to pounds
                 lboz   pounds to ounces
                 g      grams to lbs
                 pg     pounds to grams
                 lbs    pounds to kilograms
                 kg     kilograms to pounds
                 kl     kilometers to miles
                 mk     miles to kilometers
                 mi     miles per hour to kilometers per hour
                 kph    kilometers per hour to miles per hour   ''')
     

ind()         
print("Enter i for index or x to exit.")
print("Enter m to go back to main menu.")
while True:
    try:
        convert = input("Enter a letter from index  to convert, i for index  m for main menu. ")
        if convert == "c":
            while True:
                print("Enter temperature in Celsius.")
                celsius = input()
                if celsius == "m":
                    break
                result = float(celsius)  / 5 * 9 + 32
                print (result)
                print("Fahrenheit")    
        elif convert == "f":
            while True:
                print("Enter a temperature in Fahrenheit.")
                fahrenheit = input()
                if fahrenheit == "m":
                    break
                result = ((float(fahrenheit)) - 32) * 5 / 9
                print (result)
                print ("Celsious")
        elif convert == "g":
            while True:
                print("Enter a weight in grams.")
                weight_grams = input()
                if weight_grams == "m":
                    break
                weight_lbs = float(weight_grams) *.00220462
                print(weight_lbs)
                print("pounds")
        elif convert == "pg":
            while True:
                print("Enter a weight in pounds.")
                weight_pounds = input()
                if weight_pounds == "m":
                    break
                weight_grams = float(weight_pounds) * 453.59237
                print(weight_grams)
                print("grams")
        elif convert == "lbs":
            while True:
                print("Enter a weight in lbs.")
                weight_lbs = input()
                if weight_lbs == "m":
                    break
                weight_kg = float(weight_lbs) * 0.45359237
                print(weight_kg) 
                print("kilograms")
        elif convert == "kg":
            while True:
                print("Enter a weight in kg.")
                weight_kg = input()
                if weight_kg == "m":
                    break
                weight_lbs = float(weight_kg) * 2.2046226218
                print(weight_lbs)
                print("pounds")
        elif convert == "oz":
            while True:
                print("Enter a weight in ounces.")
                weight_oz = input()
                if weight_oz == "m":
                    break
                weight_lbs = float(weight_oz) * 0.062500
                print(weight_lbs)
                print("pounds")
        elif convert == "lboz":
            while True:
                print("Enter a weight in pounds.")
                weight_lbs = input()
                if weight_lbs == "m":
                    break
                weight_oz = float(weight_lbs) *16
                print(weight_oz)
                print("ounces")
        elif convert == "kl":
            while True:
                print("Enter a distance in kilometers.")
                distance_klm = input()
                if distance_klm == "m":
                    break
                distance_miles = float(distance_klm) * 0.62137119223733
                print (distance_miles)
                print("miles")
        elif convert == "mk":
            while True:
                print("Enter a distance in miles")
                distance_miles = input()
                if distance_miles == "m":
                    break
                distance_kilometers = float(distance_miles) *1.609344
                print(distance_kilometers)
                print("kilometers")
        elif convert == "mi":
            while True:
                print("Enter speed miles per hour.") 
                speed_mph = input()
                if speed_mph == "m":
                    break
                speed_klm = float(speed_mph) * 1.609344
                print(speed_klm)
                print("kilometers per hour")
        elif convert == "kph":
            while True:
                print("Enter a speed in kilometers per hour.")
                speed_kpm = input()
                if speed_kpm == "m":
                    break
                speed_mph = float(speed_kpm) / 1.609344
                print(speed_mph)
                print("Miles per hour")
        elif convert == "i":
            ind()
        elif convert == "x":
            break
        else:
            print("Enter a valid leter from index.")
    except ValueError:
        print("Enter a valid number.")
    except EOFError:
        print("Invalid input.")
  
    
 
            
            
    
        
            
                
   
    
        

 
            

            


            
