

class Date_format:
    def __init__(self,project_name):
        if project_name == "Enron400" or project_name == "Enron800":
            self.data_form="%d-%b-%Y"
        elif project_name == "RealityMining":
            self.data_form = "%d-%b-%Y"
        elif project_name == "Twitter":
            self.data_form="%d_%m"
        else:
            print(" Wrong project")

        self.proj=project_name

    def get_data_form(self):
        return self.data_form

    def get_grond_truth(self):
        if self.proj == "Enron400" or self.proj== "Enron800":
            self.truth= ['13-Dec-2000', '18-Oct-2001', '22-Oct-2001', '19-Nov-2001',
                    '23-Jan-2002', '30-Jan-2002', '04-Feb-2002']
        elif self.proj == "RealityMining":
            self.truth=["05-Sep-2004", "06-Sep-2004", "07-Sep-2004", "08-Sep-2004", "09-Sep-2004", "10-Sep-2004",
                         "11-Sep-2004",     # week 6
                         "17-Oct-2004", "18-Oct-2004", "19-Oct-2004", "20-Oct-2004", "21-Oct-2004", "22-Oct-2004",
                         "23-Oct-2004",     # week 12
                         "24-Oct-2004", "25-Oct-2004", "26-Oct-2004", "27-Oct-2004", "28-Oct-2004", "29-Oct-2004",
                         "30-Oct-2004",     # week 13
                         "07-Nov-2004", "08-Nov-2004", "09-Nov-2004", "10-Nov-2004", "11-Nov-2004", "12-Nov-2004",
                         "13-Nov-2004",     # week 15
                         "14-Nov-2004", "15-Nov-2004", "16-Nov-2004", "17-Nov-2004", "18-Nov-2004", "19-Nov-2004",
                         "20-Nov-2004",     # week 16
                         "21-Nov-2004", "22-Nov-2004", "23-Nov-2004", "24-Nov-2004", "25-Nov-2004", "26-Nov-2004",
                         "27-Nov-2004",     # week 17
                         "05-Dec-2004", "06-Dec-2004", "07-Dec-2004", "08-Dec-2004", "09-Dec-2004", "10-Dec-2004",
                         "11-Dec-2004",     # week 19
                         "12-Dec-2004", "13-Dec-2004", "14-Dec-2004", "15-Dec-2004", "16-Dec-2004", "17-Dec-2004",
                         "18-Dec-2004",     # week 20
                         "19-Dec-2004", "20-Dec-2004", "21-Dec-2004", "22-Dec-2004", "23-Dec-2004", "24-Dec-2004",
                         "25-Dec-2004",     # week 21
                         "26-Dec-2004", "27-Dec-2004", "28-Dec-2004", "29-Dec-2004", "30-Dec-2004", "31-Dec-2004",
                         "01-Jan-2005",     # week 22
                         "02-Jan-2005", "03-Jan-2005", "04-Jan-2005", "05-Jan-2005", "06-Jan-2005", "07-Jan-2005",
                         "08-Jan-2005",     # week 23
                         "30-Jan-2005", "31-Jan-2005", "01-Feb-2005", "02-Feb-2005", "03-Feb-2005", "04-Feb-2005",
                         "05-Feb-2005",     # week 27
                         "27-Feb-2005", "28-Feb-2005", "01-Mar-2005", "02-Mar-2005", "03-Mar-2005", "04-Mar-2005",
                         "05-Mar-2005",     # week 31
                         "06-Mar-2005", "07-Mar-2005", "08-Mar-2005", "09-Mar-2005", "10-Mar-2005", "11-Mar-2005",
                         "12-Mar-2005",     # week 32
                         "20-Mar-2005", "21-Mar-2005", "22-Mar-2005", "23-Mar-2005", "24-Mar-2005", "25-Mar-2005",
                         "26-Mar-2005",     # week 34
                         "27-Mar-2005", "28-Mar-2005", "29-Mar-2005", "30-Mar-2005", "31-Mar-2005", "01-Apr-2005",
                         "02-Apr-2005"]
            return
        elif self.proj == "Twitter":
            self.truth=['13_05', '20_05', '24_05', '30_05', '03_06', '05_06', '06_06', '09_06', '10_06', '11_06',
                    '15_06', '18_06', '19_06', '20_06', '25_06', '26_06', '03_07', '18_07', '30_07']

            return self.truth

    def create_anim_indx(self,time_steps):
        self.get_grond_truth()
        res=[]
        for  i in range(len(time_steps)):
            if time_steps[i] in self.truth:
                res.append(i)
        self.indx= res

    def get_anom_indx(self):
        return self.indx




