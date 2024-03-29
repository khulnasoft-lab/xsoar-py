from __future__ import print_function
import xsoar_client.xsoar_api
from xsoar_client.xsoar_api.rest import ApiException
from pprint import pprint

api_key = 'YOUR API KEY'
base_url = 'YOUR XSOAR URL'

# create an instance of the API class
api_instance = xsoar_client.configure(base_url=base_url, api_key=api_key, debug=True)
widget = xsoar_client.xsoar_api.Widget()

widget.name = 'Active Incidents - Pie chart'
widget.query = '-category:job and -status:archived and -status:closed'
widget.data_type = 'incidents'
widget.widget_type = 'pie'

try:
    # Import a widget
    api_response = api_instance.import_widget(widget=widget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_widget: %s\n" % e)
