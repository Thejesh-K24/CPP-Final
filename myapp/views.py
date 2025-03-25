from django.shortcuts import render  # Import render

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserData  # Import your model
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'index.html') 

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request, "signup.html")

        # Save the user if passwords match
        user = UserData(name=name, email=email, password=password)  # Ensure User model has these fields
        user.save()

        messages.success(request, "Signup successful! You can now log in.")
        return redirect("login")  # Change to the appropriate login page

    return render(request, "signup.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists in UserData model with the provided username and password
        user = UserData.objects.filter(name=username, password=password).first()

        if user:  # User exists and password matches
            # Manually create a session for the user
            request.session['user_id'] = user.id  # Store the user ID (or any other info) in the session
            request.session['is_logged_in'] = True  # Optionally, set a flag to indicate that the user is logged in
            
            return redirect('traffic_update')  # Redirect to the desired page after successful login
        else:
            messages.error(request, "Invalid username or password")  # Show error message for failed login
    
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TrafficData

def traffic_update(request):
    if request.method == 'POST':
        # Extract data from the POST request
        junction_id = request.POST.get('Junction')
        number_of_vehicles = request.POST.get('Number_vehicle')

        # Validate data (for example, ensure number_of_vehicles is an integer)
        try:
            number_of_vehicles = int(number_of_vehicles)
        except ValueError:
            messages.error(request, "Please enter a valid number for the number of vehicles.")
            return redirect('traffic_update')  # Redirect back to the traffic_update page

        # Create and save the TrafficData object
        traffic_data = TrafficData(junction_id=junction_id, number_of_vehicles=number_of_vehicles)
        traffic_data.save()

        # Add a success message
        messages.success(request, 'Traffic data has been successfully updated!')

        # Redirect to the home or other desired page
        return redirect('index')  # You can change 'index' to any view you prefer

    # If it's a GET request, simply render the traffic_update page
    return render(request, 'traffic_update.html')


from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('index')






