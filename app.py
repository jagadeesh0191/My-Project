# from flask import Flask, render_template, request, redirect, url_for, session, flash
# import random
# import string
# import datetime # Import for date handling

# app = Flask(__name__)
# # IMPORTANT: Change this in production. It's used for session management.
# app.secret_key = 'your_super_secret_key_here_change_this_in_production'

# # --- Mock Data ---
# users_db = {'testuser': 'testpass'}  # Demo account
# # Using a dictionary to store bookings per user
# user_past_bookings = {} # Structure: {'username': [{'booking_id': 'xyz', ...}]}

# mock_travel_options = {
#     'flights': [
#         {'id': 'flight1', 'flight_number': 'AC101', 'airline': 'AirConnect',
#          'departure_time': '06:00 AM', 'arrival_time': '08:00 AM', 'price': 150.00, 'duration': '2h 00m'},
#         {'id': 'flight2', 'flight_number': 'SH202', 'airline': 'SkyHigh',
#          'departure_time': '09:30 AM', 'arrival_time': '11:30 AM', 'price': 180.00, 'duration': '2h 00m'},
#         {'id': 'flight3', 'flight_number': 'BL303', 'airline': 'BlueJet',
#          'departure_time': '01:00 PM', 'arrival_time': '03:30 PM', 'price': 220.00, 'duration': '2h 30m'},
#     ],
#     'buses': [
#         {'id': 'bus1', 'name': 'Express Lines', 'departure_time': '08:00 AM',
#          'arrival_time': '12:00 PM', 'price': 25.00, 'total_seats': 20},
#         {'id': 'bus2', 'name': 'City Link', 'departure_time': '10:00 AM',
#          'arrival_time': '02:00 PM', 'price': 30.00, 'total_seats': 25},
#         {'id': 'bus3', 'name': 'Green Transport', 'departure_time': '03:00 PM',
#          'arrival_time': '07:30 PM', 'price': 28.00, 'total_seats': 18},
#     ],
#     'trains': [
#         {'id': 'train1', 'number': 'REX001', 'name': 'Rail Express',
#          'departure_time': '07:00 AM', 'arrival_time': '01:00 PM', 'price': 60.00},
#         {'id': 'train2', 'number': 'MET002', 'name': 'Metro Rail',
#          'departure_time': '11:00 AM', 'arrival_time': '05:00 PM', 'price': 75.00},
#         {'id': 'train3', 'number': 'SFR003', 'name': 'Speedy Freight',
#          'departure_time': '09:00 AM', 'arrival_time': '03:00 PM', 'price': 65.00},
#     ],
#     'hotels': [
#         {'id': 'hotel1', 'name': 'Grand Plaza Hotel', 'location': 'New York', 'price_per_night': 120.00, 'rating': 4.5},
#         {'id': 'hotel2', 'name': 'Riverside Inn', 'location': 'New York', 'price_per_night': 80.00, 'rating': 3.8},
#         {'id': 'hotel3', 'name': 'Mountain View Resort', 'location': 'Denver', 'price_per_night': 150.00, 'rating': 4.7},
#         {'id': 'hotel4', 'name': 'City Center Suites', 'location': 'Chicago', 'price_per_night': 95.00, 'rating': 4.0},
#         {'id': 'hotel5', 'name': 'Coastal Breeze Hotel', 'location': 'Miami', 'price_per_night': 130.00, 'rating': 4.2},
#         {'id': 'hotel6', 'name': 'The Parisian Palace', 'location': 'Paris', 'price_per_night': 250.00, 'rating': 4.9},
#         {'id': 'hotel7', 'name': 'Eiffel Tower View Hotel', 'location': 'Paris', 'price_per_night': 180.00, 'rating': 4.3},
#         {'id': 'hotel8', 'name': 'Tokyo Capsule Inn', 'location': 'Tokyo', 'price_per_night': 50.00, 'rating': 3.5},
#         {'id': 'hotel9', 'name': 'Shinjuku Grand Hotel', 'location': 'Tokyo', 'price_per_night': 200.00, 'rating': 4.6},
#         {'id': 'hotel10', 'name': 'London Bridge Hotel', 'location': 'London', 'price_per_night': 170.00, 'rating': 4.4},
#         {'id': 'hotel11', 'name': 'Westminster Guesthouse', 'location': 'London', 'price_per_night': 90.00, 'rating': 3.9},
#         {'id': 'hotel12', 'name': 'Rome Colosseum Stay', 'location': 'Rome', 'price_per_night': 110.00, 'rating': 4.1},
#         {'id': 'hotel13', 'name': 'Venetian Gondola Hotel', 'location': 'Venice', 'price_per_night': 160.00, 'rating': 4.6},
#         {'id': 'hotel14', 'name': 'Sydney Opera House Suites', 'location': 'Sydney', 'price_per_night': 190.00, 'rating': 4.8},
#         # Adding more diverse locations
#         {'id': 'hotel15', 'name': 'Berlin Central Hotel', 'location': 'Berlin', 'price_per_night': 100.00, 'rating': 4.0},
#         {'id': 'hotel16', 'name': 'Historical Heart Hotel', 'location': 'Berlin', 'price_per_night': 130.00, 'rating': 4.2},
#         {'id': 'hotel17', 'name': 'Dubai Marina Resort', 'location': 'Dubai', 'price_per_night': 300.00, 'rating': 4.9},
#         {'id': 'hotel18', 'name': 'Desert Rose Hotel', 'location': 'Dubai', 'price_per_night': 220.00, 'rating': 4.5},
#         {'id': 'hotel19', 'name': 'Kyoto Zen Garden Inn', 'location': 'Kyoto', 'price_per_night': 140.00, 'rating': 4.7},
#         {'id': 'hotel20', 'name': 'Ancient Temple Stay', 'location': 'Kyoto', 'price_per_night': 90.00, 'rating': 4.1},
#         {'id': 'hotel21', 'name': 'Rio Beachfront Hotel', 'location': 'Rio de Janeiro', 'price_per_night': 170.00, 'rating': 4.3},
#         {'id': 'hotel22', 'name': 'Carnival Grand Hotel', 'location': 'Rio de Janeiro', 'price_per_night': 210.00, 'rating': 4.6},
#     ]
# }

