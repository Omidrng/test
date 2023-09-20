import requests
import json
import time
import base64

# messagewithconfig = input("Enter message: ")

message = '''
vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogIk9taWROZXR3b3JrIiwNCiAgImFkZCI6ICJkb25ndGFpd2FuZzIuY29tIiwNCiAgInBvcnQiOiAiODA4MCIsDQogICJpZCI6ICIyNTJmOWVjNy00MmU4LTRjNjYtOWE0MS02NzNkOWI4ZTY3OTkiLA0KICAiYWlkIjogIjAiLA0KICAic2N5IjogImF1dG8iLA0KICAibmV0IjogIndzIiwNCiAgInR5cGUiOiAibm9uZSIsDQogICJob3N0IjogImNmMS5mcmVlazEueHl6IiwNCiAgInBhdGgiOiAiL2xSNFB4RkxuLyIsDQogICJ0bHMiOiAiIiwNCiAgInNuaSI6ICIiLA0KICAiYWxwbiI6ICIiLA0KICAiZnAiOiAiIg0KfQ==
vless://82423f93-5452-4321-bab3-948d1a6bd31a@salam.hostv1romid.sbs:54294?encryption=none&security=none&type=tcp&headerType=http&host=5i754763.divarcdn.com%2C5i754763.snappfood.ir%2C5i754763.yjc.ir%2C5i754763.digikala.com%2C5i754763.tic.ir#New-jd04pzxl
vmess://eyJhZGQiOiIyMy44OC4zOC40MiIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiaW50ZXJuZXQubGlmZS5jb20uYnkiLCJpZCI6IjA5MGU1MDRmLWNmMzItNDJkMC1jN2ZjLWI5OWZjNzE0YTUwMyIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwicG9ydCI6IjQ0MyIsInBzIjoidC5tZS9Db25maWdzSHViIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiJodHRwIiwidiI6IjIifQ==
vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogInQubWUvQ29uZmlnc0h1YiIsDQogICJhZGQiOiAiMjMuMTU4LjU2Ljg5IiwNCiAgInBvcnQiOiAiMjIzMjQiLA0KICAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwNCiAgImFpZCI6ICIwIiwNCiAgInNjeSI6ICJhdXRvIiwNCiAgIm5ldCI6ICJ0Y3AiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiIiwNCiAgInRscyI6ICIiLA0KICAic25pIjogIiIsDQogICJhbHBuIjogIiIsDQogICJmcCI6ICIiDQp9
vless://8223232323323232fji-bab3-948d1a6bd31a@salam.hostv1romid.sbs:54294?encryption=none&security=none&type=tcp&headerType=http&host=5i754763.divarcdn.com%2C5i754763.snappfood.ir%2C5i754763.yjc.ir%2C5i754763.digikala.com%2C5i754763.tic.ir#New-jd04pzxl
trojan://824sds93-5452-4321-bab3-948d1a6bd31a@salam.hostv1romid.sbs:54294?encryption=none&security=none&type=tcp&headerType=http&host=5i754763.divarcdn.com%2C5i754763.snappfood.ir%2C5i754763.yjc.ir%2C5i754763.digikala.com%2C5i754763.tic.ir#New-jd04pzxl
ss://824sdsse0f93-5452-4321-bab3-948d1a6bd31a@salam.hostv1romid.sbs:54294?encryption=none&security=none&type=tcp&headerType=http&host=5i754763.divarcdn.com%2C5i754763.snappfood.ir%2C5i754763.yjc.ir%2C5i754763.digikala.com%2C5i754763.tic.ir#New-jd04pzxl
'''

config_count_vmess = message.count("vmess://")
config_count_vless = message.count("vless://")
config_count_trojan = message.count("trojan://")

countloop1 = config_count_trojan + config_count_vless

for z in range(1):
    zhh = message

