# DND Character Creator

![full-mockup]()
This site has been designed to be a full character creator for DND 5e. However due to time constraints this initail plan has had to be cut down. This site is now here to provide people an insight into what kind of characters are possible within the world of DND. THis site provides a lot of information on different Races, Classes and spells. Although many mechanics of the game are only touched upon and not everything makes it into the character sheet presented at the end, the user should end their time here with atleast an understanding of what the different Races and Classes offer, an insight into what a character at any level may look like and what abilities they may have at each level. This is a site that could be infinitly expanded upon. As you'll see below I have an extensive roadmap of new features and mechanics that can be implemented in the future. It is a shame I could not complete the whole character creator at this time. But this certainly should help potential players get a bitof prior knowledge and hopefully help them in tehir decision of what character they will play, should they go on to join a campaign. 

Find a link to the deployed site [here]()

## contents:
1. [User experience](#user-experience)
   - [Mockup desings](#simple-initial-design-plans)
2. [Final product](#final-product)
   - 
3. [Features](#features)
   - 
4. [Technology that was utilized](#technology-that-was-utilized)   
   - [Languages](#languages)
   - [External assets](#external-assets-utilized)
5. [Testing](#testing)  
   - [Manual testing](#manual-testing)
   - [Device testing](#device-testing)
6. [Deployment](#deployment)
7. [Credits/Acknowledgments](#creditsacknowledgments)
   - [Content](#content)
   - [Media](#media)  
8. [Final thoughts](#final-thoughts)    
___
## User experience:
### What I wanted to achieve:

1. Create a fun application that allows someone to be able to freely design and build a character that could be used in DnD 5e.

2. Have the user leave the application with a better understanding of what options are available when designing a character.

3. Present the user with a large varity of options that have real effects on the character which allows for hundreds of potentail character options

4. Allow the user the ability to look at all information surronding a choice before confimring that choice.

5. Present the user a charcater sheet at the end of teh application that clearly shows all the choices they made.

___
### Simple initial design plans:
state | Mockup example |
--- | --- |
Initial | ![desktop mockup of what the user sees when the game opens](assets/images/readme-images/wireframeFirstImage.png) |
Whilst playing | ![desktop mock up of page 2 "getting strated"](assets/images/readme-images/wireFrameSecond.png) |
___
## Final Product

___
## Features: 
### The background and imagery:
  -
___
## Technology that was utilized:
### languages:
* python
### external assets utilized:
* [GitHub](https://github.com/)
* [GitPod](https://gitpod.io/)
___
## testing:
 
### Manual Testing:
#### Feature Testing:
* Fixes refers to any potential current fixes/improvements that are still potentially available. 'None required' refers to the fact that at this moment there is no additional work needed to improve that feature. Many bugs and errors were encounted during the development process and several of these features were very much trail and error. The accounts of which can be found throughout the commits in GitHub.
* Choose Race: 
   - What was expected? The user types a Race from the list provided and is presented with the relevent information regarding that Race. The user can then read and cycle through the information at their liesure. If the user inputs a Race that is not present or spells one of the races incorrectly they are told that their choice is not playable and are asked to pick again.
   - How it was tested? 
   - What was the outcome?
   - Fixes? None required.
* Choose Class: 
   - What was expected? The user types a class from the list provided and is presented with the relevent information regarding that Class. The user can then read and cycle through the information at their liesure. If the user inputs a Class that is not present or spells one of the Class incorrectly they are told that their choice is not playable and are asked to pick again.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Choose Level: 
   - What was expected? The user chooses a level between 1 and 20. they are then asked to confirm this level. if the user inputs either a string, or a number not within 1 and 20 they are informed that the level chosen is not within the parameters and are asked to pick again.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Rolled hit points: 
   - What was expected? Once the user has chosen a level, their hit points would be rolled and calculated. This should be decided by the class hit dice. e.g Barbarians get a d12 and wizards get a d6. and their level. e.g a level 3 wizard would roll 3 d6. the sum of these dice decide theor hit points. This would then be presented to the user.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.   
* Choose Abilities: 
   - What was expected? The user is presnted with 3d6 rolls, the sum of which can be assigned to any one of 6 abilities. After assigning the first number a new roll is presented, this is reapeated untill all skills are assigned a score. If the user wishes to assign a rolled score to an already assigned ability they must re assign the old sore, they are not presented a new roll.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Modifiers and skill calculations: 
   - What was expected? When a score is assigned to an ability all skills that use that ability as thier base are given their modifiers based on what was rolled. e.g the skill Arcana is an intellegnce based skill, if the rolled score assigned to Intellegence is 14 then the Arcana modifier will be +2. likewise stealth is a dexterity based skill. if the score assigned to dexterity is 9 then the modifier to stealth would be -1.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Choose Proficienies: 
   - What was expected? The user is presented with a list of skills two of which can be assigned as proficent skills. The list provided is deterined by the class. e.g a bard can choose any two skills as proficient. However a Barbarian could not Choose Arcana as a proficent skill. there fore it would not appear in the list.
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Choose Cantrips: 
   - What was expected?
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Choose Spells: 
   - What was expected?
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* Choose Equipment: 
   - What was expected?
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.
* All choice confirmations: 
   - What was expected?
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.   
* Present Sheet: 
   - What was expected?
   - How it was tested?
   - What was the outcome?
   - Fixes? None required.                   
#### Device testing:
This site has been physically tested on:
   - ASUS ZenBook
   - Iphone X

   ___
## deployment:
  
___
## credits/acknowledgments
### Content:
-
### Media:
-
## Final thoughts