# # Store temporary booking details (used across multiple steps before payment)
# temp_booking_details = {}

# # Mock occupied seats for buses (in a real app, this would be dynamic from a DB)
# # Key: bus_id, Value: list of occupied seat numbers
# occupied_bus_seats = {
#     'bus1': ['A1', 'A2', 'B3'],
#     'bus2': ['C1', 'D4', 'E5'],
#     'bus3': ['F1', 'F2'],
# }

# # --- Helper Functions ---
# def generate_unique_id(length=10):
#     """Generate a unique alphanumeric ID."""
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# def generate_seat_numbers(item_id, total_seats=None):
#     """Generates a list of mock seat objects (for buses) or a single seat (for flights/trains)."""
#     if 'bus' in item_id: # For buses, generate a grid of seats
#         seats = []
#         # Get occupied seats for this specific bus, or an empty list if none
#         occupied = occupied_bus_seats.get(item_id, [])
#         num_rows = (total_seats + 3) // 4 # Group into rows of 4
#         for row in range(num_rows):
#             for col in range(1, 5): # 4 seats per row
#                 seat_number = f"{chr(65+row)}{col}" # A1, A2, B1, B2 etc.
#                 if len(seats) < total_seats:
#                     seats.append({
#                         'number': seat_number,
#                         'occupied': seat_number in occupied
#                     })
#         return seats
#     else: # For flights/trains, generate a single unique seat number
#         return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# def calculate_hotel_price(hotel_id, checkin_str, checkout_str):
#     """Calculates total hotel price based on nights."""
#     try:
#         checkin_date = datetime.datetime.strptime(checkin_str, '%Y-%m-%d').date()
#         checkout_date = datetime.datetime.strptime(checkout_str, '%Y-%m-%d').date()
#         if checkout_date <= checkin_date:
#             return 0 # Invalid date range

#         nights = (checkout_date - checkin_date).days
#         hotel = next((h for h in mock_travel_options['hotels'] if h['id'] == hotel_id), None)
#         if hotel:
#             return hotel['price_per_night'] * nights
#         return 0
#     except ValueError:
#         return 0 # Handle invalid date format

# # --- Authentication Routes ---
# @app.route('/')
# def index():
#     return redirect(url_for('signin'))

# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     if 'username' in session:
#         return redirect(url_for('home'))

#     if request.method == 'POST':
#         username = request.form.get('username', '').strip()
#         password = request.form.get('password', '').strip()

#         if not username or not password:
#             flash('Please enter both username and password', 'error')
#             return redirect(url_for('signin'))

