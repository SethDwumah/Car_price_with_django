from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from .models import CarPrice
from .forms import CarPriceForm
import os , joblib
# Create your views here.


model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'car_price_model', 'model.pkl')
scaler_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'car_price_model', 'scaler.pkl')
trained_model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def home(request):
    return render(request, 'car_price/home.html')

def user_input(request):
    if request.method=='POST':
        form = CarPriceForm(request.POST)
        if form.is_valid():
            make = form.cleaned_data['make']
            year = form.cleaned_data['year']
            engine_fuel_type = form.cleaned_data['engine_fuel_type']
            engine_hp = form.cleaned_data['engine_hp']
            engine_cylinders  = form.cleaned_data['engine_cylinders']
            transmission_type = form.cleaned_data['transmission_type']
            driven_wheels = form.cleaned_data['driven_wheels']
            number_of_doors = form.cleaned_data['number_of_doors']
            vehicle_size = form.cleaned_data['vehicle_size']
            vehicle_style = form.cleaned_data['vehicle_style']
            highway_mpg = form.cleaned_data['highway_mpg']
            city_mpg = form.cleaned_data['city_mpg']
            popularity =form.cleaned_data['popularity']

            feature_list = [make, year,engine_fuel_type,engine_hp,engine_cylinders,
                            transmission_type,driven_wheels,number_of_doors,
                            vehicle_size,vehicle_style,highway_mpg,city_mpg,popularity]
            float_values = [[float(value) for value in feature_list]]
            transformed_data = scaler.transform(float_values)
            print(transformed_data.shape)
            prediction = trained_model.predict(transformed_data)
            CarPrice.objects.create(
                make=make, year=year, engine_fuel_type=engine_fuel_type, engine_hp=engine_hp ,engine_cylinders=engine_cylinders,
                            transmission_type =transmission_type ,driven_wheels = driven_wheels,number_of_doors =number_of_doors,
                            vehicle_size = vehicle_size,vehicle_style = vehicle_style, highway_mpg=highway_mpg, city_mpg=city_mpg,popularity=popularity, price =prediction
            )
            price_of_car = {
                "Results": prediction
            }
            return render(request,'car_price/results.html',price_of_car)
    else:
        form = CarPriceForm()
    return render(request, 'car_price/input_data.html',{'form':form})

def show_results(request):
    prediction_results =CarPrice.objects.last()
    context ={
        "Results":prediction_results
    }
    return render(request, 'car_price/results.html',context)



def Signup(request):
    if request.method =='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'car_price/register.html')

def Login(request):
    if request.method =='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request,user)

                return redirect('home')
    else:
        form=LoginForm()
    return render(request, 'car_price/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('home')