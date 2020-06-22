# Reddit User Analysis Web Application
# www.redditor.tk
## Data Sourcing Backend Scripts/DB creation: Mooaz Nasir
## Flask Webapp, Frontend queries/Data Visualizations: Utsav Goswami
## Tech Stack
 - Python
 - Flask
 - PRAW
 - PostgreSQL
 - Matplotlib 
 - HTML 
 - CSS 
 - Jinja
 - Bootstrap
 - Heroku 
 - ElephantSQL
## Analyzes user behavior and how similar comments are on certain posts on the social media platform Reddit. Database used is PostgreSQL and data stored on a server using ElephantSQL.

# How to Use
## Data Insertion
Necessary components:
  1. You must have access to a database (whether it's local or hosted on AWS/Azure).
  2. You should have an IDE/text editor that can run python.
  3. You must have a Reddit account. You can make one which is free. Once you do that, visit https://old.reddit.com/prefs and click the        button on the page that says 'apps'. Next, create an application by clicking the "are you a developer? create an app" button. Give your application a name and select script from the 3 boxes. Give it a short              description and have the about url/redirect url be anything you want. This could be anything (in our case it was the link to the            website). ![Picture](https://i.ibb.co/f9xyM4S/Capture.png). Once you click create app, take note of the personal use script at the          code at the top along with the secret code. You will need these for PRAW. 
  
  
![Picture](https://i.ibb.co/pfDnNMn/Capture.png) 

Above, you should see your specific tokens. Take note of the smaller one (on top) and the longer token below it.

(I deleted this app don't worry!)


Simply create a file called DBCredentials and paste appropriate content. This will vary depending on the hosting service you choose. Next, create a RedditCredentials file. The first line should be the smaller code you saved and the second line should be the secret.
From here, open up all of the files and run them in this order. First run getbestsubreddit, then getTotalComments, then getTopPostFromBestSub, then getTopComment, then getSimilarComments, and lastly getTop10Comments. You can repeat the process as many times as you want (making sure to increase the count of the index's in the files). 

## Webapp
Method 1: Open www.redditor.tk

Method 2:
1. Download project using git or zip file
2. Open up app.py on an IDE/text editor that can run Python/Flask apps
3. Press run and go to the local IP listed on the console 