#         if username in users_db and users_db[username] == password:
#             session['username'] = username
#             flash('Login successful!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid username or password', 'error')
#             return redirect(url_for('signin'))

#     return render_template('signin.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if 'username' in session:
#         return redirect(url_for('home'))

#     if request.method == 'POST':
#         email = request.form.get('email', '').strip()
#         username = request.form.get('username', '').strip()
#         password = request.form.get('password', '').strip()
#         confirm_password = request.form.get('confirm_password', '').strip()

#         if not all([email, username, password, confirm_password]):
#             flash('All fields are required', 'error')
#             return redirect(url_for('signup'))

#         if password != confirm_password:
#             flash('Passwords do not match', 'error')
#             return redirect(url_for('signup'))

#         if username in users_db:
#             flash('Username already exists', 'error')
#             return redirect(url_for('signup'))

#         users_db[username] = password
#         user_past_bookings[username] = [] # Initialize past bookings for new user
#         flash('Account created successfully! Please sign in', 'success')
#         return redirect(url_for('signin'))

#     return render_template('signup.html')

# @app.route('/home')
# def home():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))
#     return render_template('home.html', username=session['username'])

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     session.pop('current_booking', None) # Clear any ongoing booking
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('signin'))

# # --- Past Bookings ---
# @app.route('/past_bookings')
# def past_bookings():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     username = session['username']
#     bookings = user_past_bookings.get(username, [])
#     return render_template('past_bookings.html', bookings=bookings)

# # --- Buses Booking Flow ---
# @app.route('/book/buses', methods=['GET', 'POST'])
# def book_buses():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     if request.method == 'POST':
#         source = request.form.get('source')
#         destination = request.form.get('destination')
#         travel_date = request.form.get('date')

#         if not all([source, destination, travel_date]):
#             flash('Please fill in all booking details.', 'error')
#             return redirect(url_for('book_buses'))

#         session['current_booking'] = {
#             'type': 'buses',
#             'source': source,
#             'destination': destination,
#             'date': travel_date
#         }
#         return redirect(url_for('buses_available'))

#     return render_template('buses.html')

# @app.route('/book/buses/available')
# def buses_available():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     booking = session.get('current_booking')
#     if not booking or booking['type'] != 'buses':
#         flash('Please start a bus booking first.', 'error')
#         return redirect(url_for('book_buses'))

#     # In a real app, filter buses based on source, destination, date
#     available_options = mock_travel_options['buses']
#     return render_template('buses_available.html',
#                            buses=available_options,
#                            booking=booking)

# @app.route('/book/buses/select_seats/<bus_id>', methods=['GET', 'POST'])
# def select_bus_seats(bus_id):
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     bus = next((b for b in mock_travel_options['buses'] if b['id'] == bus_id), None)
#     if not bus:
#         flash('Bus not found', 'error')
#         return redirect(url_for('buses_available'))

#     if request.method == 'POST':
#         selected_seats = request.form.getlist('seats')
#         if not selected_seats:
#             flash('Please select at least one seat.', 'error')
#             return redirect(url_for('select_bus_seats', bus_id=bus_id))

#         # Check if selected seats are occupied (basic check for demo)
#         occupied = occupied_bus_seats.get(bus_id, [])
#         for seat in selected_seats:
#             if seat in occupied:
#                 flash(f'Seat {seat} is already occupied. Please choose another.', 'error')
#                 return redirect(url_for('select_bus_seats', bus_id=bus_id))

#         # Update current_booking
#         session['current_booking']['selected_bus'] = bus
#         session['current_booking']['selected_seats'] = selected_seats
#         session['current_booking']['amount'] = bus['price'] * len(selected_seats) # Calculate price based on seats

#         # Mark seats as occupied for subsequent bookings (in a real system, this would be persistent)
#         if bus_id not in occupied_bus_seats:
#             occupied_bus_seats[bus_id] = []
#         occupied_bus_seats[bus_id].extend(selected_seats)

#         # Re-assign session['current_booking'] to ensure Flask recognizes the changes
#         session.modified = True

#         return redirect(url_for('payment'))

#     # For GET request, display seats
#     seats_data = generate_seat_numbers(bus_id, bus['total_seats'])
#     return render_template('buses_select_seats.html', bus=bus, seats=seats_data)

