class Math:
    
    def __init__(self, first_number, second_number):
        self.fnumber = first_number
        self.snumber = second_number
        self.fnum_arr = []
        self.snum_arr = []
  
    def get_fnumber(self):
        return self.fnumber
  
    def get_snumber(self):
        return self.snumber
  
    def set_fnumber(self, fnumber):
        self.fnumber = fnumber
        return self
  
    def set_snumber(self, snumber):
        self.snumber = snumber
        return self

    def get_fnum_arr(self):
        return self.fnum_arr

    def set_fnum_arr(self, arr):
        self.fnum_arr = arr
        return self

    def get_snum_arr(self):
        return self.snum_arr

    def set_snum_arr(self, arr):
        self.snum_arr = arr
        return self

    def fnumber_to_arr(self):
        fnum = self.get_fnumber()
        fnum = str(fnum)
        arr = list(fnum)
        self.set_fnum_arr(arr)
        return self

    def snumber_to_arr(self):
        snum = self.get_snumber()
        snum = str(snum)
        arr = list(snum)
        self.set_snum_arr(arr)
        return self

    def len_of_fnum_arr(self):
        return len(self.get_fnum_arr())

    def len_of_snum_arr(self):
        return len(self.get_snum_arr())

    def check_same_lenght(self):
        return self.len_of_fnum_arr() == self.len_of_snum_arr()
        
      
        
        
    
  
    
        


        
        
        
    
  
    
        



