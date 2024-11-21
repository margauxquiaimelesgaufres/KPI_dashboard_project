 # Project : Dashboard for surfers !
As a data analyst, you have been contacted by a Surf School to help them to collect and visualize data relative to the sea conditions. 

They want to have a dashboard in the school showing the best moment to practice surf in the week.

The school is located near to Bordeaux. 

In this area, the best conditions to practice this activity is when the sea generates high waves and the wind speed is strong coming from the North. 

So, you will have to build appropriate KPIs relative to this information.

## Part 1 : Data extraction
School’s instructors use the following webpage to get information about the sea : https://www.surf-report.com/meteo-surf/lacanau-s1043.html
On this webpage for each day (7 days) displayed, you will capture 5 kind of data : - The date (Here : “Samedi 22 Octobre”)
 
 - The time, in the 1st column (example : 08:00)
- The wave size, in the 3rd column : (Vagues : “0.8m - 0.7m”)
- The wind speed (colored number - example : 3km/h)
- The wind direction (the arrow next to the wind speed)

What you have to do :
1) Extract the data
2) Put the extracted data in a dataframe. It should look something like that :
3) Save the dataframe a csv file
4) Create a python library called “surf_scrap”(the user can import with the standard
python import command. In this library there will be only one function. This function
will allow the user to select a specific url (ex : https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html; https://www.surf-report.com/meteo-surf/moliets-plage-centrale-s102799.html).
and save the related dataframe in csv file in the location, he/she wants)
5) Create a python (.py) script allowing to execute the library.


## Part B : Dashboard creation
Congratulations, you should have got the data allowing you to create the dashboard. Now let’s build it.
You will do it using the flexdashboard package in R. This dashboard will have the following features :
- Run the Python script
- Import the dataset just saved after the script run
    
 - Prepare the data allowing to compute KPIs
- Contain only one tab
Your client want the following KPIs in the dashboard :
- One graph containing the wave size (let’s take the mean) over the time
- One graph containing the wind speed over the time
- A table containing the day, the hour, wave size and direction
- A box containing the best moment to practice surf during the coming week
- A box containing the highest wave of the week
- A gauge containing a grade of the sea quality for the best moment to practice.

For this last KPI, you can create your own scale.
We assume that a good wave is up to 1.0m. A wind speed up to 50km/h is ok and should coming from the North (presence of the word “Nord” in the wind direction variable is ok)
Find the best organization for your dashboard. It should be as userfriendly as possible !
