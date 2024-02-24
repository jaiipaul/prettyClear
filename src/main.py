import prettyClear.prettyclearer as prettyclearer
import prettyClear.shapes as shapes


def main():
    clearer = prettyclearer.PrettyClearer()
    clearer.shape_registry.register(shapes.Shape('line', '-----__-----'))
    clearer.shape_registry.register(shapes.Shape('short_line', '-----'))
    clearer.run()


if __name__ == '__main__':
    main()
