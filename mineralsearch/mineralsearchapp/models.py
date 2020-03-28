from django.db import models


class Mineral(models.Model):
    """mineral model describing attributes of each mineral instance"""
    name = models.CharField(max_length=1000, unique=True)
    image_filename = models.CharField(max_length=1000)
    image_caption = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    formula = models.CharField(max_length=1000)
    strunz_classification = models.CharField(max_length=1000)
    crystal_system = models.CharField(max_length=1000)
    unit_cell = models.TextField(max_length=1000)
    color = models.CharField(max_length=1000)
    crystal_symmetry = models.CharField(max_length=1000)
    cleavage = models.CharField(max_length=1000)
    mohs_scale_hardness = models.CharField(max_length=1000)
    luster = models.CharField(max_length=1000)
    streak = models.CharField(max_length=1000)
    diaphaneity = models.CharField(max_length=1000)
    group = models.CharField(max_length=1000)
    optical_properties = models.CharField(max_length=1000)
    refractive_index = models.CharField(max_length=1000)
    crystal_habit = models.CharField(max_length=1000)
    specific_gravity = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    @property
    def fields_lower(self):
        """retrieve all fields on instance, strip out underscores in 
        field name (meta fields have underscores), then return a list of 
        all these cleaned field names
        """  
        cleaned_fields = {}
        for field in self._meta.fields:
            if field.name not in ('image_filename', 'image_caption', 'id', 'name'):
                if field.value_to_string(self):
                    without_underscores = field.name.replace("_", " ")
                    cleaned_fields.update(
                        {without_underscores: field.value_to_string(self)}
                    )
        return cleaned_fields