# # --- Flights Booking Flow ---
# @app.route('/book/flights', methods=['GET', 'POST'])
# def book_flights():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     if request.method == 'POST':
#         source = request.form.get('source')
#         destination = request.form.get('destination')
#         travel_date = request.form.get('date')

#         if not all([source, destination, travel_date]):
#             flash('Please fill in all booking details.', 'error')
#             return redirect(url_for('book_flights'))

#         session['current_booking'] = {
#             'type': 'flights',
#             'source': source,
#             'destination': destination,
#             'date': travel_date
#         }
#         return redirect(url_for('flights_available'))

#     return render_template('flights.html')

# @app.route('/book/flights/available')
# def flights_available():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     booking = session.get('current_booking')
#     if not booking or booking['type'] != 'flights':
#         flash('Please start a flight booking first.', 'error')
#         return redirect(url_for('book_flights'))

#     # In a real app, filter flights based on source, destination, date
#     available_options = mock_travel_options['flights']
#     return render_template('flights_available.html',
#                            flights=available_options,
#                            booking=booking)

# @app.route('/book/flights/confirm/<flight_id>')
# def confirm_flight(flight_id):
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     flight = next((f for f in mock_travel_options['flights'] if f['id'] == flight_id), None)
#     if not flight:
#         flash('Flight not found', 'error')
#         return redirect(url_for('flights_available'))

#     # Ensure current_booking exists and is a dictionary.
#     # It should already exist from book_flights(), but this adds robustness.
#     if 'current_booking' not in session or not isinstance(session['current_booking'], dict):
#         session['current_booking'] = {'type': 'flights'}
#     elif session['current_booking'].get('type') != 'flights':
#         session['current_booking'] = {'type': 'flights'} # Reset if type is mismatched

#     # Update existing booking details
#     booking_details = session['current_booking']
#     booking_details['selected_flight'] = flight
#     booking_details['seat_number'] = generate_seat_numbers(flight_id)
#     booking_details['amount'] = float(flight['price']) # Ensure it's a float
#     booking_details['type'] = 'flights' # Explicitly ensure type is set

#     # Re-assign to session to ensure Flask recognizes the modification for persistence
#     session['current_booking'] = booking_details
#     session.modified = True # Explicitly tell Flask the session object has been modified

#     return redirect(url_for('payment'))

# # --- Trains Booking Flow ---
# @app.route('/book/trains', methods=['GET', 'POST'])
# def book_trains():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     if request.method == 'POST':
#         source = request.form.get('source')
#         destination = request.form.get('destination')
#         travel_date = request.form.get('date')

#         if not all([source, destination, travel_date]):
#             flash('Please fill in all booking details.', 'error')
#             return redirect(url_for('book_trains'))

#         session['current_booking'] = {
#             'type': 'trains',
#             'source': source,
#             'destination': destination,
#             'date': travel_date
#         }
#         return redirect(url_for('trains_available'))

#     return render_template('trains.html')

# @app.route('/book/trains/available')
# def trains_available():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     booking = session.get('current_booking')
#     if not booking or booking['type'] != 'trains':
#         flash('Please start a train booking first.', 'error')
#         return redirect(url_for('book_trains'))

#     # In a real app, filter trains based on source, destination, date
#     available_options = mock_travel_options['trains']
#     return render_template('trains_available.html',
#                            trains=available_options,
#                            booking=booking)

# @app.route('/book/trains/confirm/<train_id>')
# def confirm_train(train_id):
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     train = next((t for t in mock_travel_options['trains'] if t['id'] == train_id), None)
#     if not train:
#         flash('Train not found', 'error')
#         return redirect(url_for('trains_available'))

#     # Ensure current_booking exists and is a dictionary.
#     if 'current_booking' not in session or not isinstance(session['current_booking'], dict):
#         session['current_booking'] = {'type': 'trains'}
#     elif session['current_booking'].get('type') != 'trains':
#         session['current_booking'] = {'type': 'trains'}

#     # Generate a unique seat/ticket number for the train (automated)
#     booking_details = session['current_booking']
#     booking_details['selected_train'] = train
#     booking_details['ticket_number'] = generate_seat_numbers(train_id) # Reusing func
#     booking_details['amount'] = float(train['price']) # Set amount for payment
#     booking_details['type'] = 'trains' # Explicitly ensure type is set

#     session['current_booking'] = booking_details
#     session.modified = True # Explicitly tell Flask the session object has been modified

