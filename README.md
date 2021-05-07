This is the [Flask](https://flask.palletsprojects.com/en/1.1.x/) web app for [calculating percentile](https://en.wikipedia.org/wiki/Percentile#The_nearest-rank_method) of a specific pool.

## Getting started
First, come to the source folder and install flask. 
By the way, if you want to use your own python environment which isolates with the general python environment in computer, let create a new one and active it before. See [python environment](https://docs.python.org/3/library/venv.html) for details

```bash
cd percentile-app/
pip install requirement
```

This will install the flask framework to your python environment. 
Now let's start the application, run the command below

```bash
py main.py
```

Now the web application will start at the port 5000

## Endpoints
We have the 2 endpoints in the application. One is append or insert data and one is calculte the percentile.

To test it easily, I prefer to use [PostMan tool]().

### First endpoint
This endpoint will post a pool to application. If the pool is already exists, it will append the pool values. If not, it will insert a new pool.

Endpoint:
```bash
http://localhost:5000/api/v1/pool
```

Method: HTTP POST

Request body example:
```json
{
	"poolId": 1,
	"poolValues": [16,15,14,13,12,11]
}
```

The response is the string:
```bash
Apppended
```
When posted pool is existed, or
```bash
Inserted
```
When posted pool is not exsited

### Second endpoint
This endpoint will post an object to ask the P-th of a specific percetile in a given endpoint

Endpoint:
```bash
http://localhost:5000/api/v1/pool_indexes
```

Method: HTTP POST

Request body example:
```json
{
	"poolId": 1,
	"percentile": 40
}
```

Once success, the responsed body look like:
```json
{
    "total_count": 11,
    "value": 5
}
```

#### Note: 
In this application, I keep it sample and don't use any database connection to handle it.
The POOL_LIST is defined in the file <em>pool.py</em>

## Why Flask?
Flask is the useful framework to build lightweight application with Python backend. Also, Flask can satisfy most of demand of the backend Python.

In this project, I focus on the feature calculating percentile. So use the simple framewrok to build endpoint is the best choice.

## The normal percentile formula
My formula to calculate percentile:


![Image of Yaktocat](document/formula.PNG)


Where:

<em>n</em>: The result of P-th value in list

<em>P</em>: The percentile

<em>N</em>: Number elements in the sample

## How to extend with another advance percentile formula?

