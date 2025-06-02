from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def hello():
    return {'Message':'Hello...Its my first api'}


@app.get('/about')
def about():
    return {'Message':'I love to learn new things'}