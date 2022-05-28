class Text:
    def __init__(self,filename):
        self.filename = filename

    def overwrite(self, args):
        with open(self.filename, 'w') as f:
            f.writelines(args)
    
    def abbreviate(self, args):
        with open(self.filename, 'a') as f:
            f.writelines(args)