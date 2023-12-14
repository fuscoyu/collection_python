
class DemoContext:
    def __init__(self):
        pass

    def __getattr__(self):
        pass


demo_context = DemoContext()

def instance():
    global demo_context
    return demo_context
