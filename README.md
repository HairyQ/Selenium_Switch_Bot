# Welcome to my Selenium Switch Bot!

## No, we're not talking about silly network switches...
We're talking Nintendo Switches here! 

With the COVID pandemic still ongoing, factories that make essential parts / provide essential materials for the Nintendo Switch are(were) operating at limited capacity, while millions are stuck at home over summer with nothing to do. 

Ultimately, this has created a severe shortage in Nintendo Switch consoles - online and in-store retailers sell out within minutes as people flood stores and bots flood the online market. Bots were(are) being used to purchase as many consoles at a time as possible, so their creators can sell them at nearly double price on Amazon and eBay. 

The competition is ruthless, but my own bot has a much simpler, much more innocent goal: To purchase a single Nintendo Switch console for myself. Once this task is completed (or something weird goes wrong...), the bot closes itself and stops executing.

After hours of tinkering, waiting, failing, and trying again, I finally helped my bot achieved its final form. I am now the proud owner of a Nintendo Switch :D

## Note before continuing
At the time of uploading this to github, my bot still appears to execute well on the BestBuy website. As websites change, it is likely that at some point in the future this bot won't execute - I don't have plans to update it, as it has already achieved its goal.

## Prerequisites
* This bot can only be used in Linux
* Selenium_switch_bot.py makes use of Selenium, which will need to be installed on your machine. Selenium (as I use it in the file) also makes use of two other tools:
  * Firefox browser
  * Firefox browser web driver - You can find the up-to-date geckodriver file here: https://github.com/mozilla/geckodriver/releases (This will need to be placed in the folder the bot is run from)
* This bot only operates on the BestBuy website
  * To use the bot, you will need to create an account on BestBuy's website, as well as add credit card details that will be used by the bot to make the purchase

## Using the Bot
* First, ensure you read the Prerequisites section, and make sure you use the correct Firefox driver for your system.
* Update Selenium_switch_bot.py by changing these variables to match your BestBuy credentials:
  * email
  * password
* Run the bot: 
  > python3 Selenium_switch_bot.py
* **Note**: The bot may not run the first 2 or 3 times you try. If the bot doesn't start logging you in in a Firefox window ~10 seconds after starting, hit Ctl-C and try again.
* After logging you in, the bot will continuously refresh the page, checking if Switches are sold out:
  * If they are sold out, the bot prints 'Sold out' and tries again
  * If they are available, the bot will go through the process of attempting to purchase one.
* Once a switch has been purchased, the bot will report as such and stop executing. Double-check your account to make sure one was actually purchased!
