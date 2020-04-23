# happy sim
happy simulator

## Installation

Open a Unix terminal and type `git clone https://github.com/dfox3/happy.git`


## Requirements

*These scripts are not packaged and are not standalone executable at this stage. Requirements are needed for dev env.*

Needed:

 - Python 3.7.X (latest version)
     - pip installed with
         - for gaming graphix
         	- [pygame](https://pypi.org/project/pygame/)
         - for graphing scripts
         	- [matplotlib](https://pypi.org/project/matplotlib/)
         	- [seaborn](https://pypi.org/project/seaborn/)
         	- [pandas](https://pypi.org/project/matplotlib/)
         - For more information on how to pip install, visit [this guide](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) for more information.


     - other imports from [The Python Standard Library](https://docs.python.org/2/library/) (typically pre-installed):
        - [functools](https://docs.python.org/3/library/functools.html)
        - [datetime](https://docs.python.org/3/library/datetime.html)
        - [time](https://docs.python.org/3/library/time.html)
        - [csv](https://docs.python.org/3/library/csv.html)
        - [math](https://docs.python.org/3/library/math.html)
        - [random](https://docs.python.org/3/library/random.html)
        - [itertools](https://docs.python.org/3/library/itertools.html)

## Use:

### cmd line
Navigate to the working "happy" directory via terminal.
Execute python script.

```
python social_interactions.py
```

Typically, I use a command like this

```
python social_interactions.py -i 5000 -l my-log-name -r 100
```

 - -i (int) is how many iterations you want to test
 - -l (str) is the name of the log (make sure it doesn't have underscores if you want to plot the log data)
 - -r (int) is how many iterations do you want to have happen before a recalibration happens
 - -t (int) is how many seconds to wait between iterations

## Concepts

### Theorheticals
n/a

### Scripts
#### Sim
 - social_interactions.py
 	- this script contains a "main" for interaction simulation
 	- includes functions for having 2 NPC interact
 	- includes functions for choosing dialogs of NPCs either sending or responding to interactions

 - villager.py
 	- object for an NPC, named "villager" because I had Animal Crossing brain
 	- includes several object variables
 		- list of variables will go here
 	- includes functions to update NPC from another NPC's influence
 	- includes a printable function for the state of the NPC

 - trait_modifiers.py
 	- these are a list of functions that apply traits to different steps in interactions
 	- trait influence adjustments are in "villager.py" to avoid circular logic, sorry for the confusion
 	- GLOBAL variables are set in "traits_categories.py"

 - traits_categories.py
 	- GLOBAL variables for "trait_modifiers.py"

#### Graphing
 - plot_social_interations.py
 	- i (input) needs to be a logs/\*/interactions-\*/ directory

 - plot_social_mutations.py
 	- i (input) needs to be a logs/\*/mutations/ directory

 - plot_relationships.py
 	- i (input) needs to be a logs/\*/enemies/ or logs/\*/friends/ directory

## Status
n/a its berry early

### Stuff to be built
 - beliefs
 	- a dictionary variable of ideas a user hold true and how strongly they believe in them
 - encyclopedia
 	- a dictionary variable of all objects (NPC, items, beliefs, etc) that the NPC knows of and how well they know of the object
 - family
 	- similar to friends and enemies, but with values that indicate family relationships (like Spouse, Mother, Brother, Uncle, Ex-Spouse, etc.)
 - lovers,
 	- similar to friends and enemies, but for love
 - traits
 	- still adding different categories of traits, and identified traits need to be theorized and encoded
 - interactions
 	- more interactions can be theorized and encoded
 	- more complexity can be theorized. can there be a history of interactions between NPCs? can this history be tracked? is this what friends and enemies track? should there be more than greetings, convos, and terminators in coversations?
 - items
 	- items that the NPCs can carry around with them
 - money
 	- if money as a belief is developed, there needs to be some kind of currency system built
 - property
 	- if property as a belief is developed, there needs to be some kind of system for saying items laying around can belong to some NPCs but not other
 - coaltions
 	- groups that NPCs can claim to be a part of that are a stronghold of beliefs
 - social structure
 	- beliefs that govern the group of NPCs and are integral to the culture
 	- how an NPC ranks in society are decided by social structures
 	- social structure ranks come with restrictions than might cause other NPCs to respond differently to actions that go for or against the restrictions
 - real time game
 	- needs top down graphics (thinking earthbound style)
 	- interactions can't be iterative, needs to be based on NPC spatial proximity





## Info:

**20200423**

**Dylan Fox**

**fox.dylan92@gmail.com**
