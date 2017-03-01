#!/bin/bash

javac B.java
var=$(ls -l $1 | grep ans | wc -l)

for n in `seq 1 ${var}`; do
        #java TestGen > $1/$1-$n.in 
        #java TestGen > $1/$1-$n.in
        java B < $1/$1-$n.in > $1/$1-$n-us.ans
        diff -w $1/$1-$n.ans $1/$1-$n-us.ans
        rm $1/$1-$n-us.ans
done
