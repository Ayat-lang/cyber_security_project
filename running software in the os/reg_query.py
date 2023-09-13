
import os

output = os.popen('reg query HKLM\Software\Microsoft').readlines()

output_list = []

for running_software in output:
    query_result = running_software
    query_result_length = len(query_result)
    common_match = "HKEY_LOCAL_MACHINE\Software\Microsoft\\"
    common_match_length = len(common_match)
    output_list.append(query_result[common_match_length:query_result_length-1])


file = open("output.txt" , "w")

for runing_software in output_list:
    file.write(runing_software + "\n")

file.close()


    















