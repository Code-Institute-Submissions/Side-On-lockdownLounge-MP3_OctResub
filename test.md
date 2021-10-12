# Testing

All testing was completed while working on the website. Each of the tests were performed in-line with the user stories to make sure the website is working as expected. 

<br>

Below are screenshots of the testing process, showing was was testing and the result. 

<br>

## 1. New user coming to the website 

This is the first page the user is shown when they go to the site. The screenshot on the left is the mobile version, which shows a burger icon on the top left which, when clicked, will show the links to the other pages.

![Home Page]()

## 2. Adding a story

Users can add a story once they are signed into an account. The buttons on the home page and story page change depending on whether the user is signed in. If they are, they are able to see the add story button, located on the story page, as well as the add story link on the navigation bar.

![Add a story]()

## 3 Editing a story

The icons to edit user stories and jokes are only visible to the user who created them. Testing has also been done to stop other users from being able to edit somebody elses story or joke.

![Editing a story]()

## 4 Deleting a story

The icons to edit user stories and jokes are only visible to the user who created them. Testing has also been done to stop other users from being able to edit somebody elses story or joke.

![Deleting a story]()

## 5. Commenting on a story

Similar to the add story button, the comment button only appears if the user is signed in. They are able to comment on the story.

![Comment on a story]()

## 6 Adding a joke

This works the same as the adding a joke page. Worth noting that this has been tested to stop people who aren't logged in, copying the add joke/joke url, and bypassing the feature.

![Adding a joke]()

## 7 Editing a joke

The icons to edit user jokes are only visible to the user who created them. Testing has also been done to stop other users from being able to edit somebody elses joke.

![Editing a joke]()

## 8 Deleting a joke

The icon to delete user jokes are only visible to the user who created them. Testing has also been done to stop other users from being able to delete somebody elses joke.

![Deleting a joke]()

## 9 Comment on a joke 

The user is able to comment on a joke, if they are logged in. After the comment is added, they stay on the same page.

![Comment on a joke]()

## 10 Editing a comment

The icons to edit user comments are only visible to the user who created them. Testing has also been done to stop other users from being able to edit somebody elses comment.

![Editing a comment]()

## 11 Deleting a comment

The icons to delete user comments are only visible to the user who created them. Testing has also been done to stop other users from being able to delete somebody elses comment.

![Deleting a comment]()

## 11. Register

This page allows users to create their own account using an email and choosing their own username. It tells them what they can do, once they've created an account.

![Register an account]()

## 11. Log in

Once the user has an account, they can log in on this page.

![Log in to account]()

## 13. Looking at own user stories and jokes

This page can be accessed when the user is logged into their account. It shows all of their jokes and stories, and they are able to edit and delete from from here, without having to find them again on the website.

![Look at own user stories and jokes]()

## 14. See other user stories and jokes
Page shows other user stories and jokes after clicking on their username anywhere on the website.

![Other user stories and jokes]()


## 11 See other users jokes and stories



#### Validators
To ensure all code uses correct syntax and doesnt 

[WC3 Validator](https://validator.w3.org/) - All HTML pages were tested. 'Bad Value' errors created by the Jinji code, however there were some errors which have been subsequently fixed, shown in the HTML testing table.

[Python Validator](http://pep8online.com/) - Copied app.py code into the validator and passed tests. There were some indentations to fix initally. Fixed this and tested again and it passed.

[CSS Validator](https://jigsaw.w3.org/css-validator/) - css stylesheet code was copied into the validator. There were two errors, one was 'line-break: 20px', this was written in error and removed. The other was a border style which is no longer used.

[JavaScript Validator](https://jshint.com/) - Passed code into the validator. The errors shown were undefined variables '$', this is used with jquery and appears to not be recognised by the validator.
