from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from .models import MenuItem,Order,OrderUpdate
from django.urls import reverse
from .forms import OrderForm


def home(request):
    li = {

        'food_content': [
            {'name': 'Panner Masala', 'content': 'Creamy and rich, with a delightful blend of spices. Perfect with naan or rice','src':'myapp/images/pannerMasala.jpg'},
            {'name': 'Chole Bhature', 'content': 'Test is nice','src':'myapp/images/chole.jpg'},
            {'name': 'Pav-Bhaji', 'content': 'Delicious test','src':'myapp/images/pavbhaji.jpg'},
            {'name': 'Veg-Maratha', 'content': 'Good test','src':'myapp/images/p4.jpg'},
            {'name': 'Bhaji', 'content': 'Fabalous test','src':'myapp/images/p5.jpg'},
            {'name': 'Poha', 'content': 'Yummy test','src':'myapp/images/p6.jpg'},

        ]
    }
    return render(request, "myapp/home.html", li)


def menu_page(request):
    # Define all the sections you want to display
    sections = ['FastFoods', 'Snacks', 'Lunch', 'Dinner', 'Desserts']
    
    # Use a dictionary comprehension to dynamically fetch menu items by section
    menu_items = {
        section.lower(): MenuItem.objects.filter(section=section) for section in sections
    }
    
    context = {
        **menu_items,  # Unpack the dynamically created dictionary into the context
    }
    
    return render(request, "myapp/components/menu.html", context)

# def order_product(request, id):
#     menu_item = get_object_or_404(MenuItem, id=id)

#     if request.method == "POST":
#         # Capture form data
#         name = request.POST.get('name')
#         address = request.POST.get('address')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')

#         # Validate inputs (optional, for additional validation)
#         if not name or not address or not phone_number or not email:
#             return render(request, 'myapp/components/order_form.html', {
#                 'menu_item': menu_item,
#                 'error': "All fields are required!"
#             })

#         # Save the order
#         Order.objects.create(
#             item=menu_item,
#             name=name,
#             address=address,
#             phone_number=phone_number,
#             email=email
#         )
#         return redirect('order_success')  # Redirect to success page

#     # If GET request, render the form
#     return render(request, 'myapp/components/order_form.html', {'menu_item': menu_item})



def order_product(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)

    if request.method == "POST":
        # Capture form data
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        # Validate inputs
        if not name or not address or not phone_number or not email:
            return render(request, 'myapp/components/order_form.html', {
                'menu_item': menu_item,
                'error': "All fields are required!"
            })

        # Save the order and capture the instance
        order = Order.objects.create(
            item=menu_item,
            name=name,
            address=address,
            phone_number=phone_number,
            email=email
        )

        # Redirect to success page with the order ID
        return redirect(reverse('order_success', kwargs={'order_id': order.id}))

    # Render the order form for a GET request
    return render(request, 'myapp/components/order_form.html', {'menu_item': menu_item})

# def order_success(request, order_id):
#     # Get the order by ID
#     order = get_object_or_404(Order, id=order_id)
#     return render(request, 'myapp/components/order_success.html', {'order': order})

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)

    # Add initial update for the order
    OrderUpdate.objects.create(
        order_id=order.id,
        update_desc="Order placed successfully."
    )

    return render(request, "myapp/components/order_success.html", {"order": order})

# def order_success(request):
    
#     #return HttpResponse("Thank You for Your Order! We have received your order and will process it shortly.")
#     return render(request, 'myapp/components/order_success.html')
# def menu_page(request):

#     fastfoods = MenuItem.objects.filter(section='FastFoods')
#     snacks = MenuItem.objects.filter(section='Snacks')
#     lunch = MenuItem.objects.filter(section='Lunch')
#     dinner = MenuItem.objects.filter(section='Dinner')
#     desserts = MenuItem.objects.filter(section='Desserts')

#     context={

#         'fastfoods':fastfoods,
#         'snacks': snacks,
#         'lunch': lunch,
#         'dinner':dinner,
#         'desserts': desserts,
#     }
#     return render(request,"myapp/components/menu.html",context)



# def Ordertrack(request):
#     if request.method == "POST":
#         orderId = request.POST.get('orderId', '').strip()
#         email = request.POST.get('email', '').strip()
#         try:
#             # Fetch the order using orderId and email
#             order = Order.objects.filter(id=orderId, email=email).first()
#             if order:
#                 # Fetch updates related to the order
#                 updates = OrderUpdate.objects.filter(order_id=orderId)
#                 update_list = [
#                     {
#                         'text': update.update_desc,
#                         'time': update.timestamp.strftime('%Y-%m-%d'),
#                     } for update in updates
#                 ]

#                 # Prepare the response
#                 response = {
#                     "status": "success",
#                     "updates": update_list,
#                     "itemsJson": {
#                         "Item": order.item.name,
#                         "Name": order.name,
#                         "Address": order.address,
#                         "Phone": order.phone_number,
#                         "Status": order.status,
#                         "Email": order.email,
#                         "OrderedAt": order.created_at.strftime('%Y-%m-%d %H:%M:%S')
#                     }
#                 }
#                 return JsonResponse(response)
#             else:
#                 # If no order found
#                 return JsonResponse({"status": "noitem"}, status=404)
#         except Exception as e:
#             # Handle any unexpected error
#             return JsonResponse({"status": "error", "message": str(e)}, status=500)

