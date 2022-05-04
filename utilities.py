"""
Wei Ching Lim

This file contains functions to both perform calculation and visualizing data
of private industries contribution to GDP on 2019 to 2020.
The functions include graphs that: 
    (i) compares the entire private industries in 2019-2020,
    (ii) compares Q1, Q2, Q3 and Q4 of each/individual private industry for year 2019 and year 2020 ,
    (iii) visualizes the performance of each industry by its quarter eg. Q1 of 2019, Q2 of 2020 etc. .

"""
import pandas as pd
import matplotlib.pyplot as plt

def Industry():
    """
    This function sums up all the different categories for each quarter of years 2019 to 2020.
    The results obtained is the total percent change contributed to GDP by all the private industries.
    A bar chart will be saved as png file.
    Used in main.py at def both_years(self):
    """
    dict = {'Private Industries': str, '2019_Q1': float, '2019_Q2': float, '2019_Q3': float, '2019_Q4':float , '2020_Q1': float, '2020_Q2': float , '2020_Q3': float, '2020_Q4': float}
    df = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    d = df.dtypes
    df.astype(d)
    df.loc['Total'] = df.sum()
    df2 = df.iloc[-1]
    df2 = df2.to_dict()

    quarter = list(df2.keys())
    percent = list(df2.values())
    
    fig = plt.figure(figsize = (8, 5))   
    plt.bar(quarter, percent, color = 'royalblue')
    plt.grid(fig, axis='y')
    plt.xlabel("Quarter")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Year 2019-2020")
    plt.savefig('totalIndustry.png', dpi = 100, bbox_inches='tight')

def Industry2019():
    """
    This function will plot the percent change contributed to GDP for all categories in the private industry.
    It will plot for all four quarters in 2019.
    A line chart will be saved as png file.
    Used in main.py at def tot_2019(self):
    """
    dict = {'Private Industries': str, '2019_Q1': float, '2019_Q2': float, '2019_Q3': float, '2019_Q4':float }
    df3 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df3.reset_index(level=0, inplace=True)
    d = df3.dtypes
    df3.astype(d)
    df2019 = df3.iloc[:, 0:5]       
    df4 = pd.DataFrame(df2019, columns = ['Private Industries', '2019_Q1', '2019_Q2', '2019_Q3', '2019_Q4'])
    x = list(df4["Private Industries"])
    yQ1 = list(df4["2019_Q1"])
    yQ2 = list(df4["2019_Q2"])
    yQ3 = list(df4["2019_Q3"])
    yQ4 = list(df4["2019_Q4"])
    
    fig = plt.figure(figsize = (10,3))    
    plt.plot(x, yQ1, color = 'blue', label="Quarter 1")
    plt.plot(x, yQ2, color = 'red', label="Quarter 2")
    plt.plot(x, yQ3, color = 'orange', label="Quarter 3")
    plt.plot(x, yQ4, color = 'green', label="Quarter 4")
    plt.legend(loc='upper right')  
    plt.xticks(rotation = 90)
    plt.grid(fig, 'both') 
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 1 to Quarter 4 - Year 2019")
    plt.savefig('ind2019.png', dpi = 100, bbox_inches='tight')
    
def Industry2020():
    """
    This function will plot the percent change contributed to GDP for all categories in the private industry.
    It will plot for all four quarters in 2020.
    A line chart will be saved as png file.
    Used in main.py at def tot_2020(self):
    """
    dict = {'Private Industries': str, '2020_Q1': float, '2020_Q2': float, '2020_Q3': float, '2020_Q4':float }
    df4 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df4.reset_index(level=0, inplace=True)
    d = df4.dtypes
    df4.astype(d)
    df2020 = df4.iloc[:, 5:9]        
    df5 = pd.DataFrame(df2020, columns = ['Private Industries', '2020_Q1', '2020_Q2', '2020_Q3', '2020_Q4'])
    x = list(df4["Private Industries"])
    yQ1 = list(df4["2020_Q1"])
    yQ2 = list(df4["2020_Q2"])
    yQ3 = list(df4["2020_Q3"])
    yQ4 = list(df4["2020_Q4"])   
    
    fig = plt.figure(figsize = (10,3))    
    plt.plot(x, yQ1, color = 'blue', label="Quarter 1")
    plt.plot(x, yQ2, color = 'red', label="Quarter 2")
    plt.plot(x, yQ3, color = 'orange', label="Quarter 3")
    plt.plot(x, yQ4, color = 'green', label="Quarter 4")
    plt.legend(loc='upper left')
    plt.xticks(rotation = 90)
    plt.grid(fig, 'both')  
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 1 to Quarter 4 - Year 2020")
    plt.savefig('ind2020.png', dpi = 100, bbox_inches='tight')

