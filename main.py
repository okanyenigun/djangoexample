from flask import Flask
import multiprocessing
from time import sleep
from sqlalchemy import create_engine, Session

app = Flask(__name__)

# Assuming you're using SQLite for this example (just for demonstration purposes)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

def cpu_bound_task(data):
    # If using SQLAlchemy within the process, create a new session
    with Session(engine) as session:
        # your database operations here

        # CPU-bound operation
        result = sum(i * i for i in range(data))
    return result

@app.route('/start_task')
def start_task():
    data = 10000000
    process = multiprocessing.Process(target=cpu_bound_task, args=(data,))
    process.start()
    return "Task started!"

if __name__ == "__main__":
    # Explicitly use the 'spawn' start method
    multiprocessing.set_start_method('spawn')
    
    # Run Flask in debug mode, and only accessible from localhost
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=8080)
