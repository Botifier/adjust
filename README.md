### Setup
```
pip install -r requirements.txt
```
### Create database
```
python manage.py migrate
```
### Running tests
```
python manage.py test
```
### Starting the api server
```
python manage.py runserver
```
The base url for the api is: <br>
localhost:8000/api/sampledataset/




### Common use cases:
1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order
<br>url: http://localhost:8000/api/sampledataset/?fields=impressions,clicks,channel,country&group=channel,country&date_to=2017-06-01&ordering=-clicks
2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order
<br>url: http://localhost:8000/api/sampledataset/?fields=installs,date&os=ios&date_from=2017-05-01&date_to=2017-05-31&ordering=date&group=date
3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order
<br>url: http://localhost:8000/api/sampledataset/?fields=revenue,os&group=os&date=2017-06-01&country=US&ordering=-revenue
4) Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI
<br>url: http://localhost:8000/api/sampledataset/?fields=cpi,spend,channel&group=channel&country=CA&ordering=-cpi