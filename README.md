# lgagroup2
This is a repsitory for the LGA group 2 - Nicholas Cage.
CFG is the LGA assignment from a few weeks ago that a lot of our code is going to be based on soon. 
To run it, cd into the CFG repository, and call it as python3 cfg.py \<input_file_name\>. 
The script separates out the Terminals and Non-Terminals and contains an array that defines the grammar.
The grammar array is defined with the grammar character in position [0] of each row to be the non-terminal, with an implied "->" between it and element [1]. The remaining elements in that row of the array will be all the terminals and non-terminals in that derivation. The element "|" will never appear, and is replaced with additional entries in the table with the same Non-Terminal on the left side.

- Peter
