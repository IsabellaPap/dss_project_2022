# Project for DSS 2022

## Run the app
To run the app you will need to install [Flask](https://flask.palletsprojects.com/en/2.2.x/) and [cv19index](https://github.com/closedloop-ai/cv19index) by [closedloop-ai](https://github.com/closedloop-ai). To do so, follow the instruction on the respective pages.

Before you run the app you need to locate the cv19index pakage files, installed on your computer, and **comment out** lines 339 - 346 (the contents of function reorder_inputs) in the file named "predict.py".

To run the app, after installing flask you just need to run the command:<br>
<br>
``` flask --app cv19index_app.py run ```

Open your browser to the host given in the terminal and add "/form" to it.<br>
<br>
Example: http://127.0.0.1:5000/form

The csv files (demographics, claims, preditions) will be overwritten when you run the code, but it is important that they **exist in the folder**, as the system will not create them if they are not found.
