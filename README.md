# api-demo-python
This repository contains three Python codes to get you started using DataSpark Mobility Intelligence Platform. Each of the code will demonstrate how to call each of DataSpark Mobility Intelligence API printing the response in the console and export the result as CSV file.

## Prerequisite
- Python 2.7
- [requests](http://docs.python-requests.org/en/master/) package
- Text editor of your choice to edit the code (e.g. [Sublime Text](https://www.sublimetext.com/))

## Getting your DataStreamX Authorization Token
1. Register in DataStreamX.com 
2. Subscribe to DataSpark Mobility Intelligence API
3. Click Access Subscription button on the top right area
4. Choose the DataSpark Mobility API and obtain the key from the code snippet
 
## Getting started
1. Download or clone the repository
2. Open one of the three files with your text editor
3. Paste your DataStreamX key into the DataStreamXKey variable
4. Save the document
5. Go to your terminal and navigate to the folder where you clone or download the repository
6. Run the python code by typing (in this case using the OD Matrix API)
```
python odmatrix-api.py
```
When successful, the terminal will show a JSON output from the request 
