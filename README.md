# MakerLabs Moonclerk API
Moonclerk Member Information Request Script
==============

This script is used to pull all information related to members/customers (or Plans, as MoonClerk specifies it by default)
--------------

The Moonclerk API only allows 100 requests at a time. The script will pull up to 700 members. If there are more than 700 members then you can change the number on the 
range function. All active, cancelled, pending and other plans are pulled using this script. 

2 important variables related to the API: count and offset. Count is the number of plans that are pulled at once, and offset is the starting position of the set. So if you want to pull 50 customers, then count is 50.
If you want to pull customers numbered 50-100, then offset is 50 and count is 50. 

Steps:
1. Get your API key from your Moonclerk account
2. Add your API key to the 'Token token' variable on the addheaders function (line 26)
3. Run the Python script

By default the files will be saved on the same directory as the script as customer_json[fileNumber].txt where fileNumber is the index number. 

**You have to remove the brackets in the begining and the end of the txt file before converting the JSON to CSV**

I used https://json-csv.com/ to convert the JSON to CRV file, and then upload it to Google Sheets to turn it into a spreadsheet. 