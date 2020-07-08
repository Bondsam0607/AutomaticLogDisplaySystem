from insert_sql import Manipulate_SQL
from log_parser import log_parser
import CONF
import time

log_content = log_parser(CONF.currentlyRunningLog).extract_log()

mani = Manipulate_SQL()
while True:
	mani.truncate(CONF.currLogTable)
	for info in log_content:
		mani.insert(CONF.currLogTable, info)
		mani.insert(CONF.accLogTable, info)
	time.sleep(3)
