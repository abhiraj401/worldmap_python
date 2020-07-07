# worldmap_python
In this project i am creating map based on coordinates such as longitude and latitude and mark the points on the map using python module Folium.

## Getting Started

### 1. Install Python 2.7 or 3+

If you don't already have Python 3+ installed, grab it from <https://www.python.org/downloads/>. You'll want to download install the latest version of **Python 3.x**. As of 2019-11-22, that is Version 3.8.

### 2. Get Your Location Data

Here you can find out how to download your Google data: <https://support.google.com/accounts/answer/3024190?hl=en></br>
Here you can download all of the data that Google has stored on you: <https://takeout.google.com/>

To use this script, you only need to select and download your "Location History", which Google will provide to you as a JSON file by default.  KML is also an output option and is accepted for this program.

You can also import [GPS Exchange Format (GPX)](https://en.wikipedia.org/wiki/GPS_Exchange_Format) files,
e.g. from a GPS tracker.

### 3. Clone This Repository

On <https://github.com/abhiraj401/worldmp_python>, click the green "Clone or Download" button at the top right of the page. If you want to get started with this script more quickly, click the "Download ZIP" button, and extract the ZIP somewhere on your computer.

### 4. Install Dependencies

In a [command prompt or Terminal window](https://tutorial.djangogirls.org/en/intro_to_command_line/#what-is-the-command-line), [navigate to the directory](https://tutorial.djangogirls.org/en/intro_to_command_line/#change-current-directory) containing this repository's files. Then, type the following, and press enter:

```shell
pip install -r requirements.txt
```

### 5. Run the Script

In the same command prompt or Terminal window, type the following, and press enter:

```shell
python mark_points_on_map.py <file>
```

Replace the string `<file>` from above with the path to any of the following files:

- The `Volcanoes-USA.txt` txt file

