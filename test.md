# Testing

These tests were carried out throughout the development process. I've including what the test was, how it was testing, the result and the fix, if required. I've seperated the different coding languages used as part of the project so it's easier to read.

## HTML

| Test                                          | How                                                                               | Result                                                                             | Fix                                                                                                     | Code used                                        |
| --------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Links to .html pages                          | After creating each link, testing them                                            | LL logo didn't correctly take to the index page                                    | Added correct code to take to the page                                                                  | href="{{ url_for('index') }}"                    |
| form submission for new user                  | creating a new user                                                               | the information wasn't correctly sending to the database                           | There wasn't a method connected to the html code                                                        | method="POST" added into the form element        |
| Button on story/joke                          | View in the browser                                                               | The buttons wren't displaying correctly and would appear above the card itself     | One of the /div" was located in the wrong place and stopping the button from being within the card div. | Had to move the /div futher down the line        |
| Test user input (passwords)                   | creating a new user with a password                                               | password was created, however password could be less than 5 characters             | Added rule to the html code to require more than 5 characters to create a more secure password          | minlength="5"                                    |
| search bar location on both stories and jokes | view in broswer                                                                   | the searchbar was on the left of the screen and the width was longer than the card | I added code in-line with the html to fix the issue and location of the search bar                      | div class="search-bar center" style="width: 50%" |
| length of joke and stories                    | by copying large amounts of text into the relevant section to fix a story or joke | there was only a short space to add the text                                       | increased to limit in the forms                                                                         | maxlength="600",                                 |
| HTML Validator| copy code from HTML pages and check errors|There was an error which showed there were two form elements |Removed the form elements|N/A|
HTML Validator (comments area)| Enter code into the HTML validator|There was an error which said the type="text" wasn't allowed in a textarea element|Removed the type code| N/A

<br>

## CSS

| Test                                   | How                                                           | Result                                                                             | Fix                                                                              | Code used                                |
| -------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------- |
| grid layout taken from Materialize     | testing layout in browser and changing screen resolution size | Layout did not change correctly when the screen was smaller                        | Reviewed grid guidance on documentation, added correct class name to suite needs | class="s12"                              |
| anchor tags                            | look in browser, didn't want them blue and highlighted        | tags were highlighted blue and caused issues with the story and joke cards         | change CSS code to remove the text decoration                                    | text-decoration: none; color: black;     |
| 'created by' text on story/jokes cards | view in browser                                               | the text was appearing within the card, but not in the top left corner as I wanted | add code in css to set the text to the correct location                          | position: absolute; left: 5px; top: 5px; |

<br>

## JavasScript

As the JavaScript was taken from the Materialize responsive design, only parts of the code needed to be changed to suit my needs.

| Test                                              | How                                                                                | Result                                                                                                                | Fix                                                 | Code used                                                            |
| ------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- |
| Location of the function button on the story/joke | consult the documentation from the Materialize page and view my own in the browser | The button was in the correct location, however the other buttons would go upwards instead of to the left as expected | Add code to the js function changing this direction | var instances = M.FloatingActionButton.ini(elems, {direction: 'left' |

<br>

## Python

| Test                                         | How                                 | Result                                                                 | Fix                                                                       | Code used                                                              |
| -------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| home page                                    | check in browser after lauching app | taken to stories page not home page                                    | add code to make index the first page when the website loads              | @app.route("/")                                                        |
| username check                               | creating a story and clicking on it | story went onto new page                                               | took me to the correct story                                              | N/A                                                                    | N/A |
| only show comments associated with the story | creating a comment on the story     | showed all comments associated with all stories                        | add code to story function                                                | story_comment = list(mongo.db.story_comment.find({'story_id': story})) |
| add comment to database                      | create comment                      | comment went into database, however didn't store story/joke Id with it | Add code into the function to recognise the ID and add it to the database | "story_id": mongo.db.stories.find_one({"_id": ObjectId(story_id)}),   |
|user profile displaying the correct user|clicking on a users name|receieved an error saying could not complete URL| added code into the profile functio|    username = mongo.db.users.find_one({"username": username})["username"]<br>I also needed to add: "/profile/<"username"> (ignore the " ")
|||||                                                                        |


#### Validators

[WC3 Validator](https://validator.w3.org/) - All HTML pages were tested. 'Bad Value' errors created by the Jinji code, however there were some errors which have been subsequently fixed, shown in the HTML testing table.

