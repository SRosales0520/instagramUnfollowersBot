# instagramUnfollowersBot
This project was originally created so that i could get a list of everyone i followed that didnt follow me back on instagram 
instead of having to search for each individual user but i thought i would add the functionality to be able to do it for 
other users and have it automatically send that person an email with a list of their "unfollowers". This project uses python
as well as selenium(https://selenium.dev/) and a chromedriver to automate google chrome to do what ever we want! i learned how
to code about half of it using this youtube video(https://www.youtube.com/watch?v=d2GBO_QjRlo) by Code Drip but i added functionality so that you could make it do its thing for other users as well as be able to have it automatically email them without you having to do much

prerequisites:
1. Have vscode, virtualenv, python 3, and pip installed and set up already
2. Create a random gmail account and a instagram account so that you don't have to use 
   your personal accounts for this bot

INSTRUCTIONS:
1. go to https://chromedriver.chromium.org and download the right chrome driver that corresponds with your version of chrome and your OS

2. add the filepath of the chromedriver to the system PATH variable for windows or paths file for mac (you can google how to do this)

2. open whichever python file you want to use (with or without email functionality) in visual studio code and open up a terminal in vscode for it

3. Follow what the comments say to change on lines 74, 76, and 128. This should get you to change the code so that it uses the credentials of the gmail account and the instagram account that you want it to use. If you are using the script without email functionality than you will only follow the comment on line 65!

3. create and activate a virtual environment for the folder that the file is in using virtualenv

4. run "pip install selenium" to get what is required to work with the chrome driver

5. run the python file via the terminal in vscode!


PS: you should be able to google how to set up and use selenium and the chromedriver if anything is confusing but if i have missed anything in the instructions, if you have any questions, or you feel i should add somethething, you can 
contact me via email at samuelbrosales@gmail.com!
