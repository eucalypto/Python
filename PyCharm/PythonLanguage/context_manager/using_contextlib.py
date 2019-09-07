from contextlib import contextmanager


class MaterialBox:
    def __init__(self, label):
        self.label = label
        self.amount_of_iron = 0
        self.amount_of_wood = 0

    def fill(self):
        print(f"Filling box {self.label} with resources")
        self.amount_of_iron = 10
        self.amount_of_wood = 10

    def take_iron(self):
        self.amount_of_iron -= 1
        print(f"Taking one iron from box {self.label}. Remaining iron: {self.amount_of_iron}.")

    def take_wood(self):
        self.amount_of_wood -= 1
        print(f"Taking one wood from box {self.label}. Remaining wood: {self.amount_of_wood}.")

    def tidy_up(self):
        print(f"Tidying up material box {self.label} for later use")

    def open(self):
        print(f"Open up material box {self.label}")

    def close(self):
        print(f"Closing up material box {self.label}")


@contextmanager
def use_material_box(material_box):
    try:
        print(f"Preparing resource {material_box.label}")
        material_box.open()
        material_box.fill()
        yield material_box
    finally:
        print("Cleanup after work:")
        material_box.tidy_up()
        material_box.close()


def main():
    material_box = MaterialBox("My Box")
    with use_material_box(material_box) as mb:
        print(f"Start using {mb.label}")
        mb.take_wood()
        mb.take_iron()

    # Now we can use the material box many many times with use_material_box()
    # and not worry about cleaning up, because the contnext manager is takin care
    # of it.


if __name__ == '__main__':
    main()
