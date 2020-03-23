from OneM2M import *

##################
table = "4"
##################

server = "http://192.168.1.233:8080"
cse = "/~/in-cse/in-name/"
led_num = "1"  # 1,2,3,4


# ------------------------------------------
# Fill code here to create AE
# specified by the URI
# ------------------------------------------
ae_name = "led"+"-"+table+"-"+led_num
lbl = [led_num,table]
register_ae(server+cse, ae, lbl)
# ------------------------------------------


# ------------------------------------------
# Fill code here to create container in the AE
# specified by the URI
# ------------------------------------------
container_name = "DATA"
create_cnt(server+cse+ae, container_name)
# ------------------------------------------


# ------------------------------------------
# Fill code here to create content_instance
# specified by the URI
# ------------------------------------------
content_instance = 0
create_data_cin(server+cse+ae+"/DATA", content_instance)
# ------------------------------------------

# ------------------------------------------
# Fill code here to get latest content_instance
# specified by the URI
# ------------------------------------------
ret_code, latest_data = get_data(server+cse+ae+"/DATA/la")
print(latest_data)
# ------------------------------------------

# ------------------------------------------
# Fill code here to get URIs of those containers
# that satisfy the specified filtering criteria
# ------------------------------------------
filtered_uri = get_filtered_uri(server+cse+"?fu=1&lbl=home")
print(filtered_uri)
# ------------------------------------------
