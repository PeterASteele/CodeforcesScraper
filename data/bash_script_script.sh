rm -rf sample
rm -rf secret
mkdir sample
mkdir secret
python scrape_solution.py "$1"
python scrape_data.py "$1"
./bash_script.sh sample
./bash_script.sh secret

