from KyurekiCMS import KyurekiCMS
import os

cms = KyurekiCMS()
cms.loadConfig(os.path.join(os.curdir, "SmartboysSite", "config.yaml"))