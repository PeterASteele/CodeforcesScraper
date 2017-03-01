#!/bin/bash

javac B.java
for n in `seq 1 $2`; do
        #java TestGen > $1/$1-$n.in 
        #java TestGen > $1/$1-$n.in
        java B < $1/$1-$n.in > $1/$1-$n-us.ans
        diff -w $1/$1-$n.ans $1/$1-$n-us.ans
        rm $1/$1-$n-us.ans
done
