from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
    
class Mission(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateField()
    company_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    numberApplied = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("mission_detail", kwargs={"slug": self.slug})
    
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    status = models.CharField(max_length=255)
    assignee_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class ApplyMission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    AleradyApplied = models.BooleanField(null=True)
    
    def __str__(self):
        return f"{self.user} applied to {self.mission}"    

class Waitlist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    applies = models.ManyToManyField(ApplyMission)
    
    def __str__(self):
        return f"Waitlist for {self.user}"
    
class Review(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_reviews')
    target_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_reviews')
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Payment(models.Model):
    amount = models.FloatField()
    status = models.CharField(max_length=255)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)