from django.forms import ModelForm, ValidationError
from catalog.models import Work,Image


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields=["id","title","work_type","media","dims_height","dims_width","dims_depth","work_date","price","description","notes","sold_date","sold_to","sale_price","inscription","work_key","status"]
    def clean_work_key(self):
        # convert to uppercase and verify that the key is unique
        data = self.cleaned_data["work_key"]
        data = data.upper()
        insert = self.instance.pk == None
        if insert:
            keycount = Work.objects.filter(work_key=data).count()
            if keycount > 0:
                raise ValidationError(
                    [
                        ValidationError(("Key %(value)s is already used"),code="invalid",params={"value":data})
                    ]
                )
        
            
        return data

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields=["id","image","image_type","image_file_name","image_notes","image_source"] 