for i in range(countloop1):
    if "vless://" in zhh or "trojan://" in zhh or "ss://" in zhh:
        if "trojan://" in zhh:
            start_index = zhh.index("trojan://")
        elif "vless://" in zhh:
            start_index = zhh.index("vless://")
        elif "ss://" in zhh:
            start_index = zhh.index("ss://")
    else:
        zasasa = print("sakam")
    configwithad = zhh[start_index:]
    tag_index = configwithad.index("#")
    configwithnoad = configwithad[:tag_index]
    config = configwithnoad + "#OmidNework"
    ipforcheck = config.index("@")
    ip_index = config[ipforcheck:]
    remove_index = ip_index.index(":")
    remove = ip_index[:remove_index]
    configip = remove.replace("@", "")
    zhh = zhh.replace(configwithnoad, "")
    try:
        checkhost = f"https://check-host.net/check-ping?host={configip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

        headerscheckhost = {
            'Accept': 'application/json',
        }

        responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
        responseidcodecheckhost = responseidcheckhost.text
        idgetcheckhost = json.loads(responseidcodecheckhost)
        request_id = idgetcheckhost['request_id']

        time.sleep(5)

        checkhostresult = f"https://check-host.net/check-result/{request_id}"
        responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
        responsepingtxt = responseping.text
        responsepingjson = json.loads(responsepingtxt)

        ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
        ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
        ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
        ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

        ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
        ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
        ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
        ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

        ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
        ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
        ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
        ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

        allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


        tehran = ""
        tabriz = ""
        shiraz = ""


        if 'OK' in allir:
            config1 = config
            countryres = requests.get(f"http://ip-api.com/json/{configip}")
            countryrestext = countryres.text
            countryresjson = json.loads(countryrestext)
            countrycode = countryresjson['countryCode']
            config1c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
            if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                tehran = "Tehran"
            if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                tabriz = "Tabriz"
            if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                shiraz = "Shiraz"
            config1r = tehran + " & " + tabriz + " & " + shiraz
        else:
            a = 'a'
    except:
        error = "zzs"

