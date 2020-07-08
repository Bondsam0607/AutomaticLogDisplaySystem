import re
import sys

class log_parser:
	def __init__(self, target_log):
		f = open(target_log)
		self.log = f.readlines()
		f.close()
		self.search_time_pattern = r'\d{4}\/\d{2}\/\d{2}'
	def extract_log(self):
		result = []
		for line_num in range(len(self.log)):
			if self.log[line_num][:3] == '---':
				time = re.search(self.search_time_pattern, self.log[line_num], re.M|re.I).group()
				if not time:
					print("no time info found")
					sys.exit(-1)
				else:
					for ln in range(line_num+1, len(self.log)):
						if self.log[ln][:3] == '---':
							break
						if self.log[ln][0] == '-' and self.log[ln][1] == ' ':
							localTitle = self.log[ln].strip()[2:-2]
							#print(localTitle)
							for line in self.log[ln+1:]:
								if line[0] == '-':
									break
								if line[:6] in ["[PASS]", "[FAIL]"]:
									if len(line[8:].strip())>255:
										localContent = line[8:].strip()[:250]+'...'
									else:
										localContent = line[8:].strip()
									result.append([line[1:5], localTitle, localContent, time])
		return result






if __name__ == '__main__':
	log_parser = log_parser("tmpRedfish-10.8.21.113.log")
	log_parser.extract_log()




