from django.db import models

# Create your models here.

SECTION_CHOICES =[

    ('FastFoods', 'Fast Foods'),
    ('Snacks', 'Snacks/BreakFasts'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Desserts', 'Desserts'),
]


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=50,choices=SECTION_CHOICES)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='menu_images/',blank=True,null=True,default="")

    def __str__(self):
        return self.name
    

class Order(models.Model):
    item= models.ForeignKey("MenuItem",on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    address= models.TextField()
    phone_number= models.CharField(max_length=15)
    email= models.EmailField(max_length=254)
    status= models.CharField(max_length=100, default='Pending')
    created_at= models.DateTimeField(auto_now_add=True)
    items_json = models.CharField(max_length=5000, blank=True, default='')

    def __str__(self):
        return f"Order for {self.item.name} by {self.name}"
    


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="updates")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

# class OrderUpdate(models.Model):
#     update_id =models.AutoField(primary_key=True)
#     order_id =models.IntegerField(default="")
#     update_desc =models.CharField(max_length=5000)
#     timestamp = models.DateField(auto_now_add=True)
    

#     def __str__(self):
#         return self.update_desc[0:7] + "..."
    
