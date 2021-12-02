
# Holberton School Project Reviewer

Holberton School Project Reviewer is an app that reviews holberton school
project based on selenium test suites.

## Usage/Examples

In order to build a fresh container you need to navigate to the app directory and type:
### Build
```bash
docker build . --no-cache --force-rm --tag <container_tag>
```

### Run
Now that we have a fresh container that we can working with we can run it using this command:
```bash
docker run <container_tag> <github_url_student_project_directory>
```
### Examples
```bash
docker build . --tag html_checker
...
docker run html_checker https://github.com/atefMck/holbertonschool-web_front_end/tree/master/0x06-responsive_design
...
```


## Authors

- [@Atef Mechken](https://www.github.com/atefMck)

