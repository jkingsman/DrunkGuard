from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
from random import randint
from datetime import datetime, date, time

requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def init_hook(conduit):
	currentHour = datetime.now().hour
	currentWeekday = datetime.today().weekday()
	
	#numerical days we wil check the time for (0-6, starting Monday)
	blockedDays =[4,5,6]
	
	#hour (24 hr format) that the night begins and ends
	nightStart = 20 
	nightEnd = 6

	if currentWeekday in blockedDays:
		if (currentHour <= nightEnd ) or (currentHour >= nightStart):
			conduit.info(2, 'Hm... are you drunk?')
			for x in range(0, 3):
				rand1 = randint(0, 150)
			        rand2 = randint(0, 150)
			        sum = rand1 + rand2

			        sumAttempt = raw_input('What is ' + str(rand1) + ' + ' + str(rand2) + '? ')
			        if int(sumAttempt) == sum:
			                conduit.info(2, 'Well done!')
			        else:
			                raise PluginYumExit('That\'s not right... You\'re drunk! No yum for you.')
			#close loop
			conduit.info(2, 'Looks like you\'re sober enough to use yum - be careful!')
		else:
			 conduit.info(2, 'Happy trails from the drunkGuard module. Have a great weekend!')	