if "vmess://" in zhh:
    for p in range(config_count_vmess):
        if "fQ==" in zhh:
            try:
                start_index = zhh.index("vmess://")
                configwithad = zhh[start_index:]
                vmessfilter = configwithad.index("fQ==")
                config_vmess_end = configwithad[:vmessfilter]
                config = config_vmess_end + "fQ=="
                zhh = zhh.replace(config, "")
                vmess_config = config
                vmess_config = vmess_config.replace("vmess://", "")
                try:
                    decoded_config = base64.b64decode(vmess_config).decode('utf-8')
                    vmess_data = json.loads(decoded_config)
                    vmess_ip = vmess_data['add']
                except:
                    zswq = "sskdsd"
                vmess_data['ps'] = 'OmidNetwork'
                strjson = json.dumps(vmess_data)
                input_json = f'{strjson}'
                input_data = json.loads(input_json)
                vmess_config = json.dumps(input_data)
                encoded_config = base64.b64encode(vmess_config.encode('utf-8')).decode('utf-8')
                config = "vmess://" + encoded_config

                
                try:
                    checkhost = f"https://check-host.net/check-ping?host={vmess_ip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

                    headerscheckhost = {
                        'Accept': 'application/json',
                    }

                    responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
                    responseidcodecheckhost = responseidcheckhost.text
                    idgetcheckhost = json.loads(responseidcodecheckhost)
                    request_id = idgetcheckhost['request_id']

                    time.sleep(5)

                    checkhostresult = f"https://check-host.net/check-result/{request_id}"
                    responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
                    responsepingtxt = responseping.text
                    responsepingjson = json.loads(responsepingtxt)

                    ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
                    ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
                    ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
                    ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

                    ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
                    ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
                    ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
                    ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

                    ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
                    ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
                    ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
                    ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

                    allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


                    tehran = ""
                    tabriz = ""
                    shiraz = ""


                    if 'OK' in allir:
                        config6 = config
                        countryres = requests.get(f"http://ip-api.com/json/{vmess_ip}")
                        countryrestext = countryres.text
                        countryresjson = json.loads(countryrestext)
                        countrycode = countryresjson['countryCode']
                        config2c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
                        if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                            tehran = "Tehran"
                        if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                            tabriz = "Tabriz"
                        if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                            shiraz = "Shiraz"
                        config2r = tehran + " & " + tabriz + " & " + shiraz

                    else:
                        a = 'a'
                except:
                    asqewe = "wsed"
            except:
                azdg ="sj"
        elif "p9" in zhh:
            try:
                start_index = zhh.index("vmess://")
                configwithad = zhh[start_index:]
                vmessfilter = configwithad.index("p9")
                config_vmess_end = configwithad[:vmessfilter]
                config = config_vmess_end + "p9"
                zhh = zhh.replace(config, "")
                vmess_config = config
                vmess_config = vmess_config.replace("vmess://", "")
                try:
                    decoded_config = base64.b64decode(vmess_config).decode('utf-8')
                    vmess_data = json.loads(decoded_config)
                    vmess_ip = vmess_data['add']
                except:
                    zswq = "sskdsd"
                vmess_data['ps'] = 'OmidNetwork'
                strjson = json.dumps(vmess_data)
                input_json = f'{strjson}'
                input_data = json.loads(input_json)
                vmess_config = json.dumps(input_data)
                encoded_config = base64.b64encode(vmess_config.encode('utf-8')).decode('utf-8')
                config = "vmess://" + encoded_config

                
                try:
                    checkhost = f"https://check-host.net/check-ping?host={vmess_ip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

                    headerscheckhost = {
                        'Accept': 'application/json',
                    }

                    responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
                    responseidcodecheckhost = responseidcheckhost.text
                    idgetcheckhost = json.loads(responseidcodecheckhost)
                    request_id = idgetcheckhost['request_id']

                    time.sleep(5)

                    checkhostresult = f"https://check-host.net/check-result/{request_id}"
                    responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
                    responsepingtxt = responseping.text
                    responsepingjson = json.loads(responsepingtxt)

                    ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
                    ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
                    ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
                    ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

                    ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
                    ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
                    ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
                    ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

                    ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
                    ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
                    ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
                    ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

                    allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


                    tehran = ""
                    tabriz = ""
                    shiraz = ""


                    if 'OK' in allir:
                        config5 = config
                        countryres = requests.get(f"http://ip-api.com/json/{vmess_ip}")
                        countryrestext = countryres.text
                        countryresjson = json.loads(countryrestext)
                        countrycode = countryresjson['countryCode']
                        config3c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
                        if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                            tehran = "Tehran"
                        if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                            tabriz = "Tabriz"
                        if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                            shiraz = "Shiraz"
                        config3r = tehran + " & " + tabriz + " & " + shiraz

                    else:
                        a = 'a'
                except:
                    asqewe = "wsed"
            except:
                azdg ="sj"
        elif "In0=" in zhh:
            try:
                start_index = zhh.index("vmess://")
                configwithad = zhh[start_index:]
                vmessfilter = configwithad.index("In0=")
                config_vmess_end = configwithad[:vmessfilter]
                config = config_vmess_end + "In0="
                zhh = zhh.replace(config, "")
                vmess_config = config
                vmess_config = vmess_config.replace("vmess://", "")
                try:
                    decoded_config = base64.b64decode(vmess_config).decode('utf-8')
                    vmess_data = json.loads(decoded_config)
                    vmess_ip = vmess_data['add']
                except:
                    zswq = "sskdsd"
                vmess_data['ps'] = 'OmidNetwork'
                strjson = json.dumps(vmess_data)
                input_json = f'{strjson}'
                input_data = json.loads(input_json)
                vmess_config = json.dumps(input_data)
                encoded_config = base64.b64encode(vmess_config.encode('utf-8')).decode('utf-8')
                config = "vmess://" + encoded_config

                
                try:
                    checkhost = f"https://check-host.net/check-ping?host={vmess_ip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

                    headerscheckhost = {
                        'Accept': 'application/json',
                    }

                    responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
                    responseidcodecheckhost = responseidcheckhost.text
                    idgetcheckhost = json.loads(responseidcodecheckhost)
                    request_id = idgetcheckhost['request_id']

                    time.sleep(5)

                    checkhostresult = f"https://check-host.net/check-result/{request_id}"
                    responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
                    responsepingtxt = responseping.text
                    responsepingjson = json.loads(responsepingtxt)

                    ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
                    ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
                    ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
                    ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

                    ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
                    ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
                    ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
                    ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

                    ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
                    ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
                    ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
                    ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

                    allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


                    tehran = ""
                    tabriz = ""
                    shiraz = ""


                    if 'OK' in allir:
                        config4 = config
                        countryres = requests.get(f"http://ip-api.com/json/{vmess_ip}")
                        countryrestext = countryres.text
                        countryresjson = json.loads(countryrestext)
                        countrycode = countryresjson['countryCode']
                        config5c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
                        if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                            tehran = "Tehran"
                        if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                            tabriz = "Tabriz"
                        if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                            shiraz = "Shiraz"
                        config4r = tehran + " & " + tabriz + " & " + shiraz

                    else:
                        a = 'a'
                except:
                    asqewe = "wsed"
            except:
                azdg ="sj"
        elif "J9" in zhh:
            try:
                start_index = zhh.index("vmess://")
                configwithad = zhh[start_index:]
                vmessfilter = configwithad.index("p9")
                config_vmess_end = configwithad[:vmessfilter]
                config = config_vmess_end + "p9"
                zhh = zhh.replace(config, "")
                vmess_config = config
                vmess_config = vmess_config.replace("vmess://", "")
                try:
                    decoded_config = base64.b64decode(vmess_config).decode('utf-8')
                    vmess_data = json.loads(decoded_config)
                    vmess_ip = vmess_data['add']
                except:
                    zswq = "sskdsd"
                vmess_data['ps'] = 'OmidNetwork'
                strjson = json.dumps(vmess_data)
                input_json = f'{strjson}'
                input_data = json.loads(input_json)
                vmess_config = json.dumps(input_data)
                encoded_config = base64.b64encode(vmess_config.encode('utf-8')).decode('utf-8')
                config = "vmess://" + encoded_config

                
                try:
                    checkhost = f"https://check-host.net/check-ping?host={vmess_ip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

                    headerscheckhost = {
                        'Accept': 'application/json',
                    }

                    responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
                    responseidcodecheckhost = responseidcheckhost.text
                    idgetcheckhost = json.loads(responseidcodecheckhost)
                    request_id = idgetcheckhost['request_id']

                    time.sleep(5)

                    checkhostresult = f"https://check-host.net/check-result/{request_id}"
                    responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
                    responsepingtxt = responseping.text
                    responsepingjson = json.loads(responsepingtxt)

                    ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
                    ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
                    ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
                    ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

                    ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
                    ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
                    ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
                    ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

                    ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
                    ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
                    ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
                    ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

                    allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


                    tehran = ""
                    tabriz = ""
                    shiraz = ""


                    if 'OK' in allir:
                        config3 = config
                        countryres = requests.get(f"http://ip-api.com/json/{vmess_ip}")
                        countryrestext = countryres.text
                        countryresjson = json.loads(countryrestext)
                        countrycode = countryresjson['countryCode']
                        config6c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
                        if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                            tehran = "Tehran"
                        if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                            tabriz = "Tabriz"
                        if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                            shiraz = "Shiraz"
                        config5r = tehran + " & " + tabriz + " & " + shiraz

                    else:
                        a = 'a'
                except:
                    asqewe = "wsed"
            except:
                azdg ="sj"
        else:
            aews = 'hh'


