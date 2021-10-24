from setuptools import setup, find_packages
    
long_description = 'Sample Instagram Like Scapper.\
      Scrapes likes all of the posts for a particular page and filters posts according to a specific tag in their caption and scrapes all the likes.'
setup(
        name ='igls',
        version ='1.0.0',
        author ='Shreshth Goyal',
        author_email ='shreshthg30@gmail.com',
        url ='https://github.com/shreshthgoyal/igls',
        description ='Instagram Likes Web Scraper.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'igls = igls.main:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords ='instagram web-scrapper python selenium igls shreshth',
        zip_safe = False
)