#     return redirect(url_for('payment'))

# # --- Hotels Booking Flow ---
# @app.route('/book/hotels', methods=['GET', 'POST'])
# def book_hotels():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     if request.method == 'POST':
#         location = request.form.get('location')
#         checkin_date = request.form.get('checkin')
#         checkout_date = request.form.get('checkout')

#         if not all([location, checkin_date, checkout_date]):
#             flash('Please fill in all hotel booking details.', 'error')
#             return redirect(url_for('book_hotels'))

#         # Basic date validation
#         try:
#             ci_date = datetime.datetime.strptime(checkin_date, '%Y-%m-%d').date()
#             co_date = datetime.datetime.strptime(checkout_date, '%Y-%m-%d').date()
#             if co_date <= ci_date:
#                 flash('Check-out date must be after check-in date.', 'error')
#                 return redirect(url_for('book_hotels'))
#         except ValueError:
#             flash('Invalid date format. Please use ISO format (YYYY-MM-DD).', 'error')
#             return redirect(url_for('book_hotels'))


#         session['current_booking'] = {
#             'type': 'hotels',
#             'location': location,
#             'checkin_date': checkin_date,
#             'checkout_date': checkout_date
#         }
#         return redirect(url_for('hotels_available'))

#     return render_template('hotels.html')

# @app.route('/book/hotels/available')
# def hotels_available():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     booking = session.get('current_booking')
#     if not booking or booking['type'] != 'hotels':
#         flash('Please start a hotel booking first.', 'error')
#         return redirect(url_for('book_hotels'))

#     # Filter hotels by location (case-insensitive and partial match)
#     search_location = booking['location'].lower()
#     available_hotels = [
#         h for h in mock_travel_options['hotels']
#         if search_location in h['location'].lower()
#     ]

#     # Calculate nights_stay for each hotel before passing to template
#     for hotel in available_hotels:
#         try:
#             checkin_date = datetime.datetime.strptime(booking['checkin_date'], '%Y-%m-%d').date()
#             checkout_date = datetime.datetime.strptime(booking['checkout_date'], '%Y-%m-%d').date()
#             hotel['nights_stay'] = (checkout_date - checkin_date).days
#         except ValueError:
#             hotel['nights_stay'] = 0 # Fallback for invalid date formats

#     if not available_hotels:
#         # Generate a list of available locations to suggest
#         all_locations = sorted(list(set(h['location'] for h in mock_travel_options['hotels'])))
#         flash(f'No hotels found for "{booking["location"]}". Try searching for one of these locations: {", ".join(all_locations)}.', 'info')


#     return render_template('hotels_available.html',
#                            hotels=available_hotels,
#                            booking=booking,
#                            calculate_hotel_price=calculate_hotel_price)

# @app.route('/book/hotels/confirm/<hotel_id>')
# def confirm_hotel(hotel_id):
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     hotel = next((h for h in mock_travel_options['hotels'] if h['id'] == hotel_id), None)
#     booking = session.get('current_booking')

#     if not hotel or not booking or booking['type'] != 'hotels':
#         flash('Hotel or booking details not found.', 'error')
#         return redirect(url_for('book_hotels'))

#     total_amount = calculate_hotel_price(hotel['id'], booking['checkin_date'], booking['checkout_date'])
#     if total_amount <= 0:
#         flash('Invalid hotel booking dates or price calculation error.', 'error')
#         return redirect(url_for('hotels_available'))

#     # Ensure current_booking exists and is a dictionary.
#     if 'current_booking' not in session or not isinstance(session['current_booking'], dict):
#         session['current_booking'] = {'type': 'hotels'}
#     elif session['current_booking'].get('type') != 'hotels':
#         session['current_booking'] = {'type': 'hotels'}

#     booking_details = session['current_booking']
#     booking_details['selected_hotel'] = hotel
#     booking_details['amount'] = total_amount
#     booking_details['type'] = 'hotels' # Explicitly ensure type is set

#     session['current_booking'] = booking_details
#     session.modified = True

#     return redirect(url_for('payment'))


# # --- Payment ---
# @app.route('/payment', methods=['GET', 'POST'])
# def payment():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     booking = session.get('current_booking')
#     # Updated check: ensure booking is a dict and has an 'amount' key
#     if not isinstance(booking, dict) or 'amount' not in booking or booking['amount'] is None:
#         flash('No valid booking found for payment. Please start a new booking.', 'error')
#         return redirect(url_for('home'))

