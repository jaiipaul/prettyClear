import prettyClear.prettyclearer as prettyclearer
import prettyClear.shapes as shapes


def main():
    clearer = prettyclearer.PrettyClearer()
    clearer.shape_registry.register(shapes.Shape('line', 'xxxxxxxxxxxx'))
    clearer.shape_registry.register(shapes.Shape('short_line', 'xxxx'))

    clearer.shape_registry.register(shapes.Shape('coeur', ('  xxxx xxxx  \n'
                                                           ' xxxxxxxxxxx \n'
                                                           '  xxxxxxxxx  \n'
                                                           '   xxxxxxx   \n'
                                                           '     xxx     \n')))

    clearer.shape_registry.register(shapes.Shape('triangle', ('   x   \n'
                                                              '  xxx  \n'
                                                              ' xxxxx \n'
                                                              'xxxxxxx')))
    clearer.run()


if __name__ == '__main__':
    main()
