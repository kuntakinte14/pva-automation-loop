# pva-automation-loop

This project contains the python script that loops through mock account data, calling the account creation script with individual account 
data values. The mock account data is pulled from a file called data1.csv contained in a data subdirectory (e.g., "data/data1.csv")

Features of the script:
- wait time setting to add delay between each call to the account creation script
- specify an email address to send notifications to
- logging to a local file logs.txt
- renames the data file when completely processed
