import json
import streamlit as st
from code_editor import code_editor


with open('resources/example_custom_buttons_set.json') as json_button_file:
    custom_buttons = json.load(json_button_file)

with open('resources/example_custom_buttons_bar_adj.json') as json_button_file_alt:
    custom_buttons_alt = json.load(json_button_file_alt)

# Load Info bar CSS from JSON file
with open('resources/example_info_bar.json') as json_info_file:
    info_bar = json.load(json_info_file)

# Load Code Editor CSS from file
with open('resources/code_editor.scss') as css_file:
    css_text = css_file.read()

demo_sample_python_code = '''# EXAMPL1E CODE

import string, sys

# If no arguments were given, print a helpful message
if len(sys.argv)==1:
    print 
    sys.exit(0)

# Loop over the arguments
for i in sys.argv[1:]:
    try:
        fahrenheit=float(string.atoi(i))
    except string.atoi_error:
        print repr(i), "not a numeric value"
    else:
        celsius=(fahrenheit-32)*5.0/9.0
        print 'Done' '''

# construct component props dictionary (->Code Editor)
comp_props = {"css": css_text, "globalCSS": ":root {\n  --streamlit-dark-font-family: monospace;\n}"}



btn_settings_editor_btns = [{
    "name": "copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll"],
    "style": {"top": "0rem", "right": "0.4rem"}
}, {
    "name": "update",
    "feather": "RefreshCw",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0rem", "right": "0.4rem"}
}]

height = [19, 22]
language = "python"
theme = "default"
shortcuts = "vscode"
focus = False
btns = custom_buttons_alt

col1, col2 = st.columns([6, 2])
with col1:
    st.markdown("## Demo")

    # construct props dictionary (->Ace Editor)
    ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}
    response_dict = code_editor(demo_sample_python_code, height=height, lang=language, theme=theme, shortcuts=shortcuts,
                                focus=focus, buttons=btns, info=info_bar, props=ace_props)

    if response_dict['type'] == "submit" and len(response_dict['text']) != 0:
        st.write("Response type: ", response_dict['type'])
        st.code(response_dict['text'], language=response_dict['lang'])

