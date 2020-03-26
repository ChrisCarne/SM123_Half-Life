import math
import numpy as np
import matplotlib.pyplot as plt

#uncomment for use in jupyter notebook
%matplotlib inline 

# functions #############################################################################################

# Calculates the amount of substance remaining given half_life, initial amount and time
def amount_left(tau, p_nought, time):
    return p_nought*np.exp(-math.log(2)*time/tau)

# Calculates the amount of substance needed for 5 grams to be left after 30 seconds given the half_life
def amount_needed(tau):
    return 5*np.exp(math.log(2)*30/tau)

# Returns a tuple of numpy arrays for the x and y values to use in drawing graphs
def build_time_series(half_life,p_nought, max_time):
    x_array = np.linspace(0,max_time)
    return (x_array, amount_left(half_life, p_nought, x_array)) #returns (x axis values,y axis values)
    
# Output list of isotopes studied, tweak to get commas right (yes I am that sad).
def do_iso_string(istopes):
  iso_string = ""
  for n in range(len(isotopes)):
      if n < len(isotopes)-2:
          iso_string += isotopes[n][0]+", "
      elif n==len(isotopes)-2:
          iso_string+=isotopes[n][0]+" and "
      else:
          iso_string += isotopes[n][0]+"."
  return iso_string

#Builds a graph for decay of isotope over time.  
#Trinket doesn't seem to allow legends which is a pain. Also y-axis labelling dowsnt work properly in trinket
def do_graph(time_series, name):
    x,y=time_series
    plt.plot(x, y, label=name)
    plt.title("Decay of " + name +" over time", fontweight="bold") #fontweight crashes trinket p2
    plt.xlabel("time /s")
    plt.ylabel("Amount remaining /g")

# Helper function to return a tuple of inputted isotope data
def get_input():
    isotope_name = input("Please enter the name of the isotope ")
    half_life = float(input("Please enter the half-life of the isotope in seconds "))
    p_nought = float(input("Please enter the initial amount in grams "))
    time = float(input("Please enter a time in seconds "))
    max_time=10
    time_series=build_time_series(half_life, p_nought, max_time)
    return(isotope_name,half_life,p_nought,time,time_series )

####################################################################################################

# Initialise list to keep isotope data in
isotopes = []

# Loop to process each isotope
while True:
    data = get_input()  # Puts the info entered by teh user in a variable
    isotope, half_life, p_nought, time, time_series = data  # Pulls out the pieces from the variable
    p = amount_left(half_life, p_nought, time) # Calculates the amount left at the given time
    start_amount = amount_needed(half_life)  # Calculates the starting amount.
    isotopes.append([isotope, half_life, p_nought, time, time_series]) # puts the entered data in a list 
    # Print out some stuff
    print("")
    print(f"Starting with {p_nought} grams of {isotope} after {time} seconds there will be {round(p, 2)} grams remaining")
    print(f"In order to have 5 grams left after 30 seconds you should start with {round(start_amount, 2)} grams")
    print("")
    # Go round again or finish up
    if input("Do you want to do another isotope y/n") == "n":
        print("")
        break
    else:
        print("")
        
#Process the final list and do the graphs
max_time=10  #using the time specified in the exercise
for isotope in isotopes:
  name, *other_stuff, time_series = isotope #Decomposes the tuple into its bits
  do_graph(time_series, name)
plt.title("Decay of all isotopes studied over time", fontweight="bold")
plt.legend()
plt.show()

#iso_string=do_iso_string(istopes)
#print "Istopes studied" do_iso_string(isotopes)
print(f"Isotopes studied : {do_iso_string(isotopes)}")
