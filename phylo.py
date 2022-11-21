# Phylogenetics-with-Bio.Phylo
Create a simple Newick file named simple.dnd
(((A,B),(C,D)),(E,F,G));

#Printing the tree object as a string gives us a look at the entire object 
hierarchy.

from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
print(tree)

#The Tree object contains global information about the tree, such as 
whether it’s rooted or unrooted.It has one root clade, and under that, 
it’s nested lists of clades all the way down to the tips.

#The function draw_ascii creates a simple ASCII-art (plain text) 
dendrogram. This is a convenient visualization for interactive 
exploration, 
in case better graphical tools aren’t available.

from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
Phylo.draw_ascii(tree)

#If you have matplotlib or pylab installed, ou can create a graphic using 
the draw function.
 
from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick") tree.rooted = True
Phylo.draw(tree)
