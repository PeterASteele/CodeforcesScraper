#!/bin/bash
output_file="problem.tex"
> ${output_file}
echo "\\problemname{$1}" >> ${output_file}
echo "\\includegraphics{problem-statement}" >> ${output_file}
