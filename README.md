# py-archive
arChive hackday project

### Installation and Running
1. Install required packages by executing `pip install -r requirements.txt` (It is recommended that you use a virtual environment for this).
2. Execute `python main.py` to run.

### Production Server
You can use many different production servers to run arChive. For example, to use waitress:
1. Install the waitress package using pip: `pip install waitress`.
2. Set environment variable `FLASK_SECRET_KEY` to a secret value.
2. Then, execute `waitress-serve 'main:app'` to run the server.