from django.db import models
from a1site.utils import format_dimension_string



work_type_choices = [("painting","painting"),("monotype","monotype"),("tile","tile"), ("sculpture","sculpture")]
media_choices = [("oil on wood","oil on wood"),("oil on canvas","oil on canvas"), ("ink on paper","ink on paper"), ("watercolor","watercolor"), ("ceramic","ceramic"),("oil on canvas","oil on canvas")]
image_type_choices = [("primary","primary"),("alternate","alternate"),("documentation only","documentation only"),("detail","detail"),("previous version","previous version")]
available_choices = [("available","available"),("unavailable","unavailable"),("sold","sold"),("painted over","painted over")]

class Work(models.Model):
    work_key = models.CharField("key",max_length = 12, unique=True)
    title = models.CharField(max_length = 250)
    # def __str__(self):
    #     if self.work_key == None or self.title == None:
    #         return "new entry"
    #     else:
    #         return self.work_key + " " + self.title
    work_type = models.CharField("type", max_length=100,choices=work_type_choices)
    media = models.CharField(max_length = 100,choices=media_choices)

    dims_height = models.DecimalField("height",max_digits = 6,decimal_places = 2,null=True,blank=True)
    dims_width = models.DecimalField("width",max_digits = 6,decimal_places = 2,null=True,blank=True)
    dims_depth = models.DecimalField("depth",max_digits = 6,decimal_places = 2,null=True,blank=True)
    dims_unit = models.CharField(max_length = 20,default="inches")
 #   @admin.display(
 #       boolean=True,
 #       ordering="dims_height",
 #       description="Dimensions",
 #   )
    @property
    def dimensions(self):
         return (format_dimension_string(self.dims_height,self.dims_width,self.dims_depth)) 
    work_date = models.CharField("date",max_length = 10,null=True,blank=True)
    price = models.DecimalField(max_digits = 9,decimal_places=2,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    sold_date = models.DateField(null=True,blank=True)
    sold_to = models.CharField(max_length = 100,null=True,blank=True)
    sale_price = models.DecimalField(max_digits = 9,decimal_places=2,null=True,blank=True)
    inscription = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, null=False,default="available",choices=available_choices)
 

class Image(models.Model):
    work = models.ForeignKey(Work,on_delete=models.CASCADE,verbose_name="related image")
    image_file_name = models.CharField(max_length=200,null=True,blank=True)
    image_source = models.CharField(max_length=256,null=True,blank=True)
    image_notes = models.TextField(null=True,blank=True)
    image = models.ImageField()
    image_type = models.CharField(max_length=50,choices=image_type_choices)
    def __str__(self):
        return '{}'.format(self.image_file_name or self.pk)
    

