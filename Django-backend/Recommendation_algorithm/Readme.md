### Setting up the backend
1. Install the dependencies using pip 
    ```
        pip install -r requirements.txt
    ```
### Starting Fast API backend
Starting backend for development :
```
    python app.py -e dev 
```
Starting backend for production :
```
    python app.py -w 4
```
Visit [http://localhost:8000/hello](http://localhost:8000/hello) to check if backend api running properly. You should see this message :
```json
    {
        "message": "Hello from book-recommender-api"
    }
```
API docs will be available at :
- [http://localhost:8000/docs](http://localhost:8000/docs)
- [http://localhost:8000/redoc](http://localhost:8000/redoc)

### To start the development server (vite + react + tailwindcss) :
If you're running it for the first time :
```
    npm i
```
then
```
    npm run dev
```
### Building the ui
```
    npm run build 
```
The output directory will be : [/public](public)

## Other important stuff
- [Dataset](data) taken from [kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).