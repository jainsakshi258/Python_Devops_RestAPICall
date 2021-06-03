# python_devops_restapicall
Step 1 : Create simple python application
git clone https://github.com/jainsakshi258/python_docker_movierating.git
cd python_docker_movierating

Step 2 : Create a Dockerfile for this application 
vi Dockerfile
Add following lines of code :
  FROM python  
  COPY . /src  
  CMD ["python", "/src/index.py"]  
 
Step 3 : Build Docker Image using the created Dockerfile
 
docker build -t python_docker_movierating .
docker images
docker run python_docker_movierating
 
Please check that python-api docker image has been created

Check the currently running containers
docker ps
check list of all docker images
docker images



step 4: run the api from command line 
python3 --version 
python3 movie_rating.py

porvide input as movie name 
see the output of movie rating 






sample output here 
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ python3 movie_rating.py 
blade runner
90%
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ python3 movie_rating.py 
tamasha
63%
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ python3 movie_rating.py 
flight club
No Rating Found
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ python3 movie_rating.py 
fight club
79%
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ python3 movie_rating.py 
black mirror
No Rating Found
jainsakshi258gm@ip-172-31-76-59:~/python-api/python_docker_movierating$ cd ..



Optional Steps
if you wish to remove all the images in single command
docker rmi $(docker images -q)

else if you want to export Images to tar file and Import images from tar file. ( Backup Activities )
docker save python_docker_movierating -o images.tar


