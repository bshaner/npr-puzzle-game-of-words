## NPR Sunday Puzzle 1-31-21

### Puzzle: 
https://www.npr.org/2021/01/31/962412357/sunday-puzzle-game-of-words

### Resources:
* graph of neighboring states. The provided graph was made manually, looking at a map. It doesn't account for any state borders without roads and we made some fun choices looking for more words, like including four corners as a border
* list of words to look for. The provided file was excerpted from http://www.poslarchive.com/math/scrabble/lists/common-8.html

### Approach:
* specify the length of the trip (4 states)
* read in our state graph
* find all trips, starting in each of the 48 states, removing duplicates
* read in our word bank
* see if we can permute our trips into the word bank words
* go back through our matches and rebuild the trip, taking the first route we find

### Results:
Found a bunch of words! Some of the words found in the bank don't feel "common" to me, but I found 15 good ones. Find a better word bank and more good words may be out there!
One interesting outcome is New Mexico (NM) and Minnesota (MN) are just the right distance apart that they can be used interchangably for some words.
