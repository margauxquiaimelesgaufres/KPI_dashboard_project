#Importing packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import os
import validators

def Scrap_Weather(link, save_path):
    
    """
    This function scraps the link provided by the user, 
    puts the important scrapped information into a dataframe and saves it into a .csv file into the path
    also provided by the user.
    
    """
    
    
    ###Inputs Validation:###
    
    
    # Check if URL is valid
    if not validators.url(link):
        print("Invalid URL")
        return False
    
    # Check if path exists 
    if not os.path.isdir(os.path.dirname(save_path)):
        print("Invalid file path or directory does not exist.")
        return False

    # Getting HTML from webpage
    url = link
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Finding all tables
    forecast_tab = soup.findAll('div', class_="forecast-tab")
    #putting all the dates in one list
    dates=[]
    for d in forecast_tab:
        dat= d.find('div', class_="title").text.strip()
        dates.append(dat)
        

    #this loop enters 1 table at a time, gets all the html related to each variable.
    #For each variable, we get the html related to all its values in a table at first.
    #Then we append the table information into 1 bigger list to get the html related to all the values of the var in all the tables.
    #the output variables are lists of lists.
    All_Wav=[]
    All_Wind=[]
    All_direx=[]
    All_H=[]
    for d in forecast_tab:
        
        ho= d.findAll('div', class_="cell date with-border")
        All_H.append(ho)
        wav= d.findAll('div', class_= "cell large waves with-border")
        All_Wav.append(wav)
        win= d.findAll('div', class_= re.compile(r'wind wind-color-\d+'))
        All_Wind.append(win)
        wind_dir= d.findAll("div", class_= "wind img")
        All_direx.append(wind_dir)
        

    # Get text about hours from the according html block:
    Hours= []
    for H in All_H:
        Hour_t=[]
        for h in H: 
            Hour_t.append(h.text.strip())
        Hours.append(Hour_t)
    # Get text about waves length from the according html block: 
    Waves= []
    for H in All_Wav:
        Waves_l=[]
        for w in H: 
            Waves_l.append(w.text.strip())
        Waves.append(Waves_l)
        
    # Get text about wind speed from the according html block:  
    Wind_=[]
    for H in All_Wind:
        wind_l=[]
        for w in H: 
            wind_l.append(w.text.strip())
        Wind_.append(wind_l)
    # Get text about wind direction from the according html block:
    Direx=[]
    for T in All_direx:
        dire_l=[]
        for l in T: 
            dire_l.append(l.find('img').get('alt').split('vent ')[1])
            
        Direx.append(dire_l)
    # Create a list with all data combined to be used as 
    combined_data = [Hours, Waves, Wind_, Direx]

    #Creating a new list to store the repeated dates
    repeated_dates = []

    # For each list, we're appending the dates to `repeated_dates`
    for i, lst in enumerate(combined_data[0]):  # Using one of the lists to get the correct date repetitions
        # Repeat the date value as many times as the length of each chunk
        repeated_dates.extend([dates[i]] * len(lst))

    # Define the column names
    column_names = ["Hour", "Waves_Size", "Wind_Speed", "Wind_Direction"]

    #Adding the df to be filled
    df = pd.DataFrame()
    df['Date'] = repeated_dates

    # Populate the DataFrame with the lists
    for i, lst in enumerate(combined_data):
        # Flatten each list of lists and add it as a column with the custom name
        df[column_names[i]] = [item for sublist in lst for item in sublist]

    # Display the DataFrame
    #print(df)
    df.to_csv(f'{save_path}\\Surfing_Data.csv')

