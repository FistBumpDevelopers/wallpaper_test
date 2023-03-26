from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


class Wallpaper(models.Model):
    Title = models.CharField(max_length=500 ,blank=True)
    Sauce = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    Image = models.ImageField(upload_to='images2k/', blank=False)
    Image_1080 = models.ImageField( upload_to='images1080/',null=True,blank=True)
    Image_720 = models.ImageField( upload_to='images720/',null=True,blank=True)
    thumbnail = models.ImageField( upload_to='thumbnails/',null=True,blank=True)
    tags = TaggableManager(blank=True)

    combined_field = models.CharField(max_length=300, blank=True)

    
    ANIME = 'AN'
    GAMES = 'GM'
    MOVIES = 'MV'
    CHOICES = (
        (ANIME, 'Anime'),
        (GAMES, 'Games'),
        (MOVIES, 'Movies'),
    )
    my_choice_field = models.CharField(
        max_length=2,
        choices=CHOICES,
        default=ANIME,
    )

    class Meta:
        ordering = ['-created_at']

    Dimentions = models.CharField(
        max_length=20,  blank=True
    )   

    # AUTO CREATE thumbnails 1080 720
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        img = img.convert("RGB")
        img.thumbnail((300,600))
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG')
        self.thumbnail.save(f'{self.Image.name}.thumbnail.jpg',ContentFile(thumb_io.getvalue()), save=False)

        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        img = img.convert('RGB')
        width, height = img.size
        if width==height:
            size = (1080,1080)
        else:
            size = (1920,1920)

        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG')
        self.Image_1080.save(f'{self.Image.name}.Image_1080.jpg',ContentFile(thumb_io.getvalue()), save=False)

        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        img = img.convert('RGB')
        width, height = img.size
        if width==height:
            size = (720,720)
        else:
            size = (1280,1280)

        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG')
        self.Image_720.save(f'{self.Image.name}.Image_720.jpg',ContentFile(thumb_io.getvalue()), save=False)
        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        width, height = img.size
        if width>height:
            self.Dimentions = "Desktop"
        elif width<height:
            self.Dimentions = "Mobile"
        else :
            self.Dimentions = "Square"   
        super().save(*args, **kwargs)
        tag_names = self.tags.names()
        self.combined_field = f"{self.Title} {self.Sauce} {' '.join(tag_names)}"
        super().save(*args, **kwargs)

    

  
    
        
