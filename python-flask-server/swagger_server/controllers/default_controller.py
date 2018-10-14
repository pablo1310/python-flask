import connexion
import six
import subprocess
import sys
import json
from swagger_server import util
from swagger_server.models.group import Group  # noqa: E501


def group_get(self):  # noqa: E501
    process = subprocess.check_output(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass | ConvertTo-Json"]);
    output_json = json.loads(process)
	#return {'members': output_json}
    return {'members':output_json}
