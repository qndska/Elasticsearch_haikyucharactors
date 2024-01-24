# ITCS414 Information Retrieval and Storage
Members:6488052 Sasasuang  Pattanakitjaroenchai 
6488061 Chaninan  Phetpangun 
6488226 Nisakorn Ngaosri

# Objective
The README file is to facilitate the setup and deployment of our web search system using Elasticsearch, Kibana, and Flask.  
Before starting, ensure that you already installed these devices into your system:
1. Elasticsearch
2. Kibana
3. Python
NOTE: You should install devices into Disk D to prevent errors.
                         
# Compilation and running
Elasticsearch:
1. Extract the zip file.
2. Open elasticsearch-8.10.2-windows-x86_64\elasticsearch-8.10.2\bin
   or Open Windows Powershell then use the 'cd' command to navigate the Windows Powershell to the directory where elasticsearch.bat file.
3. Click elasticsearch.bat for running.
   or Use ./elasticsearch.bat for running on Windows powershell.
4. Wait unit is finished running -> copy the token and password of Elasticsearch.

Kibana:
NOTE: If you use Windows Powershell, you must open a new Windows Powershell and don't close the previous one.
1. Extract the zip file.
2. Open kibana-8.10.2-windows-x86_64\kibana-8.10.2\bin.
   or Open Windows Powershell or Command Prompt then use the 'cd' command.
3. Click kibana.bat for running.
   or Use ./kibana.bat
4. Wait unit receives localhost of Elastic website.
5. Open the localhost
6. Enter the token of Elasticsearch.
   NOTE: If you are required to verify, you must run the verification-code.bat before entering the code from Kibana.
7. Enter the user name and password.
8. After that, you can access into Elastic website.

Flask:
1. Install Python using these commands on Anaconda Prompt:
	- pip install elasticsearch
	- pip install ndjson
2. Open Command Prompt 
3. Set up Flask using:
	- pip install Flask
	- use the 'cd' command to navigate where your Python file
	- set FLASK_APP=search_app (Name of python file)
	- set FLASK_ENV=development  
4. Running by 'flask run'
5. Copy the HTTP of the website 
6. Welcome to our web search engine!

# Snapshot of the Search System:
![image](https://github.com/qndska/Elasticsearch_haikyucharactors/assets/106175374/95c843ea-3ec5-473e-836e-7b4d92e5075d)
![image](https://github.com/qndska/Elasticsearch_haikyucharactors/assets/106175374/1fb52d42-4991-4bc0-8f64-07c44c0cd9aa)

