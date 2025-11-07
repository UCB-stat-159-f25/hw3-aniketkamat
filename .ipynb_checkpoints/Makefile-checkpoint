.PHONY: env html clean
ligo:=ligo
env:
	@if conda env list | grep -q "^$(ligo) "; then \
    	conda env update -n $(ligo) -f environment.yml --prune; \
	else \
    	conda env create -f environment.yml; \
	fi
html:
	myst build --html
clean:
	rm -f _build/* _build/**/* figures/* figures/**/* audio/* audio/**/*