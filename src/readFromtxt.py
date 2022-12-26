class data:
    def __init__(self, time, amplitude):
        self.time = time
        self.amplitude = amplitude
    
    def __str__(self):
        return f"At {self.time}, the amplitude is {self.amplitude}"
        
class readFromtxt:
    def __init__(self, path, name):
        self.name = name
        self.path = path
        
    def __str__(self):
        return f"{self.path}/{self.name}"
    
    def readtxt(self, no_header):
        filename = self.path + "/" + self.name
        print (filename)
        lst_t = []
        lst_amp = []
        with open(filename, "r") as file:
            line_no = 0;
            for line in file:
                if (line_no < no_header):
                    file.readline()
                    line_no +=1;
                else:
                    line = file.readline().strip().split("\t");
                    a = data(line[0], line[1]);
                    line_no +=1;
                    lst_t.append(a.time);
                    lst_amp.append(a.amplitude);
        print ("Extracting text file is done!")
        return (lst_t, lst_amp)