#     if request.method == 'POST':
#         payment_method = request.form.get('method')
#         if not payment_method:
#             flash('Please select a payment method.', 'error')
#             return redirect(url_for('payment'))

#         # Simulate payment success
#         booking_confirmation = {
#             'booking_id': generate_unique_id(),
#             'booking_type': booking['type'],
#             'amount': booking['amount'],
#             'payment_method': payment_method,
#             'date_booked': datetime.date.today().strftime('%Y-%m-%d') # Add booking date
#         }

#         # Add specific details based on booking type
#         if booking['type'] == 'flights':
#             flight = booking.get('selected_flight')
#             booking_confirmation['details'] = f"{flight['airline']} {flight['flight_number']}" if flight else "N/A"
#             booking_confirmation['source'] = booking.get('source')
#             booking_confirmation['destination'] = booking.get('destination')
#             booking_confirmation['travel_date'] = booking.get('date')
#             booking_confirmation['seat_number'] = booking.get('seat_number')
#         elif booking['type'] == 'buses':
#             bus = booking.get('selected_bus')
#             booking_confirmation['details'] = f"{bus['name']}" if bus else "N/A"
#             booking_confirmation['source'] = booking.get('source')
#             booking_confirmation['destination'] = booking.get('destination')
#             booking_confirmation['travel_date'] = booking.get('date')
#             booking_confirmation['selected_seats'] = booking.get('selected_seats', [])
#         elif booking['type'] == 'trains':
#             train = booking.get('selected_train')
#             booking_confirmation['details'] = f"{train['name']} {train['number']}" if train else "N/A"
#             booking_confirmation['source'] = booking.get('source')
#             booking_confirmation['destination'] = booking.get('destination')
#             booking_confirmation['travel_date'] = booking.get('date')
#             booking_confirmation['ticket_number'] = booking.get('ticket_number')
#         elif booking['type'] == 'hotels':
#             hotel = booking.get('selected_hotel')
#             booking_confirmation['details'] = f"{hotel['name']} ({hotel['location']})" if hotel else "N/A"
#             booking_confirmation['location'] = booking.get('location')
#             booking_confirmation['checkin_date'] = booking.get('checkin_date')
#             booking_confirmation['checkout_date'] = booking.get('checkout_date')

#         # Store booking in user's past bookings
#         username = session['username']
#         if username not in user_past_bookings:
#             user_past_bookings[username] = []
#         user_past_bookings[username].append(booking_confirmation)

#         session['booking_confirmation'] = booking_confirmation
#         session.pop('current_booking', None) # Clear ongoing booking after confirmation
#         session.modified = True # Explicitly tell Flask the session object has been modified
#         return redirect(url_for('payment_success'))

#     return render_template('payment.html', booking=booking)

# @app.route('/payment/success')
# def payment_success():
#     if 'username' not in session:
#         flash('Please sign in first', 'error')
#         return redirect(url_for('signin'))

#     confirmation = session.get('booking_confirmation')
#     if not confirmation:
#         flash('No booking confirmation found', 'error')
#         return redirect(url_for('home'))

#     # Clear confirmation from session after displaying
#     session.pop('booking_confirmation', None)
#     session.modified = True # Explicitly tell Flask the session object has been modified
#     return render_template('payment_success.html', confirmation=confirmation)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import string
import datetime
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here_change_this_in_production'

# AWS Configuration
AWS_REGION = 'us-west-2'  # Update to your desired region
DYNAMODB_TABLE_USERS = 'Users'
DYNAMODB_TABLE_BOOKINGS = 'Bookings'
SNS_TOPIC_ARN = 'arn:aws:sns:your-region:your-account-id:your-sns-topic'  # Update with your ARN

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
sns_client = boto3.client('sns', region_name=AWS_REGION)

