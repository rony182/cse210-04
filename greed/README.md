# Greed Game Specification
Greed is a game in which the player seeks to gather as many falling gems as possible. 
The game continues as long as the player wants more!  

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
python3 -m pip install pyray
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure 
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed                 (source code for game)
  +-- game              (specific game classes)
        +-- casting
            +-- actor (#)
            +-- cast
            +-- artifact
        +-- directing   
            +-- director
        +-- services
            +-- keyboard_service
            +-- video_service
        +-- shared   
            +-- color
            +-- point 
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```
## Structural Relationships
class Actor()
  _text: string
  _font_size: int
  _color: Color
  _position: Point
  _velocity: Point

get_color(): color
get_font_size(): int
get_text(): string
get_position(): Point
get_velocity(): Point
move_next(int): None
set_position(Point):None
set_color(Color):None
set_font_size(int): None
set_velocity(int): None
-----
class Cast()
  _actors: dictionary
  _score: int

add_actor(str, Actor)
get_actors(str): List <str>
get_all_actors(): List <str>   
get_first_actor(str): List <str>
remove_actor(str, Actor): None
update_score(): None
get_score(): int
------
class Artifact(Actor)
  super().__init__()
  _value: int (attribute set inside the constructor)
    
  get_value():
  move_actifacts(Position): None
-------



## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
## Authors (CSE210 winter 2022: Team 08)
* Kwazeme Ogubie (ogu21006@byui.edu)
* A. Belén Chaparro (cha21065@byui.edu)
* Fabrizio Carlassara (car21101@byui.edu)
* Rony Nickson Calderon Sara (cal21043@byui.edu)
* 