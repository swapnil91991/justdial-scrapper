# JustDial Scrapper

py_justdial_scrapper is a python module that helps you easily extract data from justdial.

# Features
  - Scrape more-than 100 records in a single run
  - Get complete details including address.

### Installation

Scrapper requires python version 3+ to run.


```py
$ pip install py_justdial_scrapper
```
### Usage

It's object oriented structure makes it easy to use the tool.

Get all records based on city : 

```py
from py_justdial_scrapper import JDScrapper

scrapper = JDScrapper()

# Example : scrapper.scrape('<query>', '<city>')

data = scrapper.scrape('Hardware Shops', 'Nashik')

# Returns ->  [<Query - Noorani Hardware  phone = 912532508457 >, ...]

```

Get all details of a particular merchant:
You will require a ```Query``` object
```py
data = scrapper.scrape('Hardware Shops', 'Nashik')
# Returns ->  [<Query - Noorani Hardware  phone = 912532508457 >, ...]
data[0].get_complete_details()
```

### Development

**Want to contribute? Great!**
***Steps to get started***
- Fork the repository
- Change code
- Submit a pull request

# Contributing

If you liked my work then you hire me for any type of web-scrapping work.
You can reach me through Whatsapp @ **918483900678**
or mail me @ **manjitpardeshi2003@gmail.com**

License
----

MIT

**Free Software, Hell Yeah!**
