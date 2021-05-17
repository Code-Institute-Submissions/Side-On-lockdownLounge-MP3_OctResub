# Milestone Project 3

## Backend Development

### The Lockdown Lounge
Welcome to the Lockdown Lounge! This website forum has been created for you to share some stories or jokes with everybody else bored and stuck inside. The aim of the website is to give people some space to unwind and spent some of that free time looking at how other people have managed to get through it all. 

The users can create their own account and use this to comment on peoples stories or jokes. They can also post their own content is they're logged in. If they're not registered, they will only be allowed to view the content. Not comment or add their own stuff. This is to encourage people coming back to the website. The user can also view their own content on their profile page, along with the account information. 

The website only currently has the basic functionality which allows people to do the above. There are more features which can be added to the website.

### User experience

#### New user coming to the website to browse
The new user will be taken to the index page and there is a small amount of text. As this is only a forum page, I haven't gone for large images or things like that, as it's purely user content based. 
They will be explained what the website is and where to go to find stories and jokes. They'll also be told they need to be signed up to leave comments or content. Links are on the page to take the user to the relevant page.

#### New user wanting to create a story
The user can go to the story page on the navigation bar at the top. If they are a mobile user, there is a burger icon in the top left corner for them to click on and the other pages will show on there. When they get to the page, they will be reminded that they need to register for an account before they can add a story. The Add Story button is only visible to users who have an account and are signed in.

#### New user wanting to comment on a story
As above the user will be told if they want to comment on a story, they'll have to register an account. They can then go to the stories pages and find a story they want to comment on.

#### New user wanting to look at jokes
The user is firstly taken to the home page where the website function is explained. They are given two options to get to the jokes page. They can either click on the jokes anchor tag, or go to the 'Jokes' link found in the navbar. 

#### New user wanting to comment on a joke
This is the same process as the user wanting to comment on a joke. They are told to register an account before doing so and are then able to comment on the joke.

#### New user wanting to add their own joke
Same process as the user wanting to create a story, then will need to go to the joke page after having registered their account.

#### New user wanting to sign in and register an account
This will be made clear is the user wants to add any content to the website. They will be given a link to the register page on each page of the website to make it easier for them to find, it also encourages them to create an account. This page is kept simple and the user only needs to input basic details to create their account.

#### User wanting to look at the stories they've added
This is after the user has signed into their account. They are then shown the Profile navigation tab. They can go onto this page and are taken to the 'Stories' tab which shows all of the stories they've created.

#### User wanting to edit a story they've added
This user can do this by either finding their story and clicking (hover on desktop) on the small green circle. This opens up and there is a yellow icon whih shows a pencil and a square. I chose this icon because it looks like the most comment icon when editing something. The user is then taken to another page for their story and the story title and content fields are pre-populated with the original story contents. They can then click on the edit button and their story will be edited. They will then be taken back to the stories page. 

#### User wanting to edit a joke they've added
This will be done similarly to editing a story. The use can find their own joke either from the Jokes page, or from within their profile page where it lists all of the jokes they've added to the website.

#### User wanting to look at what jokes they've added
This can be found if this user is logged into their account, and go to their profile page. It shows a list of all the jokes they've added, and they can click on each individual one to see if anybody has commented on their post.

#### User wanting to see if they've got a comment on any of their stories or jokes
The user will need to have an account and be signed into it. They can then go to their Profile page and see by what stories and jokes they've added by clicking on the relevant tab. From here, the user can edit or delete their joke or story. 

#### User wants to see other users jokes and stories
The user will need to find a story or joke and then click on a the username of the person they want to see. They will then be taken to a profile of that user, showing all of their content. They can then go into each individual joke or story to leave a comment, if they are signed in.

### Wireframe designs 
All of the wireframes were designed at the start of the project to help me get an idea in my head of what I wanted to aim for. I wanted to create a very simple forum where people could share positive content with each other. The wireframes show both the deskptop and mobile designs. 



### Features
This website is designed to allow users to easily navigate through the different pages to find a joke or story. They are told from their initial visit that they will have to have their own user account set up and signed into before being allowed to add any of their own content. 

#### Account
One of the features is the account set up. Users can choose their own username and password, they are also required to add their own email address. This can later lead on to getting notifications from the website whenever somebody comments on their content.

#### Edit/Delete
User, if they are logged on, can edit or delete their own content from two places: their stories/jokes page and the Profile page. This allows users to have control over their account and content by removing or fixing and comments they've made. They are also able to delete or edit their own comments after they've posted them by finding the comment they wish to change/delete.

#### Posting content
Users, after logging in, can post their own content on either page. Whenever they do so, they can see their content on the relative page.

#### Mobile version
Users using mobile can easily navigate and see the various pages by clicking on the burger icon in the top left of the screen. This is to allow more space on the screen and stop the need to reduce the size of the text.

#### Profile
Users cant look at each others content by clicking on their name found anywhere on the joke, story or comment. This is to open the doors to having your own personal area where others can view and comment on anything else they've created.

### Features left to implement

#### A favourites system
I began trying to implement the favourites system, however unfortunately being realistic with time, I was unable to implement it. The system was there to have a star of similar icon on the story or joke, and allow a user to click it to save it to their favourites. This then would have been added to the database, along with their own personal account ID, to allow them to see it in their own Profile page

#### An 'upvote' system
Similar to the one found on Reddit, the amount of up and down votes would have been shown on the joke or comment itself. This would have fedback to the user within their Profile screen to see if there content is liked or disliked by other users. Working similarly to the favourites system, this will be implemented to add more interaction with the content. 

### Technologies used

flask - used to create templates within the html5, allowing for pages to be generated depending on the action that's taken.
python3 - to create functions allowing the use of linking to mongoDB and to create templates
html5 - to display in a browser
css3 - for styling purposes
JavaScript - used with Materialize to create basic responsive elements within the website.
Materialize - for the basic CSS layouts
Balsamiq - to create wireframes

### Testing

Find here

### Acknowledgements

As this project is mainly focused on the backend programming skills involving databases, I used Materialize to quickly create a basic looking website which then allowed me to create a forum style website. I also looked at websites such as reddit.com and urbandictionary for their simple layouts. 

I used the tutor support on a few occassions as I was having some ificulty in some areas around posting and getting data from the database. 

I also used the basic idea of a mini project I went through within the Code Institute course, mainly the registration and log in feature as it is best suited what I wanted from this website. 

### Code used

All of the code I used I've tailored to suite my needs. I've taken sections of code from the mini project within the course, however manipualted it to suite why I needed my app to do. 

### Deployment

#### 
1. Create a development project folder and navigate to it cd /[folder path]
2. Initialise Git git init
3. Clone the project repository into your local development folder git clone https://github.com/bowets/ms3-crew-dictionary.git
4. Install Python 3
5. Install Pip
6. Create a virtual environment for your local project
7. Install Flask
8. Install PyMongo
9. Install the packages in the requirements.txt file
10. Create an env.py file with the following parameters:
11. IP: 0.0.0.0
12. PORT: 5000
13. MONGO_DBNAME: [name of your database]
14. MONGO_URI: mongodb://<yourdbuser>:<yourdbpassword>@ds225442.mlab.com:25442/<yourdbname>
15. SECRET_KEY: [any string of characters. the longer the better]
16. The project already contains a .gitignore file which contains env.py 9. Run the project python app.py