from django.conf import settings
from django.db import models
from django.urls import reverse
User = settings.AUTH_USER_MODEL
from django.db.models.signals import pre_save, post_save
from main.utils import unique_key_generator, unique_slug_generator

from django.core.validators import RegexValidator

ADDRESS_TYPE = [
			("Home", "Home"),
			("Office", "Office"),
			("Shop", "Shop"),
			("Business", "Business"),
			("Home Business", "Home Business"),
			("Warehouse", "Warehouse"),
			("Other", "Other"),
		]

STATE_FIELD = [
			('Andhra Pradesh', 'Andhra Pradesh'), 
			('Arunachal Pradesh', 'Arunachal Pradesh'), 
			('Assam', 'Assam'), 
			('Bihar', 'Bihar'), 
			('Chattisgarh', 'Chattisgarh'), 
			('Goa', 'Goa'), 
			('Gujarat', 'Gujarat'), 
			('Haryana', 'Haryana'), 
			('Himachal Pradesh', 'Himachal Pradesh'), 
			('Jharkhand', 'Jharkhand'), 
			('Jammu and Kashmir', 'Jammu and Kashmir'), 
			('Karnataka', 'Karnataka'), 
			('Kerala', 'Kerala'), 
			('Madhya Pradesh', 'Madhya Pradesh'), 
			('Maharashtra', 'Maharashtra'), 
			('Manipur', 'Manipur'), 
			('Meghalaya', 'Meghalaya'), 
			('Mizoram', 'Mizoram'), 
			('Nagaland', 'Nagaland'), 
			('Odisha', 'Odisha'),
		    ('Punjab', 'Punjab'), 
			('Rajasthan', 'Rajasthan'), 
		    ('Sikkim', 'Sikkim'), 
			('Tamil Nadu', 'Tamil Nadu'), 
			('Telangana', 'Telangana'), 
			('Tripura', 'Tripura'), 
			('Uttar Pradesh', 'Uttar Pradesh'),		
			('Uttarakhand', 'Uttarakhand'), 
			('West Bengal', 'West Bengal'),
		]

class Address(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=140, default="Title")
	address_type = models.CharField(max_length=300, choices=ADDRESS_TYPE)
	address_line = models.CharField(max_length=300)
	landmark = models.CharField(max_length=300)
	area = models.CharField(max_length=50)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=500, choices=STATE_FIELD)
	pincode = models.CharField(max_length=6, validators=[RegexValidator(regex=r'^[0-9]{6}$')])
	slug = models.SlugField(null=True, blank=True, unique=True, max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True)
	seller = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('address-edit', kwargs={"slug":self.slug})

	def get_delete_absolute_url(self):
		return reverse('address-delete', kwargs={"slug":self.slug})


def address_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(address_pre_save_receiver, sender=Address)