class Simple:
    def format(self, data):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        for name, value in sorted(data.items()):
            line = "{name} = {value}\n".format(
                name=name,
                value=value,
            )
            yield line


x = {"name": "Awin Abi", "age": 39, "key": "value"}

s = Simple()
y = s.format(x)
print(y)

y = list(s.format(x))
print(y)

y = list(s.format(x))
print(y)


def names_to_uppercase_generator(names):
    for name in names:
        name.upper()
        yield name
