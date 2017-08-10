# graphviz
Basic exercises to get familiar with graphviz python package

***

## [20170810] graphviz_basic.py
* Usage: python graphviz_basic.py
* Description:  
  Basic manipulation of graphviz
***

## [20170810] flight_figure.py
* Usage: python flight_figure.py <input_filename> <output_filename> <figure_label>  
  e.g. python flight_figure.py flight.xlsx flight_figure flight_departure_and_arrival
* Description:  
  Read flight data from excel file and generate diagram with two clusters, departure and arrival  
  Each edge represents a specific flight
***

## [20170810] flight_search.py
* Usage: python flight_search.py <input_filename> <output_filename> <figure_label>  
  e.g. python flight_search.py flight.xlsx All_figure All_figure  
  e.g. python flight_search.py flight.xlsx LAX_depart LAX_depart -d LAX  
  e.g. python flight_search.py flight.xlsx LAX_arrival LAX_arrival -a LAX  
  e.g. python flight_search.py flight.xlsx All_LAX All_LAX -s LAX  
  e.g. python flight_search.py flight.xlsx LAX_CUN LAX_CUN -d LAX -a CUN  
  e.g. python flight_search.py flight.xlsx All_SFO All_SFO -d LAX -a CUN -s SFO
* Description:  
  Advanced manipulation with flight_figure.py  
  Given flight information list, users can search for specific airport as endpoint or set particular departure and arrival airports
***
