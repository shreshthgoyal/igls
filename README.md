# IGLS - Instagram Like Scraper

It's a web scraping command line tool based on python and selenium. 

## Description

This is a trial tool for learning purpose as according to Instagram's Terms of Use, Rule 10, Instagram does not allow scraping, crawling and caching any content from Instagram. This tool is developed to scrape likes for particular clubs/organisations following their approval for the same.

This scraper CLI tool, automates flow from user login to getting likes from all the posts. In the latest version of IGLS user can scrape all the likes of a particular page/user and also filter them on the basis of certain tags used in their caption.

This tool is published on PyPi [here](https://pypi.org/project/igls/1.0.0/#files).

## Getting Started

### Dependencies

* All the external dependencies exception Python3 are listed in *requirements.txt* [here](https://github.com/shreshthgoyal/igls/blob/main/requirements.txt).

### Installing

* To setup a basic environment to run this tool locally either user can install package from PyPi and continue.<br>
  ``
  pip install igls==1.0.0
  ``
* Also, user can clone this repository and build in manually
```console
git clone https://github.com/shreshthgoyal/igls.git
cd igls
sudo python3 setup.py install
sudo python3 setup.py sdist bdist_wheel
```

### Executing program
* In the command line user needs to enter the following command to know all the commands till this release.
```
igls -h
```

### Help

As Instagram may blocks IP address of an account if user spams logging in continuously it is advised to use the alternate account which is provided for public pages or user should make an alternate account if they want to scrape a private page.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/shreshthgoyal/igls/blob/main/LICENSE) file for details.
