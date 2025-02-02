#setup environment - anaconda

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

#setup environment - shell/terminal
mkdir bike
cd bike
pipenv install
pipenv shell
pip install -r requirements.txt

run streamlit app
streamlit run bike.py
