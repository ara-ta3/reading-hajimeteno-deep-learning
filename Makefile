
run: env/bin/jupyter
	$< notebook

clean:
	rm -rf env

env/bin/jupyter:
	$(MAKE) install

install: env/bin/pip
	$< install -r requirements.txt

env/bin/pip:
	$(MAKE) virtualenv

virtualenv:
	virtualenv -p python2 env

download: lib/deel
	cd $</misc && ./getPretrainedModels.sh

lib/deel: lib
	git clone https://github.com/uei/deel.git lib/deel

lib:
	mkdir $@

deel/install: lib/deel
	./lib/deel/misc/getPretrainedModels.sh