#     return render(request, "myapp/components/tracking.html")

# def Ordertrack(request):
#     if request.method == "POST":
#         try:
#             # Parse request data
#             data = json.loads(request.body)
#             order_id = data.get("orderId", "")
#             email = data.get("email", "")

#             # Retrieve the order
#             order = Order.objects.filter(id=order_id, email=email).first()
#             if order:
#                 # Retrieve updates for the order
#                 updates = OrderUpdate.objects.filter(order_id=order_id)
#                 updates_list = [
#                     {"text": update.update_desc, "time": update.timestamp.strftime("%Y-%m-%d %H:%M:%S")}
#                     for update in updates
#                 ]
                
#                 # Construct response
#                 response_data = {
#                     "status": "success",
#                     "updates": updates_list,
#                     "itemsJson": {
#                         "name": order.name,
#                         "item": order.item.name,
#                         "address": order.address,
#                         "phone_number": order.phone_number,
#                         "email": order.email,
#                         "status": order.status,
#                         "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
#                     },
#                 }
#                 return JsonResponse(response_data)

#             return JsonResponse({"status": "noitem"})
#         except Exception as e:
#             return JsonResponse({"status": "error", "message": str(e)})

#     return render(request, "myapp/components/tracking.html")

# def Ordertrack(request):
#     if request.method == "POST":
#         try:
#             # Parse request data
#             data = json.loads(request.body)
#             order_id = data.get("orderId", "").strip()
#             email = data.get("email", "").strip()

#             print(f"Tracking order for Order ID: {order_id}, Email: {email}") 

#             # Validate inputs
#             if not order_id or not email:
#                 return JsonResponse({"status": "error", "message": "Order ID and Email are required."})

#             # Retrieve the order

#             order = Order.objects.filter(id=order_id, email=email).first()
#             if order:
#                 print(f"Order found: {order}")  # Debug print
#                 # Retrieve updates for the order

#                 updates = OrderUpdate.objects.filter(order_id=order_id)
#                 updates_list = [
#                     {
#                         "text": update.update_desc,
#                         "time": update.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
#                     }
#                     for update in updates
#                 ]

#                 # Construct response
#                 response_data = {
#                     "status": "success",
#                     "updates": updates_list,
#                     "itemsJson": {
#                         "name": order.name,
#                         "item": order.item.name,
#                         "address": order.address,
#                         "phone_number": order.phone_number,
#                         "email": order.email,
#                         "status": order.status,
#                         "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
#                     },
#                 }
#                 return JsonResponse(response_data)

#             # If no order found
#             return JsonResponse({"status": "noitem", "message": "No order found for the given details."})

#         except Exception as e:
#             return JsonResponse({"status": "error", "message": str(e)})

#     return render(request, "myapp/components/tracking.html")


def Ordertrack(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(id=orderId, email=email)
            if order.exists():  # Check if the order exists
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp.strftime('%Y-%m-%d %H:%M:%S')})
                
                # Return order details and updates as a JSON response
                response = {
                    "status": "success",
                    "updates": updates,
                    "itemsJson": order[0].items_json  # Assuming items_json is a field in your Orders model
                }
                return JsonResponse(response)
            else:
                # If no order found
                return JsonResponse({"status": "noitem"})
        except Exception as e:
            # Handle errors and return a generic error response
            return JsonResponse({"status": "error", "message": str(e)})

    # Return the tracking page for GET requests
    return render(request, 'myapp/components/tracking.html')


def reservations(request):
    return render(request,"myapp/components/reservations.html")

def contact(request):
    return render(request,"myapp/components/contact.html")

def search(request):
    query=request.GET.get('q','').strip() 
    results = MenuItem.objects.filter(name__icontains=query) if query else []
    return render(request,"myapp/components/search.html",{'query':query,'results': results})
# from math import ceil

# def home(request):
#     food_items = [
#         {'name': 'Panner Masala', 'content': 'Creamy and rich, with a delightful blend of spices. Perfect with naan or rice.', 'src': 'myapp/images/p1.jpg'},
#         {'name': 'Chole Bhature', 'content': 'Test is nice.', 'src': 'myapp/images/p2.jpg'},
#         {'name': 'Pav-Bhaji', 'content': 'Delicious test.', 'src': 'myapp/images/p3.jpg'},
#         {'name': 'Biryani', 'content': 'Flavored rice with spices and tender meat.', 'src': 'myapp/images/p4.jpg'},
#         {'name': 'Rajma Chawal', 'content': 'Simple and wholesome.', 'src': 'myapp/images/p5.jpg'},
#     ]
#     n = len(food_items)
#     nSlides = n // 3 + ceil((n / 3) - (n // 3))  # Adjust for slides of 3 items each
#     allProds = [food_items[i:i + 3] for i in range(0, len(food_items), 3)]  # Chunk items
#     params = {'allProds': allProds, 'nSlides': nSlides}
#     return render(request, 'myapp/home.html', params)
