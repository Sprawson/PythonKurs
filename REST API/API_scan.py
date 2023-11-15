import requests
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
base_url = 'http://laas.advaoptical.com/api/'

def get_request(url):
    content = requests.get(url, headers=headers, verify=False)
    return content.json()

results = get_request(base_url+'resources/?search=Wi%C5%9Bniewski')
#for result in results['results']:
 #   print(result['url'])
print(len(results['results']))

ptp_label = "PTP-4-1-C"
ip = "10.130.1.26"
command = "select ml.te_id FROM cn_network_element cn left join ml_topo_mo_ref ml on ml.descr like '%'|| cn.id::text ||'%' " \
                  "where ipaddress like '{}' and ml.descr like '%{}%' and ml.entity_class in " \
                  "('com.adva.nlms.mediation.config.fsp_r7.entity.fibermap.TerminationPointFSP_R7DBImpl');".format(ip, ptp_label)

print(command)