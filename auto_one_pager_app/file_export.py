import sys
sys.path.append('../')

import os 
os.environ['DJANGO_SETTINGS_MODULE'] = 'one_pager.settings'

from django.conf import settings
from django.core.management import setup_environ

from auto_one_pager_app.models import Task, SubTask, Meeting
from django.core.files import File

#setup_environ(settings)

f=open('one_pager.txt', 'w')
output_file=File(f)

# add an indent function to add padding to lines
def indent(strval, amount):
    ch=' '
    padding = amount*ch
    return padding + strval
    
# add a function to check if done or on priority list
def check_done_priority(object):
    if object.done==False:
        return '-bold'
    elif (object.done==True) and (object.priority==False):
        return '-italics'
    else:
        return ''

with open('one_pager.txt', 'w') as f:
  output_file=File(f)
  # first add the title header on the first line
  output_file.write("Accomplishments from Last Week's Priority List\n".encode("UTF-8"))

  for item in Task.objects.all():
    # if it is a root task then just add it with one indent
    
    # create string to add
    linetoadd=str(item.task_num) + '. ' + item.title + ' ' + '(' +str(item.est_time_hours) + ' Hours' + ')' + '[' + str(item.actual_time_hours)+ ' Hours' + ']' + '\n'
    # add an indent to the task title
    linetoadd=indent(linetoadd, 4)
    output_file.write(linetoadd)
    # now check through all tasks again to find a child
    # note this is only one level down - no more
    for item1 in SubTask.objects.all():
      # if you find a child indent and add to file
      if item1.parent==item:
        sublinetoadd=chr(item1.subtask_num+96) + '. ' + item1.title
        # add formatting based on done or priority
        sublinetoadd=sublinetoadd + check_done_priority(item1)+'\n'
        # add proper indent to the task title
        sublinetoadd=indent(sublinetoadd, 8)    
        output_file.write(sublinetoadd)

  # add an extra line to separate tasks and meetings
  output_file.write('\n')

  # add Meeting field
  # first calculate all of the hours of meetings
  total_hrs_meeting = 0
  for item in Meeting.objects.all():
    total_hrs_meeting+=item.time_length_hours  
  output_file.write('Meetings last week' + ' (' +str(total_hrs_meeting) +' Hours)-italics\n')
  # add all of the meetings with indent (and a bullet point...or dot)
  for item in Meeting.objects.all():
    meetinglinetoadd='.' + item.title + '\n'
    # add indent
    meetinglinetoadd=indent(meetinglinetoadd,4)
    output_file.write(meetinglinetoadd)



