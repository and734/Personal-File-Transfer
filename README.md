# File Server
- A simple locally hosted file server program written in **Python** to transfer files from your phone to PC.
- It makes use of python flask to run the server
- Uploaded files are stored in `uploads/`


## Features
- White minimalist theme
- Progress Bar indication
- Button to see all the uploads

## Requirements
- Python
- Flask
```
pip install flask
```

## Usage
- Clone this repo
- Run the following command inside the folder
```
py app.py
```
- Flask will show your local ip address in the terminal, however you can run `ipconfig` to get your active local IPv4 address
- Open a browser in your phone and enter `<your local IPv4>:5000` and upload any file!

**Note:** The port is set to `5000` by default in `server.py`. If you want to change it, modify the last line in `server.py` to any other port you want.

---
AL