mock_travel_options = {
    'flights': [
        {'id': 'flight1', 'flight_number': 'AC101', 'airline': 'AirConnect',
         'departure_time': '06:00 AM', 'arrival_time': '08:00 AM', 'price': 150.00, 'duration': '2h 00m'},
        {'id': 'flight2', 'flight_number': 'SH202', 'airline': 'SkyHigh',
         'departure_time': '09:30 AM', 'arrival_time': '11:30 AM', 'price': 180.00, 'duration': '2h 00m'},
    ],
    'buses': [
        {'id': 'bus1', 'name': 'Express Lines', 'departure_time': '08:00 AM',
         'arrival_time': '12:00 PM', 'price': 25.00, 'total_seats': 20},
    ],
    'trains': [
        {'id': 'train1', 'number': 'REX001', 'name': 'Rail Express',
         'departure_time': '07:00 AM', 'arrival_time': '01:00 PM', 'price': 60.00},
    ],
    'hotels': [
        {'id': 'hotel1', 'name': 'Grand Plaza Hotel', 'location': 'New York', 
         'price_per_night': 120.00, 'rating': 4.5},
    ]
}

occupied_bus_seats = {
    'bus1': ['A1', 'A2', 'B3'],
}

# Helper Functions
def generate_unique_id(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_seat_numbers(item_id, total_seats=None):
    if 'bus' in item_id:
        seats = []
        occupied = occupied_bus_seats.get(item_id, [])
        num_rows = (total_seats + 3) // 4
        for row in range(num_rows):
            for col in range(1, 5):
                seat_number = f"{chr(65+row)}{col}"
                if len(seats) < total_seats:
                    seats.append({
                        'number': seat_number,
                        'occupied': seat_number in occupied
                    })
        return seats
    else:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_notification(message):
    try:
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject='Booking Notification'
        )
        return response
    except ClientError as e:
        print(f"Error sending notification: {e}")
        return None

def get_user(username):
    table = dynamodb.Table(DYNAMODB_TABLE_USERS)
    try:
        response = table.get_item(Key={'username': username})
        return response.get('Item')
    except ClientError as e:
        print(f"Error getting user: {e}")
        return None

def add_user(username, password):
    table = dynamodb.Table(DYNAMODB_TABLE_USERS)
    try:
        table.put_item(
            Item={
                'username': username,
                'password': password
            },
            ConditionExpression='attribute_not_exists(username)'
        )
        return True
    except ClientError as e:
        print(f"Error adding user: {e}")
        return False

def add_booking(booking):
    table = dynamodb.Table(DYNAMODB_TABLE_BOOKINGS)
    try:
        table.put_item(Item=booking)
        return True
    except ClientError as e:
        print(f"Error adding booking: {e}")
        return False

@app.route('/')
def index():
    return redirect(url_for('signin'))

# Authentication Routes
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user(username)
        if user and user['password'] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if get_user(username):
            flash('Username already exists', 'error')
        elif add_user(username, password):
            flash('Account created! Please sign in', 'success')
            return redirect(url_for('signin'))
        else:
            flash('Error creating account', 'error')
    
    return render_template('signup.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('signin'))
    return render_template('home.html', username=session['username'])

# Booking Routes
@app.route('/book/<transport_type>', methods=['GET', 'POST'])
def book_transport(transport_type):
    if 'username' not in session:
        return redirect(url_for('signin'))

    if request.method == 'POST':
        session['current_booking'] = {
            'type': transport_type,
            'source': request.form.get('source'),
            'destination': request.form.get('destination'),
            'date': request.form.get('date'),
        }
        return redirect(url_for(f'{transport_type}_available'))

    return render_template(f'{transport_type}.html')

@app.route('/book/<transport_type>/available')
def transport_available(transport_type):
    if 'username' not in session:
        return redirect(url_for('signin'))

    booking = session.get('current_booking')
    if not booking or booking['type'] != transport_type:
        return redirect(url_for(f'book_{transport_type}'))

    options = mock_travel_options.get(transport_type, [])
    return render_template(f'{transport_type}_available.html', 
                         options=options,
                         booking=booking)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if 'username' not in session:
        return redirect(url_for('signin'))

    booking = session.get('current_booking')
    if not booking:
        return redirect(url_for('home'))

    if request.method == 'POST':
        booking_id = generate_unique_id()
        booking_details = {
            'booking_id': booking_id,
            'username': session['username'],
            'type': booking['type'],
            'status': 'confirmed',
            'created_at': datetime.datetime.now().isoformat(),
            'details': booking
        }

        if add_booking(booking_details):
            send_notification(
                f"New booking: {booking_id}\n"
                f"Type: {booking['type']}\n"
                f"User: {session['username']}"
            )
            session.pop('current_booking')
            flash('Booking confirmed!', 's-uccess')++++
            return redirect(url_for('home'))
        else:
            flash('Error confirming booking', 'error')

    return render_template('payment.html', booking=booking)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
