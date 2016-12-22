from crontab import CronTab
#init cron
cron   = CronTab()
import os
dirPath = os.path.dirname(os.path.realpath(__file__))
# print(dirPath)
#add new cron job
job  = cron.new(command='{}/venv/bin/python {}/run.py >> /var/log/fifabot.log 2>&1'.format(dirPath, dirPath))

#job settings
# job.hour.every(1)
job.minute.every(5)
print(cron.render())
