import time
import datetime
import random
import CONF

sections = ['SECTION'+str(i) for i in range(1,6)]
cases = ['CASE'+str(i) for i in range(1,11)]
status = ['STATUS'+str(i) for i in range(1,11)]
result = ["PASS", "FAIL"]


time_str = ['2020/07/02', '2020/07/12', '2020/07/03', '2020/07/13', '2020/08/14']


def log_generator():
	log = ""
	log += ">>> " + sections[random.randint(0,4)] + " <<<\n"
	log += "--- Time: " + time_str[random.randint(0,len(time_str)-1)] + " ---\n"
	for _ in range(random.randint(1,3)):
		log += "- " + cases[random.randint(0,9)] + ' -\n'
		for _ in range(random.randint(1,3)):
			log += "[" + result[random.randint(0,1)] + "] " + status[random.randint(0,9)] + '\n'
			log += "nonsense:afnonfoansfnabufbegblbeg\n"
	return log



f = open(CONF.currentlyRunningLog,mode='a')
for _ in range(10):
	f.write(log_generator())
	#time.sleep(1)
f.close()
