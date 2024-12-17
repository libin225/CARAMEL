from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from projname import settings


# Create your views here.

def about(request):
    return render(request,"about.html")

def booking(request):
    return render(request,"booking.html")

def contact(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        message=request.POST.get("message")
        subject = f"message from {firstname} {lastname}"
        message=f"message from:{firstname} {lastname}\n email:{email}\n\n {message}"
        email_from =settings.EMAIL_HOST_USER
        recipient_list =[settings.ADMIN_EMAIL]
        try:
            send_mail(subject,message,email_from,recipient_list)
            messages.success(request,"your messages has been send successfully")
            return redirect("contact")
        except Exception as e:
            messages.error(request,"An error occurred while sending your message.Please try again.")
            return redirect("contact")


    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")

def menu(request):
    return render(request,"menu.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        date= request.POST.get("date")
        time= request.POST.get("time")
        customers= request.POST.get("customers")
        subject = "Welcome to CARAMEL"
        message = f"Hi {name} ,your table has been booked"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "your table has been booked successfully")
            return redirect("form")
        except Exception as e:
            messages.error(request, "An error occurred while booking your table.Please try again.")
            return redirect("form")

    return render(request,"form.html")
