#### clone project
`https://github.com/iamlaboniraz/e_courier.git`

####Go to project directory 
`cd e_courier`

#### create virtualenv named venv 

for windows `virtualenv env`

for linux `virtualenv -v python3 venv`


#### Activate virtualenv 
for windows `venv\Scripts\activate`

for linux `source venv/bin/activate`


#### install packages
`pip install -r requirements.txt`

#### migrate project
`python manage.py migrate`

#### run project
`python manage.py runserver`
