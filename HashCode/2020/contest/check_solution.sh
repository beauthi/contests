#!/bin/sh

# premier argument : path vers le script
# sortie : a.txt, b.txt, c.txt, d.txt, e.txt, f.txt

echo a
cat subject/a_example.txt| python3 $1 > a.txt
echo b
cat subject/b_read_on.txt| python3 $1 > b.txt
echo c
cat subject/c_incunabula.txt | python3 $1 > c.txt
echo d
cat subject/d_tough_choices.txt | python3 $1 > d.txt
echo e
cat subject/e_so_many_books.txt | python3 $1 > e.txt
echo f
cat subject/f_libraries_of_the_world.txt | python3 $1 > f.txt

zip -r code.zip src/
