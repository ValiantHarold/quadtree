# Overview

Quadtree's are fantastic way to handle collision detection. Normally you would have to loop through and check every item with every other item causing the problem to have O(n^2). That is not optimal if I had 1000 items it would take 1 million checks per frame. By using a Quadtree I can get the big O of O(n log n) which leads to 1000 items only taking 3000 checks per frame.

[Software Demo Video](https://www.youtube.com/watch?v=tm5ptWJNtxI)

# Development Environment

Python

Pygame - used to display

# Useful Websites

-  [Coding Challenge #98.3: Quadtree Collisions - Part 3](https://www.youtube.com/watch?v=z0YFFg_nBjw)
-  [WQuadtree - wiki](https://en.wikipedia.org/wiki/Quadtree)

# Future Work

-  This quad tree is not optimal atm and I plan on working on it in the future when I have more time.
-  Add a string representation of the tree to be able to see all the nodes
-  Optimize the displaying of the items
