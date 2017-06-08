# ml-members-api
Moonclerk Member Information Request Script
==============

This script is used to pull all information related to members (or Plans, as MoonClerk specifies it by default)
--------------

The Moonclerk API only allows 100 requests at a time. The script will pull up to 700 members. If there are more than 700 members then you can change the number on the 
range function. 

Steps:
1. Get your API key from your Moonclerk account
2. Add your API key to the 'Token token' variable on the addheaders function (line 26)
3. Run the Python script