mkdir new_project
cd new_project
git init
python -m venv env
source env/Scripts/activate
pip install django
pip freeze > requirements.txt