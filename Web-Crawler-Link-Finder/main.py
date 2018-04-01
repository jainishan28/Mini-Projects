import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating Project '+ directory)
		os.makedirs(directory)

	create_data_files(directory, "https://www.youtube.com/watch?v=pjkZCQTfneQ&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&index=3")


def create_data_files(project_name, base_url):
	queue = project_name+'/queue.txt'
	crawled = project_name+'/crawled.txt'

	if not os.path.isfile(queue):m
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')


def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


def add_data_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data+'\n')


def delete_file_content(path):
	with open(path, 'w'):
		pass


def file_to_set(fileName):
	results = set()
	with open(fileName, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))


def set_to_file(fileName, setName):




if __name__ == '__main__':
	create_project_dir('thenewbostonVideos')