def Ind2019_Q1():
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 1 of year 2019.
    A bar chart will be saved as png file.
    Used in main.py at def q1_2019(self):
    """
    dict = {'Private Industries': str, '2019_Q1': float}
    df6 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df6.reset_index(level=0, inplace=True)
    d = df6.dtypes
    df6.astype(d)
    df2019 = df6.iloc[:, 0:2]
    df7 = pd.DataFrame(df2019, columns = ['Private Industries', '2019_Q1'])
    x = list(df7["Private Industries"])
    y = list(df7["2019_Q1"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'limegreen')
    plt.grid(axis='y')
    plt.xticks(rotation = 90) 
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 1 - Year 2019")
    plt.savefig('ind2019_Q1.png', dpi = 100, bbox_inches='tight')

def Ind2019_Q2(): 
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 2 of year 2019.
    A bar chart will be saved as png file.
    Used in main.py at def q2_2019(self):
    """
    dict = {'Private Industries': str, '2019_Q2': float}
    df8 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df8.reset_index(level=0, inplace=True)
    d = df8.dtypes
    df8.astype(d)
    df2019 = df8.iloc[:, 0:3]
    df9 = pd.DataFrame(df2019, columns = ['Private Industries', '2019_Q2'])
    x = list(df9["Private Industries"])
    y = list(df9["2019_Q2"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'mediumturquoise')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 2 - Year 2019")
    plt.savefig('ind2019_Q2.png', dpi = 100, bbox_inches='tight')
    
def Ind2019_Q3(): 
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 3 of year 2019.
    A bar chart will be saved as png file.
    Used in main.py at def q3_2019(self):
    """
    dict = {'Private Industries': str, '2019_Q3': float}
    df10 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df10.reset_index(level=0, inplace=True)
    d = df10.dtypes
    df10.astype(d)
    df2019 = df10.iloc[:, 0:4]
    df11 = pd.DataFrame(df2019, columns = ['Private Industries', '2019_Q3'])
    x = list(df11["Private Industries"])
    y = list(df11["2019_Q3"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'dodgerblue')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 3 - Year 2019")
    plt.savefig('ind2019_Q3.png', dpi = 100, bbox_inches='tight')
    
def Ind2019_Q4():
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 4 of year 2019.
    A bar chart will be saved as png file.
    Used in main.py at def q4_2019(self):
    """
    dict = {'Private Industries': str, '2019_Q4': float}
    df12 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df12.reset_index(level=0, inplace=True)
    d = df12.dtypes
    df12.astype(d)
    df2019 = df12.iloc[:, 0:5]
    df13 = pd.DataFrame(df2019, columns = ['Private Industries', '2019_Q4'])
    x = list(df13["Private Industries"])
    y = list(df13["2019_Q4"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'mediumpurple')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 4 - Year 2019")
    plt.savefig('ind2019_Q4.png', dpi = 100, bbox_inches='tight')
    
def Ind2020_Q1(): 
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 1 of year 2020.
    A bar chart will be saved as png file.
    Used in main.py at def q1_2020(self):
    """
    dict = {'Private Industries': str, '2020_Q1': float}
    df14 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df14.reset_index(level=0, inplace=True)
    d = df14.dtypes
    df14.astype(d)
    df2020 = df14.iloc[:, 0:6]
    df15 = pd.DataFrame(df2020, columns = ['Private Industries', '2020_Q1'])
    x = list(df15["Private Industries"])
    y = list(df15["2020_Q1"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'darkorange')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 1 - Year 2020")
    plt.savefig('ind2020_Q1.png', dpi = 100, bbox_inches='tight')    

def Ind2020_Q2(): 
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 2 of year 2020.
    A bar chart will be saved as png file.
    Used in main.py at def q2_2020(self):
    """
    dict = {'Private Industries': str, '2020_Q2': float}
    df16 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df16.reset_index(level=0, inplace=True)
    d = df16.dtypes
    df16.astype(d)
    df2020 = df16.iloc[:, 0:7]
    df17 = pd.DataFrame(df2020, columns = ['Private Industries', '2020_Q2'])
    x = list(df17["Private Industries"])
    y = list(df17["2020_Q2"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'gold')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 2 - Year 2020")
    plt.savefig('ind2020_Q2.png', dpi = 100, bbox_inches='tight')    
    
def Ind2020_Q3():
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 3 of year 2020.
    A bar chart will be saved as png file.
    Used in main.py at def q3_2020(self):
    """
    dict = {'Private Industries': str, '2020_Q3': float}
    df18 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df18.reset_index(level=0, inplace=True)
    d = df18.dtypes
    df18.astype(d)
    df2020 = df18.iloc[:, 0:8]
    df19 = pd.DataFrame(df2020, columns = ['Private Industries', '2020_Q3'])
    x = list(df19["Private Industries"])
    y = list(df19["2020_Q3"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'hotpink')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 3 - Year 2020")
    plt.savefig('ind2020_Q3.png', dpi = 100, bbox_inches='tight') 
       
def Ind2020_Q4():
    """
    This function will plot the percent change contributed to GDP 
    for all categories in the private industry only during Quarter 4 of year 2020.
    A bar chart will be saved as png file.
    Used in main.py at def q4_2020(self):
    """
    dict = {'Private Industries': str, '2020_Q4': float}
    df20 = pd.read_csv('gdpdata.csv', index_col=0, dtype=dict)
    df20.reset_index(level=0, inplace=True)
    d = df20.dtypes
    df20.astype(d)
    df2020 = df20.iloc[:, 0:9]
    df21 = pd.DataFrame(df2020, columns = ['Private Industries', '2020_Q4'])
    x = list(df21["Private Industries"])
    y = list(df21["2020_Q4"])
    
    fig = plt.figure(figsize = (10,3))   
    plt.bar(x, y, color = 'firebrick')
    plt.grid(axis='y')
    plt.xticks(rotation = 90)    
    plt.xlabel("Private Industries")
    plt.ylabel("Percent Change to GDP")
    plt.title("Private Industries Percent Change to GDP in Quarter 4 - Year 2020")
    plt.savefig('ind2020_Q4.png', dpi = 100, bbox_inches='tight') 
