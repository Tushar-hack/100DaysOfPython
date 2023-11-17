class TagCloud:
    def __init__(self):
        self.__tag = {}

    def add(self, tag):
        self.__tag[tag.lower()] = self.__tag.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tag.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tag[tag.lower()] = count

    def __len__(self):
        return len(self.__tag)

    def __iter__(self):
        return iter(self.__tag)


cloud = TagCloud()
print(cloud.__dict__)
# Accessing Private Members from outside
print(cloud._TagCloud__tag)

# Any member/variable of a class to make it private you need to prefix it with __.