config_count_ss = zhh.count("ss://")

if "ss://" in zhh:
    for z in range(config_count_ss):
        try:
            start_index = zhh.index("ss://")
            configwithad = zhh[start_index:]
            tag_index = configwithad.index("#")
            configwithnoad = configwithad[:tag_index]
            config = configwithnoad + "#OmidNework"
            ipforcheck = config.index("@")
            ip_index = config[ipforcheck:]
            remove_index = ip_index.index(":")
            remove = ip_index[:remove_index]
            configip = remove.replace("@", "")
            zhh = zhh.replace(configwithnoad, "")
            try:
                checkhost = f"https://check-host.net/check-ping?host={configip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

                headerscheckhost = {
                    'Accept': 'application/json',
                }

                responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
                responseidcodecheckhost = responseidcheckhost.text
                idgetcheckhost = json.loads(responseidcodecheckhost)
                request_id = idgetcheckhost['request_id']

                time.sleep(5)

                checkhostresult = f"https://check-host.net/check-result/{request_id}"
                responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
                responsepingtxt = responseping.text
                responsepingjson = json.loads(responsepingtxt)

                ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
                ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
                ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
                ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

                ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
                ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
                ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
                ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

                ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
                ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
                ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
                ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

                allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


                tehran = ""
                tabriz = ""
                shiraz = ""


                if 'OK' in allir:
                    config2 = config
                    countryres = requests.get(f"http://ip-api.com/json/{configip}")
                    countryrestext = countryres.text
                    countryresjson = json.loads(countryrestext)
                    countrycode = countryresjson['countryCode']
                    config4c = "Country:" + " " + countryresjson['country'] + f"({countrycode})"
                    if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                        tehran = "Tehran"
                    if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                        tabriz = "Tabriz"
                    if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                        shiraz = "Shiraz"
                    config6r = tehran + " & " + tabriz + " & " + shiraz
                else:
                    a = 'a'
            except:
                z = "z"
        except:
            srop = "dd"
else:
    error = 'error'


hhkhat = "_________________________________________"
try:
    realmessage = f"{hhkhat}\n{config1}\n{config1c}\n{config1r}\n{hhkhat}\n{config2}\n{config2c}\n{config2r}\n{hhkhat}\n{config3}\n{config3c}\n{config3r}\n{hhkhat}\n{config4}\n{config4c}\n{config4r}\n{hhkhat}\n{config5}\n{config5c}\n{config5r}\n{hhkhat}\n{config6}\n{config6c}\n{config6r}\n{hhkhat}"
    print(realmessage)
except:
    asasa = "wetdd"