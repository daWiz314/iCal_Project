

if __name__ == '__main__':
    try:
        import icalendar
    except ImportError:
        print("We need the icalendar package! Please install via pip!")
        exit(-1)
    