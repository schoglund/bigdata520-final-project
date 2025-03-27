# BIG DATA 520 Final Project
Work for the final project in UW BIG DATA 520. Simulated streaming data using OpenWeather API, Spark, and Python to rank ski resorts according to historical weather patterns and "predict" future conditions for the upcoming 2025-26 ski season.

## Files
* **Date Frequency.ipynb** : the primary Jupyter notebook where I did my pre-processing to gather selected timestamps and geographical coordinates via the AccuWeather Geocoding API for my 8 ski resorts to feed into the OpenWeather API for historical timestamped weather.
* **send.py** : a Python helper script to simulate streaming data into Azure Event Hub.
* **utilities.py** : a hidden Python file that contains API keys and Azure connection information.
* **Ski Map.ipynb** : a Jupyter notebook to create an interactive map using Folium (Python wrapper to Leaflet) to showcase the top 3 ski resorts for each week of ski season based on historical weather patterns only.
* **requirements.txt** : packages I used for this project
* **output/ski_map.html** : final output of `Ski Map.ipynb`
