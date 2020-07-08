import re
import sys


class log_parser:
	def __init__(self, target_log):
		f = open(target_log)
		self.log = f.readlines()
		f.close()
		self.search_time_pattern = r'\d{4}\/\d{2}\/\d{2}'
		self.logLength = len(self.log)
	def extract_log(self):
		result = []
		for line_num in range(self.logLength):
			if self.log[line_num][:3] == ">>>":
				localSection = self.log[line_num][4:-5]
				#print(localSection)
				for ln in range(line_num+1, self.logLength):
					if self.log[ln][:3] == ">>>":
						break
					if self.log[ln][:3] == "---":
						localTime = re.search(self.search_time_pattern, self.log[ln], re.M|re.I).group()
						#print(localTime)
						for lnn in range(ln+1, self.logLength):
							if self.log[lnn][:3] == "---":
								break
							if self.log[lnn][0] == "-" and self.log[lnn][1] == " ":
								localCase = self.log[lnn][2:-2]
								#print(localCase)
								for line in self.log[lnn+1:]:
									if line[0] == '-':
										break
									if line[:6] in ["[PASS]", "[FAIL]"]:
										localResult = line[1:5]
										localStatus = line[6:].strip()
										#print(localStatus)
										result.append([localSection, localCase, localResult, localStatus, localTime])
		return result

if __name__ == '__main__':
	print(log_parser('test.log').extract_log())
