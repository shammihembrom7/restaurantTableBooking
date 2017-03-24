# restaurantTableBooking
 REST API for restaurant table booking system.
 
 setup:  clone repository (run 'git clone https://github.com/shammighost7/restaurantTableBooking.git')
         run 'pip install -r requirement.txt'
         run 'python manage.py runserver'
         
 API is supports following functional requirements

Restuarants: 
1. Onboarding new restuarants 
2. Adding/Removing restuarants 
3. Add remove tables to restuarant 
4. Modify capacity/availability of a specific table 
5. Get bookings for a table by time range

Customers: 
1. Search Restaurants by name/location/cuisines 
2. Search for table by capacity for a given Restauant 
3. Book a table/Cancel a reservation. 
4. Write reviews on experience


to filter resatuarants by name/location/cuisines:
  hit the restaurant endpoint with  '?name=KFC'
  
  ex: http://127.0.0.1:8000/restaurants/?location=ulsoor
      http://127.0.0.1:8000/restaurants/?cuisine=italian
      http://127.0.0.1:8000/restaurants/?name=KFC
