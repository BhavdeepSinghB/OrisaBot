# Orisa Bot Documentation and List of Commands

List of instructions and general information about Orisa. The code lives [here](https://github.com/bhavdeepsinghb/whoison)

[**What's New?**](#whats-new)

Version: 1.3.5

## Getting Started

Orisa was initially created to notify team members about your online availablility. As such,  most of your interactions with Orisa will depend on your online status. 

Another thing to remember is that all of Orisa's commands start with an exclamation mark (`!`)

Make sure Orisa is online and type `!on`. If everything was set up correctly, the bot should have responded and set your status as online. 

You can check this by typing `!whoison`. This shows you a list of users who are also online along with the time they have been online for.

When you're done playing and want to turn your status to offline, type `!off`. 

In the most basic sense, you will be using these three commands the most, however, there are a lot of cool things Orisa can do you for you, the following is a table of contents for all Orisa commands divided by section

## Table Of Contents

* [**Basics**](#basics)
* [**Grouping**](#grouping)
* [**SR**](#sr)
* [**Practice**](#practice)
* [**Bug Reporting**](#bug-reporting)
* [**Misc**](#misc)

## Basics
****
## !needhealing or !ineedhealing
    
Gives you a link to this page

* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > !help

        Hi, I'm Orisa, a bot made by Zoid to automate the boring stuff on this
        server. For a full list of commands and documentation follow the link below
        https://bhavdeepsinghb.github.io/OrisaBot


    
## !status
    
Check if the bot is online and processing instructions

* **Arguments**
    
    -v : verbose - returns the number of instructions processed and bugs reported so far

* **Usage**
    
    _For All Users_

        > !status

        The bot is online and has been running for 0:02:51

        > !status -v

        The bot is online and has been running for 0:02:51
        In this session, 
        3 unique instructions have been processed
        1 unique bugs have been reported
        


## !on
Sets your status to online. 

You can now form groups, be included in groups and will be considered for captaincy during practice.

* **Arguments**
    
    *Optional*

    * `@a_user`         - (Admin ONLY) set someone else's status as online   

* **Usage**
    
    _For All Users_

        > !on

        Zoid is now online!

    _For Admin_
        
       > !on @SampleUser

        Admin command invoked by Zoid
        SampleUser is now online!


## !smurf
Sets your status to online and notifies the server that you are using a smurf account

If already online, just changes your status to smurf.
You can now form groups, be included in groups and will be considered for captaincy during practice.

* **Arguments**
    
    *Optional*

    * `@a_user`         - (Admin ONLY) set someone else's status to smurfing    

* **Usage**
    
    _For All Users_

        > !on

        Zoid is now online!

        > !smurf 

        Zoid is now smurfing

        > !smurf

        SampleUser is now online!
        SampleUser is now smurfing

## !whoison
Shows a list of all online players

* **Arguments**

    _None_

* **Usage**
    
    _For All Users_

        > !whoison

        Zoid (smurf) has been on for 0:00:57
        SampleUser has been on for 0:00:21
        Bastion has been on for 0:00:03


## !off
Sets your status to offline. 

You are automatically removed from any groups and will not be considered for captaincy in practice.

* **Arguments**
    
    `@a_user` - set someone else's status to offline (Admin ONLY)

* **Usage**
    
    _For All Users_

        > !off

        Zoid is now offline

    _For Admin_
        
        > !off @SampleUser

        Admin command invoked by Zoid
        SampleUser is now offline!

## !lmk
Notifies the caller the next time someone goes online. 
Ideal use case is for being notified when people are getting on around the same time.

* **Arguments**
    
    *Optional*

    * `@a_user`         - Be notified when specified user sets their status to `!on`

* **Usage**
    
    _For All Users_

        > !lmk

        SampleUser will be notified the next time someone goes on

        > !lmk @Zoid 

        SampleUser will be notified the next time Zoid goes on

        (Zoid) > !on 

        (As a direct message) Zoid is now online!

## !alloff
(Admin ONLY) Sets all members' statuses to offline and destroys any active groups

* **Arguments**
    
    _None_

* **Usage**
    
    _For Admin_
        
        > !alloff

        Admin command invoked by Zoid, everyone is off! All groups destroyed!

## Grouping
****

## !group {user/list of users}    
In order to use groups, please make sure you're online.

*If ungrouped* - creates a new group of calling user + all valid mentioned users

*If grouped* - adds all valid mentioned users to current group

* **User Validity**
    
    A user is consiered valid if they are online and not in any existing groups. Any users considered invalid have to be grouped up again.
    Other examples of invalidity include trying to group up with yourself, etc.

* **Arguments**
    
    (_Required_) User or list of users to group up with.

    Note - it is OPTIONAL to mention yourself when creating a group, but you need to mention at least one OTHER user.

* **Usage**
    
    _For All Users_

        > !group @SampleUser

        New Group Created for Zoid!
        The following players were added to the group ['SampleUser']

        > !group @anotherSampleUser
        
        The following players were added to the group ['anotherSampleUser']

        > !group @invalidUser

        The following players were not added since they are already grouped or
        offline, type !ungroup to remove yourself or !on to set your status 
        as online ['invalidUser']

## !whoisgrouped
Shows a list of all active groups

* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > !whoisgrouped

        The following is a list of all groups
        1) ['Zoid', 'SampleUser']
        2) ['Foo', 'Fighters', 'Bar']


## !ungroup
If you were in a group, removes you.

If there was just one other person in your group, they are ungrouped too and your group is destroyed.

* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > !ungroup

        Zoid has been removed from the group

        > !ungroup 

        Zoid has been removed from the group
        Zoid's group has been destroyed, SampleUser has now been ungrouped

## !destroygroup {group number}
(Admin ONLY) Destroys group with corresponding number

* **Arguments**
    
    (_Required_) A group number. 

    Group numbers are seen using the !whoisgrouped command

* **Usage**
    
    _For Admin_
        
        > !whoisgrouped

        The following is a list of all groups
        1) ['Dj_RealMeal', 'Ibonal (E-Bot)', 'z99ghostrider']
        2) ['Mac_Shizzle', 'Zoid']

        > !destroygroup 1

        Admin command invoked by Zoid
        Dj_RealMeal has been removed from the group
        Ibonal (E-Bot) has been removed from the group
        Ibonal (E-Bot)'s group has been destroyed, z99ghostrider has now been ungrouped

## SR
****

## !register
Adds a new database entry for the user, if none existed. 

* **User Validity**
    
    A user is consiered valid if they are a **team member** and not already in the database.

* **Arguments**
    
    (_Optional_) (Admin ONLY) User to register.

* **Usage**
    
    _For Valid Users_

        > !register

        Successfully added new database entry for SampleUser
        Please set your SR using !set <role> <sr>
        For more commands use !sr --help

        > !register
        
        Zoid is already registered. Type !sr @username for more


## !sr 
Displays given user's most recently updated SR, if any

* **Arguments**

    *Optional*
    
    * {user} - Returns the specified user's SR, if it exists
    * `--help` - Shows a quick list of all available commands  
    * `-team` - Shows team's average SR 
        * `-v` - Shows more team average statistics


* **Usage**
    
    _For All Users_

        > !sr

        For user SampleUser
        Tank: 1100
        Damage: 2334
        Support: 1242

        > !sr @Zoid

        For user Zoid
        Tank: None
        Damage: 2754
        Support: None

        > !sr -team

        Team Average SR: 2318.00

        Please note that this is based on the provided data so far. Type !sr --help for commands.

        > !sr --help

        If you're a new user, type !register to start!

        To check your sr, type !sr
        To set your sr, type !set <role> <sr>
        ...


## !set <role> <SR>
Sets the SR for the given role for the given user.
Refer to the list of acceptable roles and usage for correct syntax.

* **Arguments**

    *Required*
    
    * `role` - List of acceptable roles: ['tank', 'dps', 'damage', 'dmg', 'support', 'heals']  
    * `SR` - The SR you wish to set for the role 

    *Optional*

    * {user} - (Admin ONLY) sets the SR for the specified user. If they're registered

* **Usage**
    
    _For All Users_

        > !set tank 1100

        Successfully changed SampleUser's tank SR to 1100
        For user SampleUser
        Tank: 1100
        Damage: None
        Support: None

        > !set @SampleUser support 1242 

        Successfully changed SampleUser's support SR to 1242
        For user SampleUser
        Tank: 1100
        Damage: None
        Support: 1242


## Practice
****

## !practice {number of games} [list of arguments]
(Admin Only) Creates a new practice session with unique maps and captains for each game. 

Check out arguments to customize your practice

* **Notes**
    - At least 12 players must be online at the time practice is being created. If fewer players are online, a confirmation message is sent and the caller of the practice must react to it in within 60 seconds.
    - By default captains are unique for each game, but will be repeated if too few players are online
    - To be considered for captaincy, a user must be online (!on) before practice is invoked
    - When not using custom maps, the first map will be Control Point followed by Assault and Escort or Hybrid in that order. After the third game, this order switches around.

* **Arguments**
    
    *Required*

    * Number of games  - the number of games to be included in this practice

    *Optional*

    * `-num` - Maps may be repeated  
    * `-nuc` - Captains may be repeated
    * `-cm  <list of maps>` - Custom maps
        * List of maps is the name of all maps you wish to have
        * The name of a map is case insensitive and only needs one word. 
          
          King's Row = king's row = king's = king
        * If number of custom maps is less than the number of games in the practice, custom games will be played first and rest of the games will be randomized
* **Usage**
    

    _For Admin_
        
      > !practice 1

        Creating a practice session with 12 players where captains will be unique 
        and maps will be unique
        The number of games does not cover all game modes, you will start with 
        Control map
        Game 1: trippymcgee vs Ibonal (E-Bot)
        Map: Busan

      > !practice 4 -cm Busan Temple King's Route

        Creating a custom practice session with 10 players where captains will be unique
        Seems like less than 12 players are online, if you have enough randos or 
        those who aren't online, please react with :thumbsup: to proceed WITHIN 60 
        SECONDS
        
      > [Reacted]
        
        Game 1: Ibonal (E-Bot) vs Driller2012
        Map: Busan
        Game 2: BankerOfDoom vs Mac_Shizzle
        Map: Temple of Anubis
        Game 3: tristnieves9 vs Chicken Joe
        Map: King's Row
        Game 4: Dj_RealMeal vs trippymcgee
        Map: Route 66


## Bug Reporting
****

## !bug
Minimal bug report, notifies @Zoid of a bug, marks the location in the run's logfile

* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > !bug

        Bug Reported, thank you.
        Ping @Zoid for updates

## Misc
****

I made some commands for fun, these aren't logged and their bugs would take secondary priority. 

SOME commands will NOT use the exclamation mark (`!`)


## F 
Lets the server know you have paid your respects.

Case insensitive - f = F
* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > f

        Zoid has put some respecc on it

## X / A
Assemble either the X-men or the Avengers

Case insensitive - x = X / a = A
* **Arguments**
    
    _None_

* **Usage**
    
    _For All Users_

        > a

        Zoid has assembled the Avengers!

        > X

        Zoid has assembled the X-Men!


***

## What's New?
* **1.3.5 Update**
    Minor update 1.3.5 brings around a few more services and support services to Orisa. In addition, thanks to some deployment changes, Orisa's downtime is expected
    to reduce dramatically.

    * New Features:
        * Task - Reaper - One of the most common problems with manually turning your status to on/off was that users would forget to do one or the other. This would lead to the 
        core being in a stale state (the !whoisoncommand reporting incorrect information), effectively defeating the purpose of the bot. So reaper was created to alert the log
        channel of a user that has been on for a certain amount of time. This alert can be acknowledged by either the person being paged or anyone else. This service is also responsible for turning users !off when they have hit another threshold. 
        * (Testing) Hermes - The oldest issue with storing dynamic data in memory is that it does not persist between multiple runs and during frequent, multiple times an hour
        outages, that is not good news. Therefore, Hermes was developed as a backup and restoration service. Currently working solely with the core, Hermes writes the current core
        configuration to a backup file and if one exists, loads the config present in it. Hermes is also responsible for a backup task, which updates the backup every period of time (currently running at 6 hours) and creating a backup when gracefully shutting down to have the most recent state at next startup. 
        * Config files - Instead of storing tokens and other sensitive information in the code and risking pushing that up to github, Orisa now reads most of its data from an uncomitted config file. 
        
            There will soon be a section on a config file in the docs. This file is also used to configure all tasks, including the ones mentioned above, allowing users more flexibility on support services without necessarily diving into the code
    
    * Slash commands update: Slash commands might have to be pushed back significantly since it does not like the old architecture (client) and is effectively blocked by a whole architecutre change to bot.
        
        For now, the focus is going to be on a few more support services, starting with logging and with perhaps some more research, it might be feasible to include slash commands with the current architecture


* **1.3 is here!**
    Major update 1.3 brings about a change to the codebase. While the difference isn't noticable off-hand, it will help quite a bit with debugging, maintainance and adding new features! 
    
    New Features:
    * Welcome message - changed to send a new message in the event a user joins and delete it after each acceptance. This allows for a clean boot for the bot
    * Tasks - Ability to send scheduled messages. Currently sending a special message to taco
    
    Changes:
    * Admin commands have now been switched to "team member" commands, anyone with the role can now access them

    Expecting to bring slash commands in the next incremental update!

* **Major Update 1.3** 
    Major update 1.3 will bring changes to the codebase. 
    Users may not see as much of an impact, but it will help the devs plan out and add more features quickly and easily

* **Minor Update 1.2.2**

    New feature! Be notified via DM the next time someone goes `!on`

    New Features
    * [`!lmk {@a_user}`](#lmk) - sends you a discord DM the next time someone (specified user optional) sets their status to `!on`

* **Minor Update 1.2.1**

    `!smurf` has been updated to accept a user argument (optional). This allows `Admin`s to change the status of other people to smurfing

* **Next Beta and 1.2**

    The next whoison-beta update 1.1.3 will introduce long term records in the form of connection to a google spreadsheet.
    Users will be able to interact with the sheet through the bot and the sheet itself will take care of any necessary calculations.
    This will later transition into an actual database and launch as a new version 1.2

* **Beta 1.1.2 is now Stable 1.1.2**

    First new feature in a while and a couple of bug fixes

    New Features
    * Role Management - Roles means access and Orisa now has control over it. Currently being used to assign new members the "Friend" role once they have read and agreed to the rules.

    Bug Fixes
    * Logging issue with the Admin version of `!on` had an issue       fixed
    * Message reactions were having some issues upon reconnection      testing

* **Patch 1.1.1-1**

    Bug fixes
    * Fixed a bug that displayed user objects instead of names when using `!whoisgrouped`
    
    Changes
    * `!help` has been renamed to `!needhealing` or `!ineedhealing` (both work, case insensitive) since it was interrupting other bots' help message


    
    