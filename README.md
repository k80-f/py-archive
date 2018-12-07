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

### Docker
You can run arChive in a docker container by building and then running a docker image:
1. Build the Docker image by executing `docker build -t py-archive:latest .`
2. Run the Docker image `docker run -e "FLASK_SECRET_KEY=[SECRET KEY]" -p [PORT]:8080 py-archive`
   * Replace `[SECRET_KEY]` with a secret key.
   * Replace `[PORT]` with the desired port.
   * (Optional) Add `-d` to run detached.
   * Example: `docker run -d -e "FLASK_SECRET_KEY=mysecretkey" -p 8080:8080 py-archive`
