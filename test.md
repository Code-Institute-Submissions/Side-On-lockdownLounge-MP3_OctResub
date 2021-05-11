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

## CSS

| Test                               | How                                                           | Result                                                                     | Fix                                                                              | Code used                            |
| ---------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------ |
| grid layout taken from Materialize | testing layout in browser and changing screen resolution size | Layout did not change correctly when the screen was smaller                | Reviewed grid guidance on documentation, added correct class name to suite needs | class="s12"                          |
| anchor tags                        | look in browser, didn't want them blue and highlighted        | tags were highlighted blue and caused issues with the story and joke cards | change CSS code to remove the text decoration                                    | text-decoration: none; color: black; |
|                                    |                                                               |                                                                            |                                                                                  |                                      |
|                                    |                                                               |                                                                            |                                                                                  |                                      |
|                                    |                                                               |                                                                            |                                                                                  |                                      |
|                                    |                                                               |                                                                            |                                                                                  |                                      |
|                                    |                                                               |                                                                            |                                                                                  |                                      |

## JavasScript

| Test | How | Result | Fix | Code used |
| ---- | --- | ------ | --- | --------- |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |

## Python

| Test | How | Result | Fix | Code used |
| ---- | --- | ------ | --- | --------- |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
|      |     |        |     |           |
