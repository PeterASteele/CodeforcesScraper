#!/bin/bash
output_file="problem.tex"
echo "\\problemname{$1}" >> ${output_file}
echo "\\includegraphics[width=1\\textwidth]{problem-statement}" >> ${output_file}
