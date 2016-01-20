# install CLI in the virtualenv
develop:
	ln -fs `pwd` layers/firehose-resource


create:
	humilis --profile test create --stage TEST humilis-firehose-resource.yaml


update:
	humilis --profile test update --stage TEST humilis-firehose-resource.yaml


delete:
	humilis --profile test delete --stage TEST humilis-firehose-resource.yaml
