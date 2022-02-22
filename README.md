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
  move_artifacts(Position): None

  
  
------
class Artifact(Actor)
  super().__init__()
  _value: int (attribute set inside the constructor)
  
  get_value():
  
-------
class director()
  _keyboard_service: KeyboardService (__init__)
  _video_service: VideoService (__init__)

  start_game(Cast): None
  _get_inputs(Cast): None
  _do_updates(Cast): None
  _do_outputs(Cast): None
  _update_score(int): None

_______

class KeyboardService()
  _cell_sizes: int

  get_direction(): Point

_______

class VideoService()
  _caption: str(__init__)
  _width: int(__init__)
  _heigh: int(__init__)
  _cell_size: int(__init__)
  _frame_rate: int(__init__)
  _debug: boolean(__init__)

  close_window(): None
  clear_buffer(): None
  draw_actor(): None
  draw_actors(): None
  flush_buffer(): None
  get_cell_size(): int
  get_heigh(): int
  get_width(): int
  is_window_open(): boolean
  open_window(): None
  _draw_grid(): None

_______

class Color()
  _red: int
  _green: int
  _blue: int
  _alpha: int

  to_tuple(): Tuple

______

class Point()
  _x: int
  _y: int

  add(Point): Point
  equals(Point): boolean
  get_x(): int
  get_y(): int
  scale(int): Point

  


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