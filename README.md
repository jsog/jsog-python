# Serializing JavaScript Object Graphs with Python

This Python module serializes and deserializes cyclic object graphs in the [JSOG format](https://github.com/stickfigure/jsog).

## Source code

The official repository is (https://github.com/stickfigure/jsog-python).

## Download

Jsog is available in PyPI:

    $ pip install jsog

## Usage

This code mimics the standard *json* python package:

    import jsog

	string = jsog.dumps(cyclicGraph);
	cyclicGraph = jsog.loads(string);

It can be used to convert between object graphs directly:

    import jsog

	jsogStructure = jsog.encode(cyclicGraph);	// has { '@ref': 'ID' } links instead of cycles
	cyclicGraph = jsog.decode(jsogStructure);

## Author

* Jeff Schnitzer (jeff@infohazard.org)

## License

This software is provided under the [MIT license](http://opensource.org/licenses/MIT)
