from django.db import models
from django.utils import timezone

class Xodim(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    lavozim = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ism} {self.familiya}"
    
class Davomat(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, related_name='davomat')
    kelgan_vaqti = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.xodim} - {self.kelgan_vaqti.strftime('%Y-%m-%d %H:%M:%S')}"