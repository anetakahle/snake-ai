# snake-ai

Snake-ai is a framework for creating and testing AI agents in the environment of the "snake" game. 
The agent controls a snake which exists in an 8 by 8 grid. 
There is always a single apple placed randomly in the grid outside of the snake's body. 
When the snake eats the apple it scores a point and its body is lenghtend by one.
When the snake runs out of the grid or into its own body the game ends.

The objective of the game is for the snake to collect the apples while avoiding collision with the sides of the grid or the snake's own body. The maximum possible score is 62 which can be reached when the snake collects all the apples and fills the entire grid with its body.

The agent does not have the complete knowledge of the situation. It can see to three directions - front, left and right relative to its head position. For each direction the snake gets information about what it sees (it can only see apple or an obstacle - edge or its body) and the distance of the object in grid units. 



For tutorial please see the notebook `Tutorial.ipynb`.