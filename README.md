# Flask Halloween joke

## Description 

This is the repository of the Flask Halloween joke made for my [Spanish YouTube channel](https://youtu.be/bPvzl9F3zcM?si=6b6v6o77v_mteCvo) if you want to know more about the development of this project I encourage you to visit that video.

### About the project

This project is a Flask app that exposes one API route with the path `/speak/<string:message>` which allows a GET request. When a GET request is made to that route, the server hosted the app (tipically a Windows or Mac computer) will use the TTS system to "speak" the message send in the path of the request. This project is perfect to make a prank to any person using the computer hosting the app 👻.

## Pre-requirements

- Python, better if the version is higher than 3.8.x
- A Windows or Mac computer, the project hasn't been tested in a Linux machine.

## Installation

1. Clone the repository by using the command `git clone https://github.com/Danii2020/flask-halloween-joke`

2. Go to the project directory by using the command `cd flask-halloween-joke`

3. Create a Python virtual environment by using the following command based on your OS:

        - Windows: python -m venv venv
        - MacOS: python3 -m venv venv

4. Activate the virtual environment by using the following command based on your OS:

        - Windows: .\venv\Scripts\activate
        - MacOS: source venv/bin/activate

5. Install the required Python packages by using the command `pip install -r requirements.txt`

6. Before running the app, in the terminal use the following command to find your computer's private IP:

        - Windows: ipconfig
        - MacOS: ifconfig

7. Search for your private IP that might start with `192.168.x.x`, copy the IP and past it in the attribute `host=` in the `app.run()` function at the bottom of the `app.py` file.

8. Run the app by using the command `python app.py`.

9. Copy the URL in the terminal, past in a browser using the following format: `http://192.168.x.x/speak/any message you want`.

10. Click in send or hit enter and listen the magic 🦻🏼.

## Contribution

Feel free to clone this repository, test the project and modify it as you want. You can open a pull request if you want to contribute with useful changes to make this project spookier 💀.