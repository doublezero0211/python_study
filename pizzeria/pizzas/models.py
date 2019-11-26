from django.db import models

# Create your models here.
class Pizza(models.Model):
	"""披萨种类"""
	text = models.CharField(max_length=200)
	
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Topping(models.Model):
    """某种披萨的配料"""
    pizza = models.ForeignKey("Pizza",on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'toppings'
    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50]+"..."
        else:
            return self.text
