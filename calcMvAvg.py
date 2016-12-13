# assumes input file is CSV format:
# 	- comma delimited(separated) values
#	- no quotes around values
# this WOULD NOT WORK if:
#	- any of the values in the csv contained commas
#	- any of the values in the csv were surrounded by quotes

ALPHA = 0.25

infile = open("query-output.csv", "r")
outfile = open("movingAvgs.csv", "w")

count = 0
prev_system = 0
prev_MA_values = []
for line in infile:
	if count == 0:
		# not sure why this DID need an endline char appended
		outfile.write('systemid,vvcounthistvlun,logfrom,logto,cpulatesttotalavgpct_MA,cpulatesttotalmaxpct_MA,porttotalbandwidthmbps_MA,delackspct_MA\n')
	if count > 0:
		values = line.split(',')
		# values[0] = systemid
		# values[1] = vvcounthistvlun
		# values[2] = logfrom
		# values[3] = logto
		# values[4] = cpulatesttotalavgpct
		# values[5] = cpulatesttotalmaxpct
		# values[6] = porttotalbandwidthmbps
		# values[7] = delackspct
		curr_system =  values[0]
		if curr_system != prev_system:
			# indicates start of next system's logs
			# "increment" prev_system
			prev_system = curr_system
			# write the initial M.A. values to output file
			# not sure why this didn't need an endline char appended
			w_line = ','.join(map(str, values))
			outfile.write(w_line)
			# update prev_MA_values for next M.A. calculation
			prev_MA_values = values
		else:
			# calculate M.A.s for each metric
			cpu_MA = (ALPHA * float(values[4])) + ((1.0 - ALPHA) * float(prev_MA_values[4]))
			cpuMax_MA = (ALPHA * float(values[5])) + ((1.0 - ALPHA) * float(prev_MA_values[5]))
			bdw_MA = (ALPHA * float(values[6])) + ((1.0 - ALPHA) * float(prev_MA_values[6]))
			delAcksPct_MA = (ALPHA * float(values[7])) + ((1.0 - ALPHA) * float(prev_MA_values[7]))
			# write the calculated M.A. values to output file
			w_values = [values[0], values[1], values[2], values[3], cpu_MA, cpuMax_MA, bdw_MA, delAcksPct_MA]
			# not sure why this DID need an endline char appended
			w_line = ','.join(map(str, w_values)) + '\n'
			outfile.write(w_line)
			# update prev_MA_values for next M.A. calculation
			prev_MA_values = w_values
	count += 1