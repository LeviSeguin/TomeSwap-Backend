#Recommendation_algorithm/Readme.md
### Setting up the backend
Install the dependencies using pip 
    ```
        pip install -r requirements.txt
    ```
### Starting Fast API backend
Starting backend for production :
```
    python app.py -w 4
```
Visit 
[http://localhost:8000/hello](http://localhost:8000/hello) 
to check if backend api running properly. You should see this message :
```json
    {
        "message": "Hello from book-recommender-api"
    }
```
API docs will be available at :
- [http://localhost:8000/docs](http://localhost:8000/docs)
- [http://localhost:8000/redoc](http://localhost:8000/redoc)

### To start the development server:
open ui in terminal and run 
```
    npm run dev
```
### Building the ui
```
    npm run build 
```
## Other important stuff
- [Dataset](data) taken from [kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).