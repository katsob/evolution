#!/bin/bash

Rscript create_learn_curve.R $1
for NR in 1 21 41 61 81 101 121 141 161 181 201
do
	Rscript animate.R $1 $NR
done