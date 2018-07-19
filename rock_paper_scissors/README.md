# Rock Paper Scissors!

### User stories

As a player,
So that I can play RPS,
I want to be able to input my move.

As a player,
So that I know what choices there are,
I want to see the choices available before I input my move.

As a player,
Because I have no friends,
I want to be able to play against myself.

As a player,
Because I think I don't like things being unfair,
I want the game to tell if I have won.

### Blockers: Mocking randomisers

I've worked out by using the `python` REPL how to write simple mocks, how to call on randomisers, and then how to mock randomisers.

From here, I managed to mock a randomiser in the REPL. However, when I try to implement it to my code, I found that I can't seem to have them work in the tests. I may have made 2 assumptions:

- The mocking and testing works exactly the same as Ruby RSpec
- The way I've nested a class call inside a class method might be screwing things up.
