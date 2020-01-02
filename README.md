Taiwan receipt lottery statistic
=====
A web-app made by [Flask](https://github.com/pallets/flask) framework showing the annual statistics of  Taiwan receipt lottery, all the data shown in the chart are gathered from the Taiwan Ministry of Finance official site at real-time. ([source](https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/))  

This is a complete project ready to be directly deployed on [Google App Engine](https://cloud.google.com/appengine/)


Showcase
----------
![](https://raw.githubusercontent.com/314pies/Taiwan-receipt-lottery-statistic/master/Showcase.gif)

Try it Yourself: https://tw-lottery-statistic.appspot.com/


Installation
----------------
1. Clone this repository
2. Setup a Python 3 environment and install all the dependency listed in requirements.txt
3.  Run main.py, then enter http://127.0.0.1:5000/  in your browser. 
The following messages should be printed in the console.
    ```
     * Restarting with stat
     * Debugger is active!
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```


Credits
------------
[Flask](https://github.com/pallets/flask)  
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
[Matplotlib](https://matplotlib.org/)  
[How to show matplotlib in flask](https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask)  
[TheWeatherApp](https://github.com/tristanga/WeatherApp_FullCode)  
[Deploying a Web Application on Google App Engine](https://youtu.be/j_zD8jfVQJ4)  
[How to output requirements.txt automatically?](https://stackoverflow.com/questions/29715249/is-there-any-way-to-output-requirements-txt-automatically)