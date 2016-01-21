# install CLI in the virtualenv
develop:
	ln -fs `pwd` layers/firehose-rsc


create:
	humilis --profile test create --stage TEST humilisenv.yaml


update:
	humilis --profile test update --stage TEST humilisenv.yaml


delete:
	humilis --profile test delete --stage TEST humilisenv.yaml
