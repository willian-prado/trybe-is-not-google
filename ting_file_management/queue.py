class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None

        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError
        return self._data[index]

    def search_by_filename(self, filename):
        for item in self._data:
            if item["nome_do_arquivo"] == filename:
                return True
