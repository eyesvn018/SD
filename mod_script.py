import sys

target = r"c:\Users\Trung Anh\Desktop\SDVN-WebUI-c07a775ffca6c11ad1e49b743080e2142d0690cc\SDVN-WebUI-c07a775ffca6c11ad1e49b743080e2142d0690cc\Script.ipynb"

with open(target, 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """    "def xformers_check():\\n",
    "  xformersver = {\\n",
    "    'Forge-v2':'0.0.27.post2',\\n",
    "    'Automatic': '0.0.23.post1',\\n",
    "    'Forge': '0.0.23.post1'\\n",
    "  }\\n",
    "  if Version in xformersver:\\n",
    "    !pip install xformers=={xformersver[Version]}\\n","""

new_str = """    "def xformers_check():\\n",
    "  !pip install -U xformers\\n","""

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replace successful!")
else:
    print("Old string not found in file!")
