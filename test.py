from uptime_kuma_api import UptimeKumaApi
from uptime_kuma_api.monitor_type import MonitorType

api = UptimeKumaApi("http://localhost:3001")
api.login("admin", "Password456")

print(api.get_monitors())

result = api.add_monitor(type=MonitorType.HTTP, name="Google", url="https://google.com")
