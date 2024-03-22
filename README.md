
# Welcome to Shloker

Here I will describe the functionality and planned future features of the Shloker application, a simple password manager.

The obvious features like generating a password and saving entries per URL exist in this application
though are limited in certain ways. The initial version only generates a password of 16 characters
containing at least 1 of each:

* lower case character (abc...)
* upper case (ABC...)
* number (123...)

If you choose not to generate a password you can enter your own as well. The copy button to the left of the save button 
will copy whatever is in the password field to the clipboard.

The application prompts for URL of the username and password combination and then writes those entries as json to a 
file. The entries are indexed starting from 0.

## Planned features

Better app security:
* password hashes
* protected password file
* configuration file to set and get from

More password options:
* special characters
* change password character length generated
* 

## Bugs


# Updates
## v0.11
- Clears the entries when saving
- Aligned some widgets

## v0.12
- Added copy to clipboard button
- Refactored some password generation code