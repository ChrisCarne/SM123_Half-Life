import math
import numpy as np
import matplotlib.pyplot as plt

#Functions############################################################################################

#Calculates the amount of substance remaining given the half_life (tau), initial amount(p0) and time(t)
def amount_left(tau, p_nought, time):
    return  p_nought*np.exp(-math.log(2)*time/tau)
  
#Calculates the amount of substance needed for 5 grams to be left after 30 seconds given the half_life (tau)
def amount_needed(tau):
     return 5*np.exp(math.log(2)*30/tau)
     
# Returns a tuple of numpy arrays for the x and y values to use in drawing graphs
def build_time_series(half_life,p_nought, max_time):
    x = np.linspace(0,max_time) # x values 
    y = amount_left(half_life, p_nought, x) #y value
    return (x,y) #returns (x axis values,y axis values)
    
# Output list of isotopes studied, tweaked to get punctuation right (yes I am that sad).
# There's probably a better way to do it but this works so...
def do_iso_string(isotopes):
    iso_string = "" #initialise a string that will be the list of isotope names
    for n in range(len(isotopes)):
        if n < len(isotopes)-2: #if the isotope is not the second to last in the list
            iso_string += isotopes[n][0]+", " #then add the isotope name and a comma to the string
        elif n==len(isotopes)-2: #else if the isotope is the second to last in the list
            iso_string+=isotopes[n][0]+" and " #then add the isotope name and an 'and' to the string
        else:
            iso_string += isotopes[n][0]+"." #else we're at the end, add the name and a full stop  to the string
    return iso_string

#Builds a graph for decay of isotope over time.
def do_graph(time_series,isotope_name):
    x, y = time_series
    plt.title("Decay of " + isotope_name +" over time")
    plt.plot(x, y)

#Returns a tuple of inputted and calculated isotope data
def get_input():
    isotope_name=input("Please enter the name of the isotope");
    half_life=float(input("Please enter the half-life of the isotope in seconds"))
    p_nought = float(input("Please enter the initial amount in grams"))
    time=float(input("Please enter a time in seconds"))
    max_time=10
    time_series=build_time_series(half_life, p_nought, max_time )
    return(isotope_name,half_life,p_nought,time,time_series )
  
###################################################################################################

isotopes=[] #Initialise a list to keep isotope data in

#Note: the isoptope data is held in a list of tuples ie 
#[(name_1,half_life 1, p_nought_1,time_1,time_series_1),...,(name_n,half_life n, p_nought_n,time_n,time_series_n)]

#Main loop to process each isotope
while True:
  data=get_input() # Gets a tuple of the isotope data
  isotope_name, half_life,p_nought,time,time_series= data #Unpacks the tuple
  amount_remaining=amount_left(half_life,p_nought,time) #Calculates the amount left at the given time
  start_amount = amount_needed(half_life)  # Calculates the starting amount.
  isotopes.append((isotope_name,half_life,p_nought,time,time_series))#Builds the list used in doing the final graph
    #output stuff
  print ""
  print "Starting with", p_nought, "grams of",isotope_name, "after", time, "seconds there will be", round(amount_remaining, 2), "grams remaining \n"
  print "In order to have 5 grams left after 30 seconds you should start with", round(start_amount, 2), "grams \n"
  # stop or go again
  if input("Do you want to do another isotope y/n")=="n":
    print ""
    break
  else: 
    print ""

#Process the isotope list and do the graph
#Just iterates through the list, decomposes the element tuple and calls do_graph() for each element

iso_string=do_iso_string(isotopes) # String of isotope names

plt.clf()
for isotope in isotopes: #iterate through the list of isotopes
  name, half_life,p_nought,time,time_series = isotope #Unpack the tuple into its components
  do_graph(time_series,name)
plt.title("Decay over time of " + iso_string)
plt.show()

#Prints the list of isotopes studied
print "Isotopes studied:", iso_string


  
