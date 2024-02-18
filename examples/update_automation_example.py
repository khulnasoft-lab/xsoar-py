from __future__ import print_function
import xsoar_client.xsoar_api
from xsoar_client.xsoar_api.rest import ApiException
from pprint import pprint

api_key = 'YOUR API KEY'
base_url = 'YOUR XSOAR URL'

# create an instance of the API class
api_instance = xsoar_client.configure(base_url=base_url, api_key=api_key, debug=True)
automation_script_filter_wrapper = xsoar_client.xsoar_api.AutomationScriptFilterWrapper()
script = xsoar_client.xsoar_api.AutomationScript()
args = xsoar_client.xsoar_api.Argument()

# Create Arguments
args.name = 'system'
args.required = True
args.default = True
args.description = 'The system name'

# Create Script
script.name = 'D2Remove'
script.enabled = True
script.version = -1
script.type = 'python'
script.arguments = [args]
script.script = '''
result = demisto.executeCommand('d2_remove', demisto.args())

if isError(result[0]):
    demisto.results(result)
else:
    demisto.results('D2 agent removed successfully')
'''

automation_script_filter_wrapper.script = script

try:
    # Create or update automation
    api_response = api_instance.save_or_update_script(
        automation_script_filter_wrapper=automation_script_filter_wrapper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_or_update_script: %s\n" % e)
