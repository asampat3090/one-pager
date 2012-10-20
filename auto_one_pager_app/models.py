from django.db import models
from django.contrib import admin
#from button_class import ButtonAdmin, Button

#class FooAdmin(ButtonAdmin):
    
#    def bar(self, request, obj=None):
#        if obj != None: 
#            obj.bar()
#            return None # Redirect or Response or None
#    bar.short_description='Example button'
    
#    list_buttons = [ bar ]
#    change_buttons = [ bar ]

#class Test(ButtonAdmin):
#    buttons = (
#               Button('test', "A Test Button", needSuperUser=False),
#               Button('redirect', "A redirect", needSuperUser=False),
#               )
    
#    def tool_test(self, request, obj, button):
#        return 'templates/test.html', {"message" : "a test"}
    
#    def tool_redirect(self, request, obj, button):
#        return HttpResponseRedirect('/somewhere')

# import the mptt class to enable heirarchal trees
# import mptt

# Create your models here.
class Task(models.Model):
  # task number as to be displayed in output file
  task_num = models.IntegerField(default=0)
  title = models.CharField(max_length=2000)
  # assume you will never haave a task more than 999 hours...i hope
  est_time_hours = models.DecimalField(max_digits=5, decimal_places=2)
  actual_time_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
  # add boolean fields we care about
  priority = models.BooleanField(default=False)
  done = models.BooleanField(default=False)
 
  # describe Task by its title
  def __unicode__(self):
    return self.title


class SubTask(models.Model):
	subtask_num = models.IntegerField(default=0)
	title = models.CharField(max_length=2000)
	priority = models.BooleanField(default=False)
	done = models.BooleanField(default=False)
	# have a reference to its parent
	parent = models.ForeignKey(Task)
	# describe SubTask by its title
	def __unicode__(self):
		return self.title
			
class Meeting(models.Model):
  title = models.CharField(max_length=2000)
  time_length_hours= models.DecimalField(max_digits=5, decimal_places=2)
  # describe Meeting by its title
  def __unicode__(self):
    return self.title

class TaskAdmin(admin.ModelAdmin):
  fields=(("task_num"),("title","est_time_hours","actual_time_hours"),("priority","done"))
  list_display =["task_num","title","est_time_hours","actual_time_hours","priority","done"]

class SubTaskAdmin(admin.ModelAdmin):
	fields=(("subtask_num", "parent"),("title"),("priority","done"))
	list_display =["subtask_num","parent","title","priority","done"]
	
class MeetingAdmin(admin.ModelAdmin):
    list_display=["title","time_length_hours"]

# mptt.register(Task)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
admin.site.register(Meeting, MeetingAdmin)
