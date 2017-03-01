#!/bin/bash
source install_venv_and_packages.sh
cd data
./bash_script_script.sh "$1"
./get_problem_pdf.sh "$2"
cd ../problem_statement
./gen_problem_statement.sh "sample title